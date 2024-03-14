import json
import yaml
import sys

from os.path import join, dirname


def get_recursive(d, dot_string, remove=False):
    keys = dot_string.split('.')
    k = keys.pop(0)
    v = d.get(k, {})
    if k not in d:
        raise KeyError(f"Key '{k}' not found.")
    if not keys:
        if remove:
            del d[k]
        return v
    result = get_recursive(v, '.'.join(keys), remove)
    # remove empty parent
    if remove and not d[k]:
        del d[k]
    return result


def set_recursive(d, dot_string, v, orig_dot_string=''):
    if orig_dot_string == '':
        orig_dot_string = dot_string
    created = False
    keys = dot_string.split('.')
    k = keys.pop(0)
    if k not in d:
        d[k] = {}
        created = True
    if not keys:
        if k in d and not created:
            print(f"Warning: {orig_dot_string} already contains: {d.get(k)} and will be overwritten with: {v}")
        d[k] = v
        return
    set_recursive(d.get(k), '.'.join(keys), v, orig_dot_string)


def if_exists_move_to(config_dict, jsonpath, yamlpath, join_sep=''):
    try:
        o = get_recursive(config_dict, jsonpath, True)
        if join_sep:
            o = join_sep.join(o)
        set_recursive(config_dict, yamlpath, o)
        print(f"Info: {jsonpath} moved to {yamlpath}")
    except KeyError as err:
        print(f"Info: No property for '{jsonpath}' to migrate.")


def remove_and_output(jsondict, jsonpath, msg=''):
    try:
        _ = get_recursive(jsondict, jsonpath, True)
        print(f"Info: Removed {jsonpath}{f'. {msg}' if msg else ''}")
    except KeyError as err:
        print(f"Info: No property for '{jsonpath}' to remove.")


if __name__ == "__main__":
    args = sys.argv[1:]
    in_file = args[0]
    out_file = join(dirname(__file__), 'ors-config.yml')

    print(args)

    if not 0 < len(args) < 3:
        print("Usage: python migrate.py ./your-ors-config.json [./ors-config.yml]")
    elif len(args) == 2:
        out_file = args[1]

    print(f'Migrating file from {in_file} to {out_file}')

    x = json.load(open(join(dirname(__file__), str(in_file))))

    with open(out_file, 'w') as f:
        f.writelines(yaml.dump(x))
        print(f'Wrote yml output to {f.name}')

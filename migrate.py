import json
import yaml
import sys

from os.path import join, dirname

from pydantic import ValidationError

from models.yml_config import OrsConfigYML
from models.json_config import OrsConfigJSON, Parameters, ProfileEntry
from models.json_config_ignore_extras import OrsConfigJSONIgnoreExtras


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


def validate_profiles(json_dict, error_list):
    profiles = json_dict['ors']['services']['routing']['profiles']
    for key, value in profiles.items():
        if key == "active":
            try:
                assert isinstance(value, list)
                for entry in value:
                    assert isinstance(entry, str)
            except AssertionError as err:
                print(f"Wrong type for 'ors.services.routing.profiles.active'")
                error_list.append(e)
                print()
        if key == "default_params":
            try:
                Parameters.model_validate(value)
            except ValidationError as e:
                format_e = '\n'.join(str(e).split('\n')[:2])
                print(
                    f"Unknown config property found in 'ors.services.routing.profiles.default_parameters': {format_e}")
                error_list.append(e)
                print()
        if key.startswith("profile-"):
            try:
                ProfileEntry.model_validate(value)
            except ValidationError as e:
                format_e = '\n'.join(str(e).split('\n')[:2])
                print(f"Unknown config property found in 'ors.services.routing.profiles.{key}': {format_e}")
                error_list.append(e)
                print()


def migrate_logging(x, jsonpath, yamlpath):
    if_exists_move_to(x, f'{jsonpath}.location', f'{yamlpath}.file.name')
    try:
        o = get_recursive(x, jsonpath, True)
        if o.get('level_file'):
            lvl_root = 'WARN'
            lvl_org_heigit = 'INFO'
            match o.get('level_file'):
                case 'DEFAULT_LOGGING.json':
                    lvl_root = 'WARN'
                    lvl_org_heigit = 'INFO'
                case 'PRODUCTION_LOGGING.json':
                    lvl_root = 'WARN'
                    lvl_org_heigit = 'WARN'
                case 'DEBUG_LOGGING.json':
                    lvl_root = 'ERROR'
                    lvl_org_heigit = 'DEBUG'
            set_recursive(x, f'{yamlpath}.level.root', lvl_root)
            set_recursive(x, f'{yamlpath}.level.org.heigit', lvl_org_heigit)

        print(f"Info: {jsonpath}.location moved to {yamlpath}.file.name.")
        print(f"Warning: This was a best effort conversion to the new logging configuration. The logging was heavily "
              f"reworked. Best check how to set up Logging now: "
              f"https://giscience.github.io/openrouteservice/run-instance/configuration/spring/logging")
    except KeyError as e:
        print(f"Info: No property for '{jsonpath}' to migrate.")


def migrate_mode_prop(x, jsonpath, yamlpath):
    try:
        mode = get_recursive(x, jsonpath, True)

        match mode:
            case 'normal':
                mode = False
            case 'preparation':
                mode = True
        if isinstance(mode, bool):
            set_recursive(x, yamlpath, mode)
            print(f'Info: Migrating "{jsonpath}" to "{yamlpath}". Converted string to bool.')
        else:
            print(f'Warning: Malformed property "{jsonpath}". Removed from configuration.')
    except KeyError as e:
        print(f'Info: No property for "{jsonpath}" to migrate.')


def migrate(json_config_path, yaml_config_path):
    """
    Program to migrate an existing ors-config.json to the new ors-config.yml format.
    Includes validation of config input and reports on invalid or non-transferable entries.
    For further information and configuration of ORS via environment variables
    see https://giscience.github.io/openrouteservice/run-instance/configuration
    """
    results = {
        "actions_needed": [],
        "info": [],
        "warnings": [],
        "errors": []
    }
    with open(join(dirname(__file__), str(json_config_path)), 'r') as f:
        x = json.load(f)

    try:
        OrsConfigJSON.model_validate(x)
    except ValidationError as e:
        results['errors'].append(e)

    validate_profiles(x, results["errors"])

    print(f'Migrating file from {json_config_path} to {yaml_config_path}')

    print("\n--- Migrating ors.api_settings ---")
    if_exists_move_to(x, 'ors.api_settings.cors.allowed.origins', 'ors.cors.allowed_origins', ', ')
    if_exists_move_to(x, 'ors.api_settings.cors.allowed.headers', 'ors.cors.allowed_headers', ', ')
    if_exists_move_to(x, 'ors.api_settings.cors.preflight_max_age', 'ors.cors.preflight_max_age')
    remove_and_output(x, 'ors.api_settings.cors.exposed', 'Option was removed. For available options see '
                                                          'https://giscience.github.io/openrouteservice/run-instance/configuration/ors/cors/')

    print("\n--- Migrating ors.system_messages ---")
    if_exists_move_to(x, 'ors.system_messages', 'ors.messages')

    print("\n--- Migrating ors.logging ---")
    migrate_logging(x, 'ors.logging', 'logging')

    print("\n--- Migrating ors.services ---")
    if_exists_move_to(x, 'ors.services', 'ors.endpoints')

    migrate_mode_prop(x, 'ors.endpoints.routing.mode', 'ors.engine.preparation_mode')

    print("\n--- Migrating ors.info ---")
    if_exists_move_to(x, 'ors.info.base_url', 'ors.endpoints.routing.gpx_base_url')
    if_exists_move_to(x, 'ors.info.support_mail', 'ors.endpoints.routing.gpx_support_mail')
    if_exists_move_to(x, 'ors.info.author_tag', 'ors.endpoints.routing.gpx_author')
    if_exists_move_to(x, 'ors.info.content_licence', 'ors.endpoints.routing.gpx_content_licence')
    remove_and_output(x, 'ors.info.swagger_documentation_url', 'TODO: removed?')

    try:
        OrsConfigYML.model_validate(x)
    except ValidationError as e:
        raise e

    with open(yaml_config_path, 'w') as f:
        f.writelines(yaml.dump(x))
        print(f'Wrote yml output to {f.name}')


if __name__ == "__main__":
    args = sys.argv[1:]
    in_file = args[0]
    out_file = join(dirname(__file__), 'ors-config.yml')

    print(args)

    if not 0 < len(args) < 3:
        print("Usage: python migrate.py ./your-ors-config.json [./ors-config.yml]")
    elif len(args) == 2:
        out_file = args[1]
    migrate(in_file, "./ors-config.yml")

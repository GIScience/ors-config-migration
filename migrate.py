import json
import yaml
import sys

from os.path import join, dirname

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

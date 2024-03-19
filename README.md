# ors config migration

this is a tool for migrating from ors-config.json to ors-config.yml.

As with Release 8 a lot of config options have been restructured, this tool should help people
to migrate their configs from JSON to YAML format without hassle, and inform about changes made.

## Usage

For running the migration script you need at least Python version 3.11.


```shell
# create virtual python environment
python3 -m venv .venv

# activate venv
source .venv/bin/activate

# install requirements
python3 -m pip install -r requirements.txt

# run migration script
python3 migrate.py <your-ors-json-config-path> [<optional-output-ors-yml-config-path>]
```

## Testing

If you want to run the schema tests locally:

```shell
# install pytest
python3 -m pip install pytest

# run tests
python3 -m pytest tests
```

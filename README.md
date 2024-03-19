# ors config migration

this is a tool for migrating from ors-config.json to ors-config.yml.

As with Release 8 a lot of config options have been restructured, this tool should help people
to migrate their configs from JSON to YAML format without hassle, and inform about changes made.

## Quick usage with Docker

The following lines will build the ors-config-migrate docker image and run the migration script with the provided `test-config.json` file.
Once the container finishes, the container will be removed and the `test-config.yml` file will be created in the local working directory.
The `test-config.yml` will be a valid yaml file that can be used with the latest version of ORS.

Please examine the container logs to see if there are any warnings or errors concerning the migration.

```shell
# Build the dockerfile
docker build -t local/ors-config-migrate .
# Change into a new working directory
mkdir -p ./config && cd ./config
# Execute the migration script by mounting the local working directory into the container
docker run --rm -v ${PWD}:/app local/ors-config-migrate:latest config-files-json/test-config.json test-config.yml  
```

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

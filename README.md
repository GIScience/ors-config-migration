# ors config migration

this is a tool for migrating from ors-config.json to ors-config.yml.

As with Release 8 a lot of config options have been restructured, this tool should help people
to migrate their configs from JSON to YAML format without hassle, and inform about changes made.

## Usage

To migrate your `ors-config.json`, run the following command in the folder with your config file,
as the current directory is mounted into the container as a volume:

```shell
docker run --rm -v ${PWD}:/app openrouteservice/ors-config-migrate <path-to-your-ors-config.json>  
```

Please examine the container logs (should print to stdout) to see if there are any warnings or
errors concerning the migration.

The migrated `ors-config.yml` will be written to the current working directory.


## Local usage with Python

For running the migration script locally you need at least Python version 3.11.
Clone the repository and run the following commands in the repo-root directory:

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

## Local usage with Docker

The following will build the ors-config-migration docker image locally and run the migration script with the
provided `test-config.json` file.
Once the container finishes, the container will be removed and the `test-config.yml` file will be created in the local
working directory.
Clone the repository and run the following commands in the repo-root directory:

```shell
# Build the dockerfile
docker build -t ors-config-migration:local .
# Change into a new working directory
mkdir -p ./config && cd ./config
# Execute the migration script by mounting the local working directory into the container
docker run --rm -v ${PWD}:/app ors-config-migration:local config-files-json/test-config.json test-config.yml  
```

## Testing

If you want to run the schema tests locally:

```shell
# install pytest
python3 -m pip install pytest

# run tests
python3 -m pytest tests
```

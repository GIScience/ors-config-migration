import json
import yaml
import sys

from os.path import join, dirname

from pydantic import ValidationError

from models.yml_config import OrsConfigYML

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'  # orange on some systems

RESET = '\033[0m'  # called to return to standard terminal text color


def info(text):
    print(GREEN + "Info: " + text + RESET)


def warning(text):
    print(YELLOW + "Warning: " + text + RESET)


def error(text):
    print(RED + "Error: " + text + RESET)


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
            warning(f"{orig_dot_string} already contains: {d.get(k)} and will be overwritten with: {v}")
        d[k] = v
        return
    set_recursive(d.get(k), '.'.join(keys), v, orig_dot_string)


def if_exists_move_to(config_dict, jsonpath, yamlpath, join_sep=''):
    try:
        o = get_recursive(config_dict, jsonpath, True)
        if join_sep:
            o = join_sep.join(o)
        set_recursive(config_dict, yamlpath, o)
        info(f"{jsonpath} moved to {yamlpath}")
    except KeyError as err:
        info(f"No property for '{jsonpath}' to migrate.")


def remove_and_output(jsondict, jsonpath, msg=''):
    try:
        _ = get_recursive(jsondict, jsonpath, True)
        warning(f"Removed {jsonpath}{f'. {msg}' if msg else ''}")
    except KeyError as err:
        info(f"No property for '{jsonpath}' to remove.")


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

        info(f"{jsonpath}.level_file migrated to {yamlpath}.level.root & {yamlpath}.level.org.heigit")
        warning(f"This was a best effort conversion to the new logging configuration. The logging was heavily "
                f"reworked. Best check how to set up Logging now: "
                f"https://giscience.github.io/openrouteservice/run-instance/configuration/spring/logging")
    except KeyError as e:
        info(f"No property for '{jsonpath}' to migrate.")


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
            info(f'Migrating "{jsonpath}" to "{yamlpath}". Converted string to bool.')
        else:
            warning(f'Malformed property "{jsonpath}". Removed from configuration.')
    except KeyError as e:
        info(f'No property for "{jsonpath}" to migrate.')


def migrate_sources(x, jsonpath, yamlpath):
    try:
        sources = get_recursive(x, jsonpath, True)
        set_recursive(x, yamlpath, sources[0])
        info(f'Migrating "{jsonpath}" to "{yamlpath}".'
             f'Converted list of strings to string. Used first item from sources.')
    except KeyError as e:
        warning(
            f'Info: No property for "{jsonpath}" to migrate? An ORS instance without sources doesn\'t make much sense.')


def migrate_elevation(x):
    if_exists_move_to(x, 'ors.services.routing.elevation_preprocessed', 'ors.engine.elevation.preprocessed')
    for key in ['elevation_provider', 'elevation_cache_path', 'elevation_cache_clear']:
        if_exists_move_to(x, f'ors.services.routing.profiles.default_params.{key}',
                          f'ors.engine.elevation.{key.replace("elevation_", "")}')


def migrate_messages(x):
    jsonpath = 'ors.system_message'
    yamlpath = 'ors.messages'
    try:
        msgs = get_recursive(x, jsonpath, True)
        for [i, msg] in enumerate(msgs):
            if 'condition' in msg:
                new_conditions = []
                for [key, value] in msg['condition'].items():
                    new_conditions.append({key: value})
                msg['condition'] = new_conditions
                info(
                    f'Migrating message {i + 1} conditions from Object with key-values to List of Condition Entries '
                    f'with single key-values"')
        set_recursive(x, yamlpath, msgs)
        info(f"{jsonpath} moved to {yamlpath}")
    except KeyError as err:
        info(f"No property for '{jsonpath}' to migrate.")


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

    print(f'Migrating file from {json_config_path} to {yaml_config_path}')

    print("\n--- Migrating ors.api_settings ---")
    if_exists_move_to(x, 'ors.api_settings.cors.allowed.origins', 'ors.cors.allowed_origins', ', ')
    if_exists_move_to(x, 'ors.api_settings.cors.allowed.headers', 'ors.cors.allowed_headers', ', ')
    if_exists_move_to(x, 'ors.api_settings.cors.preflight_max_age', 'ors.cors.preflight_max_age')
    remove_and_output(x, 'ors.api_settings.cors.exposed', 'Option was removed. For available options see '
                                                          'https://giscience.github.io/openrouteservice/run-instance/configuration/ors/cors/')

    print("\n--- Migrating ors.system_messages ---")
    migrate_messages(x)

    print("\n--- Migrating ors.logging ---")
    migrate_logging(x, 'ors.logging', 'logging')

    print("\n--- Migrating elevation provider ---")
    migrate_elevation(x)

    print("\n--- Migrating ors.services ---")
    migrate_mode_prop(x, 'ors.services.routing.mode', 'ors.engine.preparation_mode')
    migrate_sources(x, 'ors.services.routing.sources', 'ors.engine.source_file')
    if_exists_move_to(x, 'ors.services.routing.init_threads', 'ors.engine.init_threads')
    if_exists_move_to(x,
                      'ors.services.isochrones.fastisochrones.profiles.default_params',
                      'ors.engine.profile_default.preparation.methods.fastisochrones')

    remove_and_output(x, 'ors.services.matrix.allow_resolve_locations', 'Option was removed.')
    remove_and_output(x, 'ors.services.routing.distance_approximation', 'Option was removed.')

    if_exists_move_to(x, 'ors.services.routing.profiles', 'ors.engine.profiles')
    if_exists_move_to(x, 'ors.services', 'ors.endpoints')
    if_exists_move_to(x, 'ors.endpoints.routing.description', 'ors.endpoints.routing.gpx_description')
    if_exists_move_to(x, 'ors.endpoints.routing.routing_description', 'ors.endpoints.routing.gpx_description')
    if_exists_move_to(x, 'ors.endpoints.routing.routing_name', 'ors.endpoints.routing.gpx_name')

    print("\n--- Migrating ors.info ---")
    if_exists_move_to(x, 'ors.info.base_url', 'ors.endpoints.routing.gpx_base_url')
    if_exists_move_to(x, 'ors.info.support_mail', 'ors.endpoints.routing.gpx_support_mail')
    if_exists_move_to(x, 'ors.info.author_tag', 'ors.endpoints.routing.gpx_author')
    if_exists_move_to(x, 'ors.info.content_licence', 'ors.endpoints.routing.gpx_content_licence')
    remove_and_output(x,
                      'ors.info.swagger_documentation_url',
                      'Option was removed. For settings related to the swagger-ui see '
                      'https://springdoc.org/properties.html#_swagger_ui_properties')

    print("\n--- Remove kafka settings")
    kafka_text = ('Option was removed due maintenance effort. If you want to keep using this, you need to run an older '
                  'ORS version or migrate the feature yourself!')
    remove_and_output(x, 'ors.kafka_test_cluster', kafka_text)
    remove_and_output(x, 'ors.kafka_consumer', kafka_text)

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

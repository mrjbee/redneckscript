
__author__ = 'mrjbee'

from common.log import debug, info, warn
import json
from pathlib import Path
from common.args import inline_config

def configuration_json(name='config'):
    conf_path = Path(name + '.json')

    configuration = {}
    if conf_path.exists():
        with conf_path.open() as data_file:
            configuration = json.load(data_file)
    else:
        warn("No configuration exists for path = %s", str(conf_path.absolute()))

    local_conf_path = Path(name + '.local.json')

    # Local configuration file exists
    if local_conf_path.exists():
        with local_conf_path as data_file:
            local_configuration = json.load(data_file)
            __merge_json(configuration, local_configuration)
    else:
        debug("No [local] configuration exists for path = %s", str(local_conf_path.absolute()))
    # Inline configuration
    if inline_config():
        debug("Inline configuration: %s", inline_config())
        __merge_json(configuration, json.loads(inline_config()))
    else:
        debug("No [inline] configuration exists")

    debug("Configuration name = '%s' value = %s", name, str(json.dumps(configuration)))
    return configuration


def __merge_json(first, second):
    for key in second:
        first[key] = second[key]
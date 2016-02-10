
__author__ = 'mrjbee'

from common.log import debug, info, warn
import json, sys
from pathlib import Path
from common.args import inline_config, is_tty_mode


def config(name='config'):
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
            merge_configs(configuration, local_configuration)
    else:
        debug("No [local] configuration exists for path = %s", str(local_conf_path.absolute()))
    # Inline configuration
    if inline_config():
        debug("Inline configuration: %s", inline_config())
        merge_configs(configuration, json.loads(inline_config()))
    else:
        debug("No [inline] configuration exists")

    if not is_tty_mode():
        pipe_config = json.load(sys.stdin)
        merge_configs(configuration, pipe_config)

    debug("Configuration name = '%s' value = %s", name, str(json.dumps(configuration)))
    return configuration


def merge_configs(first, second):
    for key in second:
        first[key] = second[key]
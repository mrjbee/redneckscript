__author__ = 'mrjbee'

import os
import atexit
import sys
from common import args
from common.log import prepare, debug, info, warn
import json
from pathlib import Path
from common.args import inline_config, is_tty_mode

SCRIPT_DIRECTORY, SCRIPT_FILENAME = os.path.split(os.path.abspath(sys.argv[0]))

DEF_DESCRIPTION = None
DEF_CONFIG_EXAMPLE = None
DEF_OPTIONS = {}
DEF_CONFIG_NAME = 'redscript'

__EXECUTED = False


def execute(execution):
    global __EXECUTED
    __EXECUTED = True

    if not DEF_DESCRIPTION:
        raise Exception('Please define common.script.DEF_DESCRIPTION')

    if not DEF_CONFIG_EXAMPLE:
        raise Exception('Please define common.script.DEF_CONFIG_EXAMPLE')

    # Initialize arguments
    args.build_args(DEF_DESCRIPTION, DEF_OPTIONS)
    prepare(SCRIPT_FILENAME)
    in_config = config(DEF_CONFIG_NAME)
    answer = execution(in_config, args.SCRIPT_OPTS)

    if is_tty_mode(True):
        print()
        json.dump(answer, sys.stdout, sort_keys=True, indent=4, separators=(',', ': '))
        print()
        print()
    else:
        __merge_configs(config, answer)
        json.dump(config, sys.stdout)


def config(name):
    conf_path = Path(name + '.json')

    configuration = {}
    if conf_path.exists():
        with conf_path.open() as data_file:
            configuration = json.load(data_file)
    else:
        info("No configuration exists for path = %s", str(conf_path.absolute()))

    local_conf_path = Path(name + '.local.json')

    # Local configuration file exists
    if local_conf_path.exists():
        with local_conf_path as data_file:
            local_configuration = json.load(data_file)
            __merge_configs(configuration, local_configuration)
    else:
        debug("No [local] configuration exists for path = %s", str(local_conf_path.absolute()))
    # Inline configuration
    if inline_config():
        debug("Inline configuration: %s", inline_config())
        inline_conf = json.loads(inline_config())
        __merge_configs(configuration, inline_conf)
    else:
        debug("No [inline] configuration exists")

    if not is_tty_mode():
        pipe_config = json.load(sys.stdin)
        __merge_configs(configuration, pipe_config)

    debug("Configuration name = '%s' value = %s", name, str(json.dumps(configuration)))
    return configuration


def __merge_configs(first, second):
    for key in second:
        first[key] = second[key]


def execution_call_check():
    global __EXECUTED
    if not __EXECUTED:
        raise Exception('Please call common.script.execute()')


atexit.register(execution_call_check)
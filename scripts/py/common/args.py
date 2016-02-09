__author__ = 'mrjbee'

import sys
import getopt
import logging

SCRIPT_OPTS = None
SCRIPT_ARGS = None


def describe(usage, **options):
    global SCRIPT_OPTS
    global SCRIPT_ARGS

    short_options = 'vih'
    option_description = ''

    for key in options:
        short_options = short_options+key
        option_description = option_description + '\n -' + key[:1] + ' ' + options[key]

    try:
        SCRIPT_OPTS, SCRIPT_ARGS = getopt.getopt(sys.argv[1:], short_options, ["config="])
        SCRIPT_OPTS = dict(SCRIPT_OPTS)
    except getopt.GetoptError:
        __print_usage(usage, option_description,
                      "-h for help [same] message",
                      "-v or -i for debug or info log level",
                      '--config {\\"key\\":\\"value\\"} for inline configuration')
        sys.exit(2)
    if '-h' in SCRIPT_OPTS:
        __print_usage(usage, option_description,
                      "-h for help [this] message",
                      "-v or -i for debug or info log level",
                      '--config {\\"key\\":\\"value\\"} for inline configuration')
        sys.exit(0)


def __print_usage(usage, options, *extra):
    print()
    print("\t" + usage)
    print()
    print("Options:")
    print(options)
    for extraOption in extra:
        print("\t" + extraOption)


def log_level():
    if SCRIPT_OPTS is None:
        raise Exception('Script forget to call describe()')

    if '-i' in SCRIPT_OPTS.keys():
        return logging.INFO
    elif '-v' in SCRIPT_OPTS.keys():
        return logging.DEBUG
    return logging.WARN


def inline_config():

    if SCRIPT_OPTS is None:
        raise Exception('Script forget to call describe()')

    if '--config' in SCRIPT_OPTS.keys():
        return SCRIPT_OPTS["--config"]
    return None
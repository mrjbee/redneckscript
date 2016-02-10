__author__ = 'mrjbee'

import sys
import getopt
import logging
import json

SCRIPT_OPTS = None
SCRIPT_ARGS = None


def describe(func, usage, **options):
    global SCRIPT_OPTS
    global SCRIPT_ARGS

    short_options = 'vih'
    option_description = ''

    for key in options:
        short_options = short_options+key
        option_description = option_description + '\n -' + key[:1] + ' ' + options[key]

    try:
        SCRIPT_OPTS, SCRIPT_ARGS = getopt.getopt(sys.argv[1:], short_options, ["config=", "tty-mode"])
        SCRIPT_OPTS = dict(SCRIPT_OPTS)
    except getopt.GetoptError:
        __print_usage(usage, option_description)
        sys.exit(2)

    if '-h' in SCRIPT_OPTS:
        __print_usage(usage, option_description)
        sys.exit(0)

    # HAVE TO IMPORT IT HERE BECAUSE OF LOGGING INITIALIZATION
    from common.utils import config, merge_configs

    config = config()
    answer = func(config)
    merge_configs(config, answer)

    if is_tty_mode(True):
        print()
        json.dump(config, sys.stdout, sort_keys=True, indent=4, separators=(',', ': '))
        print()
        print()
    else:
        json.dump(config, sys.stdout)


def __print_usage(usage, options):
    extra = [
        "-h for help [this] message",
        "-v or -i for debug or info log level",
        '--tty-mode force tty mode',
        '--config {\\"key\\":\\"value\\"} for inline configuration'
    ]
    print()
    print("\t" + usage)
    print()
    print("Options:")
    print(options)
    for extraOption in extra:
        print("\t" + extraOption)
    print()


def log_level():
    if SCRIPT_OPTS is None:
        raise Exception('Script forget to call describe()')

    if '-i' in SCRIPT_OPTS.keys():
        return logging.INFO
    elif '-v' in SCRIPT_OPTS.keys():
        return logging.DEBUG
    return logging.WARN


def is_tty_mode(out=False):
    return (sys.stdout.isatty() if out else sys.stdin.isatty()) or ('--tty-mode' in SCRIPT_OPTS.keys())


def inline_config():

    if SCRIPT_OPTS is None:
        raise Exception('Script forget to call describe()')

    if '--config' in SCRIPT_OPTS.keys():
        return SCRIPT_OPTS["--config"]
    return None
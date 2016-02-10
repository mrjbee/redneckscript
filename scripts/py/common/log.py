__author__ = 'mrjbee'
import logging
import sys, os
from common.args import log_level, is_tty_mode

# -----------LOGGING SETUP----------
LOG_LEVEL = log_level()
# -----------LOGGING SETUP END----------

directory, filename = os.path.split(os.path.abspath(sys.argv[0]))
LOGGER = logging.getLogger(filename)

LOGGER_DEFAULT_FORMATTER = logging.Formatter('%(asctime)s [%(name)s - %(levelname)s] %(message)s')
LOGGER.setLevel(LOG_LEVEL)
LOGGER_CONSOLE_HANDLER = logging.StreamHandler(sys.stdout if is_tty_mode(True) else sys.stderr)
LOGGER_CONSOLE_HANDLER.setFormatter(LOGGER_DEFAULT_FORMATTER)
LOGGER.addHandler(LOGGER_CONSOLE_HANDLER)


def debug(msg, *args, **kwargs):
    LOGGER.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    LOGGER.info(msg, *args, **kwargs)


def warn(msg, *args, **kwargs):
    LOGGER.warn(msg, *args, **kwargs)
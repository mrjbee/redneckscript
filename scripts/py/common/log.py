__author__ = 'mrjbee'
import logging
import sys
from common.args import log_level, is_tty_mode

LOGGER = None


def prepare(script_file_name):
    global LOGGER
    log_level_value = log_level()
    LOGGER = logging.getLogger(script_file_name)
    logger_default_formatter = logging.Formatter('%(asctime)s [%(name)s - %(levelname)s] %(message)s')
    LOGGER.setLevel(log_level_value)
    logger_console_handler = logging.StreamHandler(sys.stdout if is_tty_mode(True) else sys.stderr)
    logger_console_handler.setFormatter(logger_default_formatter)
    LOGGER.addHandler(logger_console_handler)


def debug(msg, *args, **kwargs):
    if not LOGGER:
        raise Exception('prepare() not called')
    LOGGER.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    if not LOGGER:
        raise Exception('prepare() not called')
    LOGGER.info(msg, *args, **kwargs)


def warn(msg, *args, **kwargs):
    if not LOGGER:
        raise Exception('prepare() not called')
    LOGGER.warn(msg, *args, **kwargs)
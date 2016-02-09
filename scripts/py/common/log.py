__author__ = 'mrjbee'
import logging
from common.args import log_level

# -----------LOGGING SETUP----------
LOG_LEVEL = log_level()
# -----------LOGGING SETUP END----------

LOGGER = logging.getLogger('REDNECK')

LOGGER_DEFAULT_FORMATTER = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
LOGGER.setLevel(LOG_LEVEL)
LOGGER_CONSOLE_HANDLER = logging.StreamHandler()
LOGGER_CONSOLE_HANDLER.setFormatter(LOGGER_DEFAULT_FORMATTER)
LOGGER.addHandler(LOGGER_CONSOLE_HANDLER)


def debug(msg, *args, **kwargs):
    LOGGER.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    LOGGER.info(msg, *args, **kwargs)


def warn(msg, *args, **kwargs):
    LOGGER.warn(msg, *args, **kwargs)
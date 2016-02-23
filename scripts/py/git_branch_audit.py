__author__ = 'mrjbee'

from common import script

script.DEF_DESCRIPTION = "Retrieve head commits of all branches"
script.DEF_CONFIG_EXAMPLE = {
    'something': "value"
}


def execution(config, opts):
    return {}

script.execute(execution)



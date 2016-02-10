__author__ = 'mrjbee'
import sys

from common.args import describe, is_tty_mode

describe("Retrieve head commits of all branches")

from common import utils

config = utils.configuration_json()
if not is_tty_mode():
    for line in sys.stdin:
        print(">>" + line)

print("End of script")

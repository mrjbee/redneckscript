__author__ = 'mrjbee'
import sys

from common.args import describe

describe("Retrieve head commits of all branches")

from common import utils

config = utils.configuration_json()
if not sys.stdin.isatty():
    for line in sys.stdin:
        print(">>" + line)

print("End of script")

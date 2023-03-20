#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

'''
from Service_Layer.viewer import Visualization
Visualization.print_instances()
Visualization.print_status('R6-d635')
'''

import argparse     # Parser for command-line options, arguments and sub-commands
from Service_Layer.simulator import *

config = argparse.ArgumentParser(
    formatter_class = argparse.RawDescriptionHelpFormatter,
    description = help)
config.add_argument('-l', '--list', action='store_true', help="Show instance list")
config.add_argument('-i', '--instance', default='instance01', help="Select an instance")
config.add_argument('-s', '--status', action='store_true', help="Show instance information")
config.add_argument('-a', '--action', type=int, choices=range(1,7), help="Run an action on instance")
args = config.parse_args()

Simulation.run(args)



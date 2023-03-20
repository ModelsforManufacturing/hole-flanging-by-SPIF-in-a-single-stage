#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

"""

import argparse     # Parser for command-line options, arguments and sub-commands
import textwrap     # Text wrapping and filling

from Service_Layer.mw_data import *
from Service_Layer.mw_adapter import Adapter
from Service_Layer.viewer import Visualization

class Simulation:
    @staticmethod
    def run(args):
        if args.list:
            Visualization.print_instances()

        if args.status:
            instance_name = args.instance
            status = args.status
            Visualization.print_status(instance_name)

        if args.action:
            instance_name = args.instance
            action = args.action
            
            if action==1:
                print('Executing action 1: new experimental test')
                i = DataInstance(instance_name)
                i.new()
                Adapter.fix_properties(instance_name)
                Adapter.ask_for_properties(instance_name)
                Adapter.calculate_flange_height(instance_name)
                Adapter.calculate_tool_path(instance_name)
                Adapter.generate_g_code(instance_name)
            elif action==2:
                print('Executing action 2: prepare specimen')
                Adapter.check_for_specimen(instance_name)
            elif action==3:
                print('Executing action 3: check for fracture')
                Adapter.check_for_fracture(instance_name)
            elif action==4:
                print('Executing action 4: measure flange height')
                Adapter.measure_flange_height(instance_name)
            elif action==5:
                print('Executing action 5: measure strain distribution')
                Adapter.measure_strain_distribution(instance_name)
            elif action==6:
                print('Executing action 6: process experimental results and plot diagrams')
                Adapter.calculate_hole_expansion_ratio(instance_name)
                Adapter.calculate_non_dimensional_flange_height(instance_name)
                Adapter.calculate_non_dimensional_average_thickness(instance_name)
                Adapter.calculate_global_lfr(instance_name)
                Adapter.calculate_lfr_per_tool(instance_name)
                Adapter.plot_global_fld(instance_name)
                Adapter.plot_fld_per_tool(instance_name)
                Adapter.plot_fld_for_successful_tests(instance_name)
                Adapter.plot_fld_for_fractured_tests(instance_name)
                Adapter.plot_h_df(instance_name)
                Adapter.plot_t_t0(instance_name)
            else:
                print('Action not found.')
            Visualization.print_status(instance_name)

help = textwrap.dedent('''\
        MfM simulator: hole-flanging-by-SPIF-in-a-single-stage

        Examples:
            -l
            -i instance01 -s
            -i instance01 -a 1
            
        Actions:
            1 new experimental test
            2 prepare specimen
            3 check for fracture
            4 measure flange height
            5 measure strain distribution
            6 process experimental results and plot diagrams
        
        ''')
            
if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    from Service_Layer.mw_data import DataInstance
    from Service_Layer.mw_adapter import Adapter
    from Service_Layer.viewer import Visualization
    
    import os
    os.chdir('..')
    
    config = argparse.ArgumentParser(
        formatter_class = argparse.RawDescriptionHelpFormatter,
        description = help)
    config.add_argument('-l', '--list', action='store_true', help="Show instance list")
    config.add_argument('-i', '--instance', default='instance01', help="Select an instance")
    config.add_argument('-s', '--status', action='store_true', help="Show instance information")
    config.add_argument('-a', '--action', type=int, choices=range(1,7), help="Run an action on instance")
    args = config.parse_args()

    Simulation.run(args)


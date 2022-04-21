#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

"""

import argparse     # Parser for command-line options, arguments and sub-commands
import textwrap     # Text wrapping and filling

import interfaces.interfaces_service as service
import interfaces.interfaces_data as data
import Service_Layer.extra as extra

description = textwrap.dedent('''\
        MfM simulator: hole-flanging-by-SPIF-in-a-single-stage
        ------------------------------------------------------
        Actions:
        1 configure new experimental test
        2 prepare specimen
        3 perform experiment
        4 measure flange height
        5 measure strain distribution
        6 process experimental results
        7 analyze results
        8 give conclusions
        ------------------------------------------------------
        
        Examples of usage:
        
            simul.py --list
            simul.py --instance instance01 --status
            simul.py --instance instance01 --action 1
            
        where 'instance01' is a directory that contains a config file 'data.ini'
        
        ''')



if __name__ == '__main__':
    # using 'parser' for command-line options

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=description)
    parser.add_argument('-l', '--list', action='store_true', help="Show instance list")
    parser.add_argument('-i', '--instance', default='instance01', help="Select an instance")
    parser.add_argument('-s', '--status', action='store_true', help="Show instance information")
    parser.add_argument('-a', '--action', type=int, choices=range(1,9), help="Run an action on instance")
    args = parser.parse_args()

    if args.list:
        extra.list_instances()

    if args.status:
        instance = args.instance
        status = args.status
        extra.print_status(instance)

    if args.action:
        instance = args.instance
        action = args.action
        
        if action==1:
            print('Executing action 1: configure new experimental test')
            extra.new_instance(instance)
            service.calculate_flange_height(instance)
            service.calculate_tool_path(instance)
            service.generate_g_code(instance)
        elif action==2:
            print('Executing action 2: prepare specimen')
            service.prepare_specimen(instance)
        elif action==3:
            print('Executing action 3: perform hole flanging test')
            service.perform_hole_flanging_test(instance)
        elif action==4:
            print('Executing action 4: measure flange height')
            service.measure_flange_height(instance)
        elif action==5:
            print('Executing action 5: measure strain distribution')
            service.measure_strain_distribution(instance)
        elif action==6:
            print('Executing action 6: process experimental results')
            service.calculate_hole_expansion_ratio(instance)
            service.calculate_non_dimensional_flange_height(instance)
            service.calculate_non_dimensional_average_thickness(instance)
        elif action==7:
            print('Executing action 7: analyze results')
            service.calculate_global_lfr(instance)
            service.calculate_lfr_per_tool(instance)
            service.plot_global_fld(instance)
            service.plot_fld_per_tool(instance)
            service.plot_fld_for_successful_tests(instance)
            service.plot_fld_for_fractured_tests(instance)
            service.plot_h_df(instance)
            service.plot_t_t0(instance)
        else:
            print('Action not found.')
        extra.print_status(instance)


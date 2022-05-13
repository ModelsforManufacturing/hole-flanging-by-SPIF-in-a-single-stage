#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

"""

import argparse     # Parser for command-line options, arguments and sub-commands
import textwrap     # Text wrapping and filling

from interfaces.mediating_controller import MediatingController
from Data_Layer.data import *
from Service_Layer.visualization import Visualization

class Simulation:
    @staticmethod
    def __new_instance(instance_name):
        i = DataInstance(instance_name)
        i.new()

        t0 = 1.6
        d0 = input('Enter pre-cut hole diameter of the specimen (mm): ')
        df = 95.8
        R  = input('Enter tool radius (mm) [6, 8, 10]: ')
        f  = 1000
        sd = 0.2
        ffl = 'files/fracture_forming_limit.csv'
        
        blank_model = BlankModel(t0, d0)
        blank_model.save(instance_name)
        part_model = PartModel(df, 0)
        part_model.save(instance_name)
        forming_tool_model = FormingToolModel(R)
        forming_tool_model.save(instance_name)
        forming_conditions = FormingConditions(f, sd)
        forming_conditions.save(instance_name)
        material_properties = MaterialProperties(ffl)
        material_properties.save(instance_name)

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
                print('Executing action 1: configure new experimental test')
                Simulation.__new_instance(instance_name)
                MediatingController.calculate_flange_height(instance_name)
                MediatingController.calculate_tool_path(instance_name)
                MediatingController.generate_g_code(instance_name)
            elif action==2:
                print('Executing action 2: prepare specimen')
                MediatingController.prepare_specimen(instance_name)
            elif action==3:
                print('Executing action 3: perform hole flanging test')
                MediatingController.perform_hole_flanging_test(instance_name)
            elif action==4:
                print('Executing action 4: measure flange height')
                MediatingController.measure_flange_height(instance_name)
            elif action==5:
                print('Executing action 5: measure strain distribution')
                MediatingController.measure_strain_distribution(instance_name)
            elif action==6:
                print('Executing action 6: process experimental results and plot diagrams')
                MediatingController.calculate_hole_expansion_ratio(instance_name)
                MediatingController.calculate_non_dimensional_flange_height(instance_name)
                MediatingController.calculate_non_dimensional_average_thickness(instance_name)
                MediatingController.calculate_global_lfr(instance_name)
                MediatingController.calculate_lfr_per_tool(instance_name)
                MediatingController.plot_global_fld(instance_name)
                MediatingController.plot_fld_per_tool(instance_name)
                MediatingController.plot_fld_for_successful_tests(instance_name)
                MediatingController.plot_fld_for_fractured_tests(instance_name)
                MediatingController.plot_h_df(instance_name)
                MediatingController.plot_t_t0(instance_name)
            elif action==7:
                print('Executing action 7: analyze results')
                MediatingController.conclusions_for_lfr(instance_name)
                MediatingController.conclusions_for_height(instance_name)
                MediatingController.conclusions_for_thickness(instance_name)
                MediatingController.conclusions_for_t0_r(instance_name)
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
            1 configure new experimental test
            2 prepare specimen
            3 perform experiment
            4 measure flange height
            5 measure strain distribution
            6 process experimental results and plot diagrams
            7 give conclusions
        
        ''')
            
if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    from interfaces.mediating_controller import MediatingController
    from Data_Layer.data import DataInstance
    from Service_Layer.visualization import Visualization
    
    import os
    os.chdir('..')
    
    config = argparse.ArgumentParser(
        formatter_class = argparse.RawDescriptionHelpFormatter,
        description = help)
    config.add_argument('-l', '--list', action='store_true', help="Show instance list")
    config.add_argument('-i', '--instance', default='instance01', help="Select an instance")
    config.add_argument('-s', '--status', action='store_true', help="Show instance information")
    config.add_argument('-a', '--action', type=int, choices=range(1,8), help="Run an action on instance")
    args = config.parse_args()

    Simulation.run(args)


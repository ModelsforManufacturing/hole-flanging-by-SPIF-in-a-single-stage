#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

"""

import Data_Layer.interfaces as data
import Service_Layer.interfaces as service

import argparse     # Parser for command-line options, arguments and sub-commands
import textwrap     # Text wrapping and filling


def a11_t1_calculate_flange_height(instance):
    """
    Activity: A11 Update Design Part
    Task: T1 Calculate flange height
    """
    blank_d, blank_t, part_d, part_h, part_3d, tool_r, plastic, anisotr, fracture, stepdown, feedrate, process_3d, apt, toolpath, analysis, sim_strain, sim_fract, issues_h, manuf_fail, manuf_fract, manuf_h, manuf_d, manuf_photos, analyze_strain, analyze_t, analyze_fractogr, manuf_issues_h = data.retrieve_data(instance)

    part_h = service.calculate_flange_height(blank_d, part_d, issues_h)

    variables = (blank_d, blank_t, part_d, part_h, part_3d, tool_r, plastic, anisotr, fracture, stepdown, feedrate, process_3d, apt, toolpath, analysis, sim_strain, sim_fract, issues_h, manuf_fail, manuf_fract, manuf_h, manuf_d, manuf_photos, analyze_strain, analyze_t, analyze_fractogr, manuf_issues_h)
    data.save_data(variables, instance)
    
    return part_h


def a11_t2_update_cad_model(instance):
    """
    A11 Update Design Part
    T2 Generate CAD Model
    """
    blank_d, blank_t, part_d, part_h, part_3d, tool_r, plastic, anisotr, fracture, stepdown, feedrate, process_3d, apt, toolpath, analysis, sim_strain, sim_fract, issues_h, manuf_fail, manuf_fract, manuf_h, manuf_d, manuf_photos, analyze_strain, analyze_t, analyze_fractogr, manuf_issues_h = data.retrieve_data(instance)

    part_3d = service.generate_cad_model(blank_d, part_d, part_h, part_3d)

    variables = (blank_d, blank_t, part_d, part_h, part_3d, tool_r, plastic, anisotr, fracture, stepdown, feedrate, process_3d, apt, toolpath, analysis, sim_strain, sim_fract, issues_h, manuf_fail, manuf_fract, manuf_h, manuf_d, manuf_photos, analyze_strain, analyze_t, analyze_fractogr, manuf_issues_h)
    data.save_data(variables, instance)
    
    return part_3d







# using 'parser' for command-line options

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        MfM simulator: hole-flanging-by-SPIF-in-a-single-stage
        ------------------------------------------------------
        List of Activities and Tasks:

        A0 - Produce a hole flanged part by SPIF in a single stage
            A1 - Define NC Program
                A11 - Update Design Part
                    T1 - Calculate Flange Height
                    T2 - Generate CAD Model
                A12 - Generate NC
                    T1 - Create NC Model
                    T2 - Simulate NC Model
                    T3 - Generate NC Code
            A2 - Simulate and Analyze SPIF Operation
                A21 - Extract Tool Trajectory
                    T1 - Read next line
                    T2 - Calculate time
                    T3 - Write results
                A22 - Simulate SPIF Process
                    T1 - Create Simulation Model
                    T2 - Run Simulation Model
                A23 - Validate Simulation
                    T1 - Check Fracture
                    T2 - Check Finished Flange
                A24 - Analyze Simulation
                    T1 - Extract strain distribution
                    T2 - Find fracture location
            A3 - Inspect Manufactured Part
                    T1 - Check Finished Flange
                    T2 - Measure Strain Distribution
                    T3 - Measure Thickness Profile
                    T4 - Make Fractographies
        ------------------------------------------------------
        
        Example of usage:
        
            run.py --instance instance01 --task a11t1
            
        where 'instance01' is the directory that contains 'data.ini'
        
        '''))
parser.add_argument('--instance', default='instance01', help="Directory name that contains 'data.ini'")
parser.add_argument('--task', default='a11t1', help="Task of an activity to be executed, example: --task a11t1")
args = parser.parse_args()

if __name__ == '__main__':
    if args.task:
        instance = args.instance
        task = args.task
        
        if task=='a11t1':
            print('Executing A11 Update Design Part, T1 Calculate flange height')
            h = a11_t1_calculate_flange_height(instance)
            print('   flange height = %f mm' % h)
            
        if task=='a11t2':
            print('Executing A11 Update Design Part, T2 Generate CAD Model')
            part3d = a11_t2_update_cad_model(instance)
            print('   part 3d model = %s' % part3d)


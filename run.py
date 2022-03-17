#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

"""

import argparse     # Parser for command-line options, arguments and sub-commands
import textwrap     # Text wrapping and filling

import interfaces.interfaces_service as service


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
                    T1 - Extract Tool Movements
                    T2 - Calculate Path Lengths and Times
                    T3 - Write Results
                A22 - Simulate SPIF Process
                    T1 - Create Simulation Model
                    T2 - Run Simulation Model
                A23 - Validate Simulation
                    T1 - Check Fracture
                    T2 - Check Simulated Flange
                A24 - Analyze Simulation
                    T1 - Extract Strain Distribution
                    T2 - Find Fracture Location
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
            h = service.calculate_flange_height(instance)
            print('   Output: flange height = %f mm' % h)
            
        elif task=='a11t2':
            print('Executing A11 Update Design Part, T2 Generate CAD Model')
            part3d = service.generate_cad_model(instance)
            print('   Output: updated part 3d model = %s' % part3d)

        elif task=='a12t1':
            print('Executing A12 Generate NC, T1 Create NC Model')
            process3d = service.a12_t1_create_nc_model(instance)
            print('   Output: process3d = %s' % process3d)
            
        elif task=='a12t2':
            print('Executing A12 Generate NC, T2 Simulate NC Model')
            process3d = service.a12_t2_simulate_nc_model(instance)
            print('   Output: process3d = %s' % process3d)
            
        elif task=='a12t3':
            print('Executing A12 Generate NC, T3 Generate NC Code')
            apt_code = service.a12_t3_generate_nc_code(instance)
            print('   Output: apt_code = %s' % apt_code)

        elif task=='a21t1':
            print('Executing A21 Extract Tool Trajectory, T1 Extract Tool Movements')
            feedrate_x_y_z = service.extract_tool_movements(instance)
            print('   Output: feedrate_x_y_z = %s ...' % feedrate_x_y_z[:20])
            
        elif task=='a21t2':
            print('Executing A21 Extract Tool Trajectory, T2 Calculate Path Lengths and Times')
            time_x_y_z = service.calculate_path_lengths_and_times(instance)
            print('   Output: time_x_y_z = %s ...' % time_x_y_z[:20])

        elif task=='a21t3':
            print('Executing A21 Extract Tool Trajectory, T3 Write Results')
            toolpath_code = service.write_results(instance)
            print('   Output: toolpath_code = %s' % toolpath_code)
            
        elif task=='a22t1':
            print('Executing A22 Simulate SPIF Process, T1 Create Simulation Model')
            analysis3d_model = service.a22_t1_create_simulation_model(instance)
            print('   Output: analysis3d_model = %s' % analysis3d_model)

        elif task=='a22t2':
            print('Executing A22 Simulate SPIF Process, T2 Run Simulation Model')
            analysis3d_output = service.a22_t2_run_simulation_model(instance)
            print('   Output: analysis3d_output = %s' % analysis3d_output)

        elif task=='a23t1':
            print('Executing A23 Validate Simulation, T1 Check Fracture')
            simul_fracture_location = service.a23_t1_check_fracture(instance)
            print('   Output: simul_fracture_location = %s' % simul_fracture_location)

        elif task=='a23t2':
            print('Executing A23 Validate Simulation, T2 Check Simulated Flange')
            simul_issues_h = service.a23_t2_check_simulated_flange(instance)
            print('   Output: simul_issues_h = %s' % simul_issues_h)

        elif task=='a24t1':
            print('Executing A24 Analyze Simulation, T1 Extract Strain Distribution')
            part_sim_strain = service.a24_t1_extract_strain_distribution(instance)
            print('   Output: part_sim_strain = %s' % part_sim_strain)

        elif task=='a24t2':
            print('Executing A24 Analyze Simulation, T2 Find Fracture Location')
            simul_fracture_location = service.a24_t2_find_fracture_location(instance)
            print('   Output: simul_fracture_location = %s' % simul_fracture_location)

        elif task=='a3t1':
            print('Executing A3 Inspect Manufactured Part, T1 Check Finished Flange')
            manuf_issues_h = service.a3_t1_check_finished_flange(instance)
            print('   Output: manuf_issues_h = %s' % manuf_issues_h)

        elif task=='a3t2':
            print('Executing A3 Inspect Manufactured Part, T2 Measure Strain Distribution')
            analys_strain = service.a3_t2_measure_strain_distribution(instance)
            print('   Output: analys_strain = %s' % analys_strain)

        elif task=='a3t3':
            print('Executing A3 Inspect Manufactured Part, T3 Measure Thickness Profile')
            analys_thickness = service.a3_t3_measure_thickness_profile(instance)
            print('   Output: analys_thickness = %s' % analys_thickness)

        elif task=='a3t4':
            print('Executing A3 Inspect Manufactured Part, T4 Make Fractographies')
            analys_fractogr = service.a3_t4_make_fractographies(instance)
            print('   Output: analys_fractogr = %s' % analys_fractogr)
            
        else:
            print('Task not found.')


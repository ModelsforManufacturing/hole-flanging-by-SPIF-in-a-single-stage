#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

"""

import argparse     # Parser for command-line options, arguments and sub-commands
import textwrap     # Text wrapping and filling

import Data_Layer.interfaces as data
import Service_Layer.interfaces as service


def a11_t1_calculate_flange_height(instance):
    """
    A11 - Update Design Part
    T1  - Calculate flange height
    """
    i = data.Instance(instance)
    blank_d = i.blank_sheet.hole_diameter
    part_d = i.design_part.diameter
    issues_h = i.simulation_issues.flange_height
    
    part_h = service.calculate_flange_height(blank_d, part_d, issues_h)

    i.design_part.height = part_h
    i.save()
    
    return part_h


def a11_t2_update_cad_model(instance):
    """
    A11 - Update Design Part
    T2  - Generate CAD Model
    """
    i = data.Instance(instance)
    blank_d = i.blank_sheet.hole_diameter
    part_d = i.design_part.diameter
    part_h = i.design_part.height
    part_3d = i.design_part.part3d

    part_3d = service.generate_cad_model(blank_d, part_d, part_h, part_3d)

    i.design_part.part3d = part_3d
    i.save()
    
    return part_3d


def a12_t1_create_nc_model(instance):
    """
    A12 - Generate NC
    T1  - Create NC Model
    """
    i = data.Instance(instance)
    part_3d_model = i.design_part.part3d
    tool_radius = i.forming_tool.radius
    stepdown = i.strategy.stepdown
    feedrate = i.strategy.feedrate

    process3d = service.create_nc_model(part_3d_model, tool_radius, stepdown, feedrate)
    
    i.nc_model.process3d = process3d
    i.save()
    
    return process3d


def a12_t2_simulate_nc_model(instance):
    """
    A12 - Generate NC
    T2  - Simulate NC Model
    """
    i = data.Instance(instance)
    process3d = i.nc_model.process3d

    process3d = service.simulate_nc_model(process3d)
    
    i.nc_model.process3d = process3d
    i.save()
    
    return process3d


def a12_t3_generate_nc_code(instance):
    """
    A12 - Generate NC
    T3  - Generate NC Code
    """
    i = data.Instance(instance)
    process3d = i.nc_model.process3d

    apt_code = service.generate_nc_code(process3d)
    
    i.nc_program.apt_code = apt_code
    i.save()
    
    return apt_code


def a21_t1_extract_tool_movements(instance):
    """
    A21 - Extract Tool Trajectory
    T1  - Extract Tool Movements
    """
    i = data.Instance(instance)
    apt_code = i.nc_program.apt_code

    feedrate_x_y_z = service.extract_tool_movements(apt_code)

    return feedrate_x_y_z


def a21_t2_calculate_path_lengths_and_times(instance):
    """
    A12 - Extract Tool Trajectory
    T2  - Calculate Path Lengths and Times
    """
    feedrate_x_y_z = a21_t1_extract_tool_movements(instance)

    time_x_y_z = service.calculate_path_lengths_and_times(feedrate_x_y_z)

    return time_x_y_z


def a21_t3_write_results(instance):
    """
    A12 - Extract Tool Trajectory
    T3  - Write Results
    """
    time_x_y_z = a21_t2_calculate_path_lengths_and_times(instance)

    toolpath_code = service.write_results(instance, time_x_y_z)

    i = data.Instance(instance)
    i.trajectory.toolpath_code = toolpath_code
    i.save()
    
    return toolpath_code


def a22_t1_create_simulation_model(instance):
    """
    A22 - Simulate SPIF Process
    T1  - Create Simulation Model
    """
    i = data.Instance(instance)
    hole_diameter = i.blank_sheet.hole_diameter
    thickness = i.raw_material.thickness
    toolpath_code = i.trajectory.toolpath_code
    elasticity_modulus = i.elastic_behaviour.elasticity_modulus
    poisson_ratio = i.elastic_behaviour.poisson_ratio
    strain_stress_curve = i.plastic_behaviour.strain_stress_curve
    anisotropy_coefficients = i.plastic_behaviour.anisotropy_coefficients

    analysis3d_model = service.create_simulation_model(hole_diameter, thickness, toolpath_code, elasticity_modulus, poisson_ratio, strain_stress_curve, anisotropy_coefficients)
    
    i.simulation_model.analysis3d_model = analysis3d_model
    i.save()
    
    return analysis3d_model


def a22_t2_run_simulation_model(instance):
    """
    A22 - Simulate SPIF Process
    T2  - Run Simulation Model
    """
    i = data.Instance(instance)
    analysis3d_model = i.simulation_model.analysis3d_model

    analysis3d_output = service.run_simulation_model(analysis3d_model)

    i.simulation_results.analysis3d_output = analysis3d_output
    i.save()
    
    return analysis3d_output


def a23_t1_check_fracture(instance):
    """
    A23 - Validate Simulation
    T1  - Check Fracture
    """
    i = data.Instance(instance)
    analysis3d_output = i.simulation_results.analysis3d_output

    simul_fracture_location = service.check_fracture(analysis3d_output)

    i.simulated_part.fracture_location = simul_fracture_location
    i.save()
    
    return simul_fracture_location


def a23_t2_check_simulated_flange(instance):
    """
    A23 - Validate Simulation
    T2  - Check Finished Flange
    """
    i = data.Instance(instance)
    analysis3d_output = i.simulation_results.analysis3d_output

    simul_issues_h = service.check_simulated_flange(analysis3d_output)

    i.simulation_issues.flange_height = simul_issues_h
    i.save()
    
    return simul_issues_h


def a24_t1_extract_strain_distribution(instance):
    """
    A24 - Validate Simulation
    T1  - Extract Strain Distribution
    """
    i = data.Instance(instance)
    analysis3d_output = i.simulation_results.analysis3d_output

    part_sim_strain = service.extract_strain_distribution(analysis3d_output)

    i.simulated_part.strain_distribution = part_sim_strain
    i.save()
    
    return part_sim_strain


def a24_t2_find_fracture_location(instance):
    """
    A24 - Validate Simulation
    T2  - Find Fracture Location
    """
    i = data.Instance(instance)
    simul_strain_distribution = i.simulated_part.strain_distribution
    fracture_curve = i.fracture_behaviour.fracture_curve

    simul_fracture_location = service.find_fracture_location(simul_strain_distribution, fracture_curve)

    i.simulated_part.strain_distribution = simul_fracture_location
    i.save()
    
    return simul_fracture_location


def a3_t1_check_finished_flange(instance):
    """
    A3 - Inspect Manufactured Part
    T1 - Check Finished Flange
    """
    i = data.Instance(instance)
    design_part_h = i.design_part.height
    mfd_part_fail = i.manufactured_part.failed
    mfd_part_h = i.manufactured_part.height
    mfd_part_fract = i.manufactured_part.fracture_location
    mfd_part_d = i.manufactured_part.height

    manuf_issues_h = service.check_finished_flange(design_part_h, mfd_part_fail, mfd_part_h, mfd_part_fract, mfd_part_d)

    i.manufacturing_issues.flange_height = manuf_issues_h
    i.save()
    
    return manuf_issues_h


def a3_t2_measure_strain_distribution(instance):
    """
    A3 - Inspect Manufactured Part
    T2 - Measure Strain Distribution
    """
    i = data.Instance(instance)
    mfd_photos = i.manufactured_part.photos

    analys_strain = service.measure_strain_distribution(mfd_photos)

    i.analyzed_part.strain_distribution = analys_strain
    i.save()
    
    return analys_strain


def a3_t3_measure_thickness_profile(instance):
    """
    A3 - Inspect Manufactured Part
    T3 - Measure Thickness Profile
    """
    i = data.Instance(instance)
    mfd_photos = i.manufactured_part.photos

    analys_thickness = service.measure_thickness_profile(mfd_photos)

    i.analyzed_part.thickness_profile = analys_thickness
    i.save()
    
    return analys_thickness


def a3_t4_make_fractographies(instance):
    """
    A3 - Inspect Manufactured Part
    T4 - Make Fractographies
    """
    i = data.Instance(instance)
    mfd_photos = i.manufactured_part.photos

    analys_fractogr = service.make_fractographies(mfd_photos)

    i.analyzed_part.fractographies = analys_fractogr
    i.save()
    
    return analys_fractogr





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
            h = a11_t1_calculate_flange_height(instance)
            print('   Output: flange height = %f mm' % h)
            
        elif task=='a11t2':
            print('Executing A11 Update Design Part, T2 Generate CAD Model')
            part3d = a11_t2_update_cad_model(instance)
            print('   Output: updated part 3d model = %s' % part3d)

        elif task=='a12t1':
            print('Executing A12 Generate NC, T1 Create NC Model')
            process3d = a12_t1_create_nc_model(instance)
            print('   Output: process3d = %s' % process3d)
            
        elif task=='a12t2':
            print('Executing A12 Generate NC, T2 Simulate NC Model')
            process3d = a12_t2_simulate_nc_model(instance)
            print('   Output: process3d = %s' % process3d)
            
        elif task=='a12t3':
            print('Executing A12 Generate NC, T3 Generate NC Code')
            apt_code = a12_t3_generate_nc_code(instance)
            print('   Output: apt_code = %s' % apt_code)

        elif task=='a21t1':
            print('Executing A21 Extract Tool Trajectory, T1 Extract Tool Movements')
            feedrate_x_y_z = a21_t1_extract_tool_movements(instance)
            print('   Output: feedrate_x_y_z = %s ...' % feedrate_x_y_z[:20])
            
        elif task=='a21t2':
            print('Executing A21 Extract Tool Trajectory, T2 Calculate Path Lengths and Times')
            time_x_y_z = a21_t2_calculate_path_lengths_and_times(instance)
            print('   Output: time_x_y_z = %s ...' % time_x_y_z[:20])

        elif task=='a21t3':
            print('Executing A21 Extract Tool Trajectory, T3 Write Results')
            toolpath_code = a21_t3_write_results(instance)
            print('   Output: toolpath_code = %s' % toolpath_code)
            
        elif task=='a22t1':
            print('Executing A22 Simulate SPIF Process, T1 Create Simulation Model')
            analysis3d_model = a22_t1_create_simulation_model(instance)
            print('   Output: analysis3d_model = %s' % analysis3d_model)

        elif task=='a22t2':
            print('Executing A22 Simulate SPIF Process, T2 Run Simulation Model')
            analysis3d_output = a22_t2_run_simulation_model(instance)
            print('   Output: analysis3d_output = %s' % analysis3d_output)

        elif task=='a23t1':
            print('Executing A23 Validate Simulation, T1 Check Fracture')
            simul_fracture_location = a23_t1_check_fracture(instance)
            print('   Output: simul_fracture_location = %s' % simul_fracture_location)

        elif task=='a23t2':
            print('Executing A23 Validate Simulation, T2 Check Simulated Flange')
            simul_issues_h = a23_t2_check_simulated_flange(instance)
            print('   Output: simul_issues_h = %s' % simul_issues_h)

        elif task=='a24t1':
            print('Executing A24 Analyze Simulation, T1 Extract Strain Distribution')
            part_sim_strain = a24_t1_extract_strain_distribution(instance)
            print('   Output: part_sim_strain = %s' % part_sim_strain)

        elif task=='a24t2':
            print('Executing A24 Analyze Simulation, T2 Find Fracture Location')
            simul_fracture_location = a24_t2_find_fracture_location(instance)
            print('   Output: simul_fracture_location = %s' % simul_fracture_location)

        elif task=='a3t1':
            print('Executing A3 Inspect Manufactured Part, T1 Check Finished Flange')
            manuf_issues_h = a3_t1_check_finished_flange(instance)
            print('   Output: manuf_issues_h = %s' % manuf_issues_h)

        elif task=='a3t2':
            print('Executing A3 Inspect Manufactured Part, T2 Measure Strain Distribution')
            analys_strain = a3_t2_measure_strain_distribution(instance)
            print('   Output: analys_strain = %s' % analys_strain)

        elif task=='a3t3':
            print('Executing A3 Inspect Manufactured Part, T3 Measure Thickness Profile')
            analys_thickness = a3_t3_measure_thickness_profile(instance)
            print('   Output: analys_thickness = %s' % analys_thickness)

        elif task=='a3t4':
            print('Executing A3 Inspect Manufactured Part, T4 Make Fractographies')
            analys_fractogr = a3_t4_make_fractographies(instance)
            print('   Output: analys_fractogr = %s' % analys_fractogr)
            
        else:
            print('Task not found.')


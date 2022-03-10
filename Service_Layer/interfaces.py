#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

Functions to implement the Behaviour Model.

There is a function for each 'Task' of the 'Elementary Activities'.

Format:

def <task>(<input_1>, ...(<input_n>):
    ''' <rule> '''
    if <constraint>:
        <action>
    else:
        <another_action>
    return (<output_1>, ...<output_n>)

"""


""" A11 Update Design Part """

def calculate_flange_height(blank_d, part_d, simul_issues_h):
    ''' Update the flange height according to an equation '''
    
    from Service_Layer.actions.a11_t1_flange_height import flange_height
    part_h = flange_height(part_d, blank_d)
    
    if not part_h > simul_issues_h:
    
        from Service_Layer.actions.a11_t1_flange_height import alternative_flange_height
        part_h = alternative_flange_height(part_d, blank_d, simul_issues_h)
        
    return part_h


def generate_cad_model(blank_d, part_d, part_h, part_3d_model):
    ''' Update a parametrized CAD model with the actual parameters '''

    '''
    TODO: see https://stackoverflow.com/questions/34833407/run-a-catia-macro-with-a-python-script#36212094
    import win32com.client
    catapp = win32com.client.Dispatch('CATIA.Application')
    catapp.StartCommand('Service_Layer/actions/a11_t2_part_3d_model.CATScript')
    '''    
    return part_3d_model
    


""" A12 Generate NC """

def create_nc_model(part_3d_model, tool_radius, stepdown, feedrate):
    ''' Update a parametrized NC model with the actual parameters '''
    process3d = 'pending action implementation'
    return process3d

def simulate_nc_model(process3d):
    ''' Analyse tool path to avoid tool collisions '''
    process3d = 'pending action implementation'
    return process3d

def generate_nc_code(process3d):
    ''' Generate and export the APT code '''
    apt_code = 'pending action implementation'
    return apt_code



""" A21 Extract Tool Trajectory """

def extract_tool_movements(apt_code):
    ''' Read 'apt code' and extract tool movements as a list of data (feedrate, x, y, z) '''
    import io
    
    filename = 'Data_Layer/files/%s' % apt_code
    f = open(filename, 'r')
    apt = f.read()
    f.close()
    
    from Service_Layer.actions.a21_t1_extract_tool_movements import apt2toolpath
    feedrate_x_y_z = apt2toolpath(apt)

    return feedrate_x_y_z

def calculate_path_lengths_and_times(feedrate_x_y_z):
    ''' For each tool movement, calculate the path length and time = lenght/feedrate '''

    from Service_Layer.actions.a21_t2_calculate_path_lengths_and_times import toolpath2time
    time_x_y_z = toolpath2time(feedrate_x_y_z)

    return time_x_y_z

def write_results(instance_name, time_x_y_z):
    ''' Append results according to the simulation solver, e.g. Abaqus: ((time, X), (time, Y), (time, Z)) '''

    from Service_Layer.actions.a21_t3_write_results import create_toolpath_files_for_abaqus
    directory='Data_Layer/%s/' % instance_name
    toolpath_files = create_toolpath_files_for_abaqus(time_x_y_z, directory)
    
    res = [i.replace(directory, '') for i in toolpath_files]
    toolpath_code = '(%s, %s, %s, %s)' % (res[0], res[1], res[2], res[3])
    
    return toolpath_code



""" A22 Simulate SPIF Process """

def create_simulation_model(hole_diameter, thickness, toolpath_code, elasticity_modulus, poisson_ratio, strain_stress_curve, anisotropy_coefficients):
    ''' Update a parametrized Finite Element model with the actual parameters '''
    analysis3d_model = 'pending action implementation'
    return analysis3d_model

def run_simulation_model(analysis3d_model):
    ''' Run solver and confirm success (valid output file) '''
    analysis3d_output = 'pending action implementation'
    return analysis3d_output



""" A23 Validate Simulation """

def check_fracture(analysis3d_output):
    ''' Represent strains in a FLD and compare with fracture curve to determine fracture location: wall, edge or none '''
    simul_fracture_location = 'pending action implementation'
    return simul_fracture_location

def check_simulated_flange(analysis3d_output):
    ''' Check that the forming tool formed the entire flange '''
    simul_issues_h = 999999
    return simul_issues_h



""" A24 Analyze Simulation """

def extract_strain_distribution(analysis3d_output):
    ''' Open '3d analysis output' and extract 'strain distribution' along the flange (to be analyzed in a FLD) '''
    part_sim_strain = 'pending action implementation'
    return part_sim_strain

def find_fracture_location(simul_strain_distribution, fracture_curve):
    ''' Construct a FLD and find fracture location: wall, edge or none '''
    simul_fracture_location = 'pending action implementation'
    return simul_fracture_location



""" A3 Inspect Manufactured Part """

def check_finished_flange(design_part_h, mfd_part_fail, mfd_part_h, mfd_part_fract, mfd_part_d):
    ''' Verify that the forming tool has advanced far enough to form the entire flange '''
    manuf_issues_h = 123456789
    return manuf_issues_h

def measure_strain_distribution(mfd_photos):
    ''' Extract the strain distribution along the outer flange surface '''
    analys_strain = 'pending action implementation'
    return analys_strain

def measure_thickness_profile(mfd_photos):
    ''' Microscopic measurement of cut parts '''
    analys_thickness = 'pending action implementation'
    return analys_thickness

def make_fractographies(mfd_photos):
    ''' Make fractographies of the failure zone for failed tests '''
    analys_fractogr = 'pending action implementation'
    return analys_fractogr




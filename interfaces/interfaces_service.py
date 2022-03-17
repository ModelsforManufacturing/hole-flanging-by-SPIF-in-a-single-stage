#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

This file has been generated automatically.

Functions to implement the Behaviour Model.

Format:

def <task>(<input_1>, ...(<input_n>):
    # <rule>
    if <constraint>:
        <action>
    else:
        <another_action>
    return (<output_1>, ...<output_n>)

'''

import interfaces.interfaces_data as data



def calculate_flange_height(instance):
    '''
    Update the flange height according to an equation

    Arguments:
        diameter_1 -- type: DesignPart.diameter
        hole_diameter_2 -- type: BlankSheet.hole_diameter
        flange_height_3 -- type: SimulationIssues.flange_height
    Output:
        height_1 -- type: DesignPart.height
    '''
    
    i = data.Instance(instance)
    diameter_1 = i.design_part.diameter
    hole_diameter_2 = i.blank_sheet.hole_diameter
    flange_height_3 = i.simulation_issues.flange_height
    
    from Service_Layer.a11_t1_flange_height import flange_height
    height_1 = flange_height(diameter_1, hole_diameter_2)

    if not height_1 > flange_height_3:
        from Service_Layer.a11_t1_flange_height import alternative_flange_height
        height_1 = alternative_flange_height(diameter_1, hole_diameter_2, flange_height_3)

    i.design_part.height = height_1
    i.save()

    return height_1


def generate_cad_model(instance):
    '''
    Update a parametrized CAD model with the actual parameters

    Arguments:
        diameter_1 -- type: DesignPart.diameter
        hole_diameter_2 -- type: BlankSheet.hole_diameter
        height_3 -- type: DesignPart.height
        model_3d_4 -- type: DesignPart.model_3d
    Output:
        model_3d_1 -- type: DesignPart.model_3d
    '''
    
    i = data.Instance(instance)
    diameter_1 = i.design_part.diameter
    hole_diameter_2 = i.blank_sheet.hole_diameter
    height_3 = i.design_part.height
    model_3d_4 = i.design_part.model_3d
    
    # INSERT YOUR CODE HERE


    i.design_part.model_3d = model_3d_1
    i.save()

    return model_3d_1


def extract_tool_movements(instance):
    '''
    Read 'apt code' and extract tool movements as a list of data (feedrate, x, y, z)

    Arguments:
        apt_code_1 -- type: NCProgram.apt_code
    Output:
        feedrate_x_y_z_1 -- type: object
    '''
    
    i = data.Instance(instance)
    apt_code_1 = i.nc_program.apt_code
    
    import io
    filename = 'Data_Layer/files/%s' % apt_code_1
    f = open(filename, 'r')
    apt = f.read()
    f.close()
    
    from Service_Layer.a21_t1_extract_tool_movements import apt2toolpath
    feedrate_x_y_z_1 = apt2toolpath(apt)

    return feedrate_x_y_z_1


def calculate_path_lengths_and_times(instance):
    '''
    For each tool movement, calculate the path length and time = lenght/feedrate

    Arguments:
        feedrate_x_y_z_1 -- type: object
    Output:
        time_x_y_z_1 -- type: object
    '''
    
    feedrate_x_y_z_1 = extract_tool_movements(instance)

    from Service_Layer.a21_t2_calculate_path_lengths_and_times import toolpath2time
    time_x_y_z_1 = toolpath2time(feedrate_x_y_z_1)

    return time_x_y_z_1


def write_results(instance):
    '''
    Append results according to the simulation solver, e.g. Abaqus: ((time, X), (time, Y), (time, Z))

    Arguments:
        time_x_y_z_1 -- type: object
    Output:
        toolpath_code_1 -- type: ToolTrajectory.toolpath_code
    '''
    
    time_x_y_z_1 = calculate_path_lengths_and_times(instance)

    from Service_Layer.a21_t3_write_results import create_toolpath_files_for_abaqus
    directory='Data_Layer/%s/' % instance
    toolpath_files = create_toolpath_files_for_abaqus(time_x_y_z_1, directory)
    res = [i.replace(directory, '') for i in toolpath_files]
    toolpath_code_1 = '(%s, %s, %s, %s)' % (res[0], res[1], res[2], res[3])

    i = data.Instance(instance)
    i.tool_trajectory.toolpath_code = toolpath_code_1
    i.save()

    return toolpath_code_1


def create_nc_model(instance):
    '''
    Update a parametrized NC model with the actual parameters

    Arguments:
        part_3d_1 -- type: DesignPart.part_3d
        radius_2 -- type: FormingTool.radius
        step_down_3 -- type: Strategy.step_down
        feedrate_4 -- type: Strategy.feedrate
    Output:
        process_3d_1 -- type: NCModel.process_3d
    '''
    
    i = data.Instance(instance)
    part_3d_1 = i.design_part.part_3d
    radius_2 = i.forming_tool.radius
    step_down_3 = i.strategy.step_down
    feedrate_4 = i.strategy.feedrate
    
    # INSERT YOUR CODE HERE


    i.nc_model.process_3d = process_3d_1
    i.save()

    return process_3d_1


def simulate_nc_model(instance):
    '''
    Analyse tool path to avoid tool collisions

    Arguments:
        process_3d_1 -- type: NCModel.process_3d
    Output:
        process_3d_1 -- type: NCModel.process_3d
    '''
    
    i = data.Instance(instance)
    process_3d_1 = i.nc_model.process_3d
    
    # INSERT YOUR CODE HERE


    i.nc_model.process_3d = process_3d_1
    i.save()

    return process_3d_1


def generate_nc_code(instance):
    '''
    Generate and export the APT code

    Arguments:
        process_3d_1 -- type: NCModel.process_3d
    Output:
        apt_code_1 -- type: NCProgram.apt_code
    '''
    
    i = data.Instance(instance)
    process_3d_1 = i.nc_model.process_3d
    
    # INSERT YOUR CODE HERE


    i.nc_program.apt_code = apt_code_1
    i.save()

    return apt_code_1


def extract_strain_distribution(instance):
    '''
    Open '3d analysis output' and extract 'strain distribution' along the flange (to be analyzed in a FLD)

    Arguments:
        analysis_output_1 -- type: SimulationResults.analysis_output
    Output:
        strain_distribution_1 -- type: SimulatedPart.strain_distribution
    '''
    
    i = data.Instance(instance)
    analysis_output_1 = i.simulation_results.analysis_output
    
    # INSERT YOUR CODE HERE


    i.simulated_part.strain_distribution = strain_distribution_1
    i.save()

    return strain_distribution_1


def find_fracture_location(instance):
    '''
    Construct a FLD and find fracture location: wall, edge or none

    Arguments:
        strain_distribution_1 -- type: SimulatedPart.strain_distribution
        fracture_curve_2 -- type: Fracturebehaviour.fracture_curve
    Output:
        fracture_location_1 -- type: SimulatedPart.fracture_location
    '''
    
    i = data.Instance(instance)
    strain_distribution_1 = i.simulated_part.strain_distribution
    fracture_curve_2 = i.fracture_behaviour.fracture_curve
    
    # INSERT YOUR CODE HERE


    i.simulated_part.fracture_location = fracture_location_1
    i.save()

    return fracture_location_1


def check_fracture(instance):
    '''
    Represent strains in a FLD and compare with fracture curve to determine fracture location: wall, edge or none

    Arguments:
        analysis_output_1 -- type: SimulationResults.analysis_output
    Output:
        fracture_location_1 -- type: SimulatedPart.fracture_location
    '''
    
    i = data.Instance(instance)
    analysis_output_1 = i.simulation_results.analysis_output
    
    # INSERT YOUR CODE HERE


    i.simulated_part.fracture_location = fracture_location_1
    i.save()

    return fracture_location_1


def check_simulated_flange(instance):
    '''
    Check that the forming tool formed the entire flange

    Arguments:
        analysis_output_1 -- type: SimulationResults.analysis_output
    Output:
        flange_height_1 -- type: SimulationIssues.flange_height
    '''
    
    i = data.Instance(instance)
    analysis_output_1 = i.simulation_results.analysis_output
    
    # INSERT YOUR CODE HERE


    i.simulation_issues.flange_height = flange_height_1
    i.save()

    return flange_height_1


def check_finished_flange(instance):
    '''
    Verify that the forming tool has advanced far enough to form the entire flange

    Arguments:
        height_1 -- type: DesignPart.height
        failed_2 -- type: ManufacturedPart.failed
        height_3 -- type: ManufacturedPart.height
        fracture_location_4 -- type: ManufacturedPart.fracture_location
        diameter_5 -- type: ManufacturedPart.diameter
    Output:
        flange_height_1 -- type: ManufacturingIssues.flange_height
    '''
    
    i = data.Instance(instance)
    height_1 = i.design_part.height
    failed_2 = i.manufactured_part.failed
    height_3 = i.manufactured_part.height
    fracture_location_4 = i.manufactured_part.fracture_location
    diameter_5 = i.manufactured_part.diameter
    
    # INSERT YOUR CODE HERE


    i.manufacturing_issues.flange_height = flange_height_1
    i.save()

    return flange_height_1


def measure_strain_distribution(instance):
    '''
    Extract the strain distribution along the outer flange surface

    Arguments:
        photos_1 -- type: ManufacturedPart.photos
    Output:
        strain_distribution_1 -- type: AnalyzedPart.strain_distribution
    '''
    
    i = data.Instance(instance)
    photos_1 = i.manufactured_part.photos
    
    # INSERT YOUR CODE HERE


    i.analyzed_part.strain_distribution = strain_distribution_1
    i.save()

    return strain_distribution_1


def measure_thickness_profile(instance):
    '''
    Microscopic measurement of cut parts

    Arguments:
        photos_1 -- type: ManufacturedPart.photos
    Output:
        thickness_profile_1 -- type: AnalyzedPart.thickness_profile
    '''
    
    i = data.Instance(instance)
    photos_1 = i.manufactured_part.photos
    
    # INSERT YOUR CODE HERE


    i.analyzed_part.thickness_profile = thickness_profile_1
    i.save()

    return thickness_profile_1


def make_fractographies(instance):
    '''
    Make fractographies of the failure zone for failed tests

    Arguments:
        photos_1 -- type: ManufacturedPart.photos
    Output:
        fractographies_1 -- type: AnalyzedPart.fractographies
    '''
    
    i = data.Instance(instance)
    photos_1 = i.manufactured_part.photos
    
    # INSERT YOUR CODE HERE


    i.analyzed_part.fractographies = fractographies_1
    i.save()

    return fractographies_1


def create_simulation_model(instance):
    '''
    Update a parametrized Finite Element model with the actual parameters

    Arguments:
        hole_diameter_1 -- type: BlankSheet.hole_diameter
        thickness_2 -- type: RawMaterial.thickness
        toolpath_code_3 -- type: ToolTrajectory.toolpath_code
        elasticity_modulus_4 -- type: Elasticbehaviour.elasticity_modulus
        poisson_ratio_5 -- type: Elasticbehaviour.poisson_ratio
        strain_stress_curve_6 -- type: Plasticbehaviour.strain_stress_curve
        anisotropy_coefficients_7 -- type: Plasticbehaviour.anisotropy_coefficients
    Output:
        analysis_model_1 -- type: SimulationModel.analysis_model
    '''
    
    i = data.Instance(instance)
    hole_diameter_1 = i.blank_sheet.hole_diameter
    thickness_2 = i.raw_material.thickness
    toolpath_code_3 = i.tool_trajectory.toolpath_code
    elasticity_modulus_4 = i.elastic_behaviour.elasticity_modulus
    poisson_ratio_5 = i.elastic_behaviour.poisson_ratio
    strain_stress_curve_6 = i.plastic_behaviour.strain_stress_curve
    anisotropy_coefficients_7 = i.plastic_behaviour.anisotropy_coefficients
    
    # INSERT YOUR CODE HERE


    i.simulation_model.analysis_model = analysis_model_1
    i.save()

    return analysis_model_1


def run_simulation_model(instance):
    '''
    Run solver and confirm success (valid output file)

    Arguments:
        analysis_model_1 -- type: SimulationModel.analysis_model
    Output:
        analysis_output_1 -- type: SimulationResults.analysis_output
    '''
    
    i = data.Instance(instance)
    analysis_model_1 = i.simulation_model.analysis_model
    
    # INSERT YOUR CODE HERE


    i.simulation_results.analysis_output = analysis_output_1
    i.save()

    return analysis_output_1


    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

This file has been generated automatically.
'''

class BehaviourInterface:

    def calculate_non_dimensional_flange_height(self,
        is_fractured_1: str,
        flange_height_2: float,
        diameter_3: float) -> float:
    '''
    Only if no part fracture was found, calculate h/df.

    Arguments:
        is_fractured_1 -- type: TestResults.is_fractured
        flange_height_2 -- type: TestResults.flange_height
        diameter_3 -- type: PartModel.diameter
    Output:
        non_dimensional_flange_height_1 -- type: TestResults.non_dimensional_flange_height
    '''
    pass

    def calculate_hole_expansion_ratio(self,
        is_fractured_1: str,
        diameter_2: float,
        hole_diameter_3: float) -> float:
    '''
    Only if no part fracture was found, calculate HER=df/d0.

    Arguments:
        is_fractured_1 -- type: TestResults.is_fractured
        diameter_2 -- type: PartModel.diameter
        hole_diameter_3 -- type: BlankModel.hole_diameter
    Output:
        hole_expansion_ratio_1 -- type: TestResults.hole_expansion_ratio
    '''
    pass

    def calculate_non_dimensional_average_thickness(self,
        is_fractured_1: str,
        flange_height_2: float,
        hole_diameter_3: float,
        diameter_4: float,
        thickness_5: float) -> float:
    '''
    Only if no part fracture was found, calculate the average thickness t by volume conservation and return t/t0.

    Arguments:
        is_fractured_1 -- type: TestResults.is_fractured
        flange_height_2 -- type: TestResults.flange_height
        hole_diameter_3 -- type: BlankModel.hole_diameter
        diameter_4 -- type: PartModel.diameter
        thickness_5 -- type: BlankModel.thickness
    Output:
        non_dimensional_average_thickness_1 -- type: TestResults.non_dimensional_average_thickness
    '''
    pass

    def calculate_flange_height(self,
        thickness_1: float,
        hole_diameter_2: float,
        diameter_3: float,
        radius_4: float) -> float:
    '''
    Estimate the theoretical flange height of the part to be manufactured taking into account that the thickness distribution will be no homogeneous

    Arguments:
        thickness_1 -- type: BlankModel.thickness
        hole_diameter_2 -- type: BlankModel.hole_diameter
        diameter_3 -- type: PartModel.diameter
        radius_4 -- type: FormingToolModel.radius
    Output:
        flange_height_1 -- type: PartModel.flange_height
    '''
    pass

    def measure_strain_distribution(self,
        is_fractured_1: str) -> str:
    '''
    Either fracture was found or not, ask for the measured strain distribution along the flange.

    Arguments:
        is_fractured_1 -- type: TestResults.is_fractured
    Output:
        strain_distribution_1 -- type: TestResults.strain_distribution
    '''
    pass

    def measure_flange_height(self,
        is_fractured_1: str) -> float:
    '''
    Only if no part fracture was found, ask for the measured flange height.

    Arguments:
        is_fractured_1 -- type: TestResults.is_fractured
    Output:
        flange_height_1 -- type: TestResults.flange_height
    '''
    pass

    def calculate_lfr_per_tool(self,
        radius_1: float,
        hole_expansion_ratio_2: float,
        is_fractured_3: str) -> float:
    '''
    For all unfractured specimens tested by the same forming tool, calculate LFR=max(HER).

    Arguments:
        radius_1 -- type: FormingToolModel.radius
        hole_expansion_ratio_2 -- type: TestResults.hole_expansion_ratio
        is_fractured_3 -- type: TestResults.is_fractured
    Output:
        lfr_per_tool_1 -- type: LFR.lfr_per_tool
    '''
    pass

    def calculate_global_lfr(self,
        hole_expansion_ratio_1: float,
        is_fractured_2: str) -> float:
    '''
    For all unfractured specimens, calculate LFR=max(HER).

    Arguments:
        hole_expansion_ratio_1 -- type: TestResults.hole_expansion_ratio
        is_fractured_2 -- type: TestResults.is_fractured
    Output:
        global_lfr_1 -- type: LFR.global_lfr
    '''
    pass

    def plot_t_t0(self,
        non_dimensional_average_thickness_1: float) -> str:
    '''
    Plot t/t0 vs. HER of successful hole-ﬂanged sheets

    Arguments:
        non_dimensional_average_thickness_1 -- type: TestResults.non_dimensional_average_thickness
    Output:
        average_thickness_diagram_1 -- type: TechnologicalParameters.average_thickness_diagram
    '''
    pass

    def plot_h_df(self,
        non_dimensional_flange_height_1: float) -> str:
    '''
    Plot h/df vs. HER of successful hole-ﬂanged sheets

    Arguments:
        non_dimensional_flange_height_1 -- type: TestResults.non_dimensional_flange_height
    Output:
        flange_height_diagram_1 -- type: TechnologicalParameters.flange_height_diagram
    '''
    pass

    def conclusions_for_height(self,
        flange_height_diagram_1: str) -> str:
    '''
    Write conclusions for flange height

    Arguments:
        flange_height_diagram_1 -- type: TechnologicalParameters.flange_height_diagram
    Output:
        flange_height_1 -- type: Conclusions.flange_height
    '''
    pass

    def conclusions_for_t0_r(self,
        average_thickness_diagram_1: str,
        flange_height_diagram_2: str,
        global_fld_3: str,
        fld_per_tool_4: str,
        fld_for_successful_tests_5: str,
        fld_for_fractured_tests_6: str,
        global_lfr_7: float,
        lfr_per_tool_8: float) -> str:
    '''
    Write conclusions for bending ratio

    Arguments:
        average_thickness_diagram_1 -- type: TechnologicalParameters.average_thickness_diagram
        flange_height_diagram_2 -- type: TechnologicalParameters.flange_height_diagram
        global_fld_3 -- type: FLD.global_fld
        fld_per_tool_4 -- type: FLD.fld_per_tool
        fld_for_successful_tests_5 -- type: FLD.fld_for_successful_tests
        fld_for_fractured_tests_6 -- type: FLD.fld_for_fractured_tests
        global_lfr_7 -- type: LFR.global_lfr
        lfr_per_tool_8 -- type: LFR.lfr_per_tool
    Output:
        bending_ratio_1 -- type: Conclusions.bending_ratio
    '''
    pass

    def conclusions_for_lfr(self,
        global_lfr_1: float,
        lfr_per_tool_2: float) -> str:
    '''
    Write conclusions for LFR

    Arguments:
        global_lfr_1 -- type: LFR.global_lfr
        lfr_per_tool_2 -- type: LFR.lfr_per_tool
    Output:
        limit_forming_ratio_1 -- type: Conclusions.limit_forming_ratio
    '''
    pass

    def conclusions_for_thickness(self,
        average_thickness_diagram_1: str) -> str:
    '''
    Write conclusions for average thickness

    Arguments:
        average_thickness_diagram_1 -- type: TechnologicalParameters.average_thickness_diagram
    Output:
        average_thickness_1 -- type: Conclusions.average_thickness
    '''
    pass

    def perform_hole_flanging_test(self,
        g_code_1: str,
        is_prepared_2: str) -> str:
    '''
    Verify that the specimen is prepared, show information about the NC program to be executed and, wait for the experimental test, and ask if fracture occurred.

    Arguments:
        g_code_1 -- type: NCProgram.g_code
        is_prepared_2 -- type: Specimen.is_prepared
    Output:
        is_fractured_1 -- type: TestResults.is_fractured
    '''
    pass

    def plot_fld_per_tool(self,
        strain_distribution_1: str,
        fracture_forming_limit_2: str,
        radius_3: float) -> str:
    '''
    Plot a FLD for all specimens tested by the same forming tool

    Arguments:
        strain_distribution_1 -- type: TestResults.strain_distribution
        fracture_forming_limit_2 -- type: MaterialProperties.fracture_forming_limit
        radius_3 -- type: FormingToolModel.radius
    Output:
        fld_per_tool_1 -- type: FLD.fld_per_tool
    '''
    pass

    def plot_fld_for_fractured_tests(self,
        strain_distribution_1: str,
        fracture_forming_limit_2: str,
        is_fractured_3: str) -> str:
    '''
    Plot a FLD for all failed tests closest to success

    Arguments:
        strain_distribution_1 -- type: TestResults.strain_distribution
        fracture_forming_limit_2 -- type: MaterialProperties.fracture_forming_limit
        is_fractured_3 -- type: TestResults.is_fractured
    Output:
        fld_for_fractured_tests_1 -- type: FLD.fld_for_fractured_tests
    '''
    pass

    def plot_global_fld(self,
        strain_distribution_1: str,
        fracture_forming_limit_2: str) -> str:
    '''
    Plot the FLD for all specimens

    Arguments:
        strain_distribution_1 -- type: TestResults.strain_distribution
        fracture_forming_limit_2 -- type: MaterialProperties.fracture_forming_limit
    Output:
        global_fld_1 -- type: FLD.global_fld
    '''
    pass

    def plot_fld_for_successful_tests(self,
        strain_distribution_1: str,
        fracture_forming_limit_2: str,
        is_fractured_3: str) -> str:
    '''
    Plot a FLD for all successful tests with the minimum pre-cut hole diameters

    Arguments:
        strain_distribution_1 -- type: TestResults.strain_distribution
        fracture_forming_limit_2 -- type: MaterialProperties.fracture_forming_limit
        is_fractured_3 -- type: TestResults.is_fractured
    Output:
        fld_for_successful_tests_1 -- type: FLD.fld_for_successful_tests
    '''
    pass

    def generate_g_code(self,
        toolpath_code_1: str) -> str:
    '''
    Convert to G-code for the EMCO VMC-200 machining center and append program number, coordinates system, tool charge, etc.

    Arguments:
        toolpath_code_1 -- type: ToolPath.toolpath_code
    Output:
        g_code_1 -- type: NCProgram.g_code
    '''
    pass

    def prepare_specimen(self,
        thickness_1: float,
        hole_diameter_2: float,
        g_code_3: str) -> str:
    '''
    Show information about the specimen to be prepared and ask for confirmation.

    Arguments:
        thickness_1 -- type: BlankModel.thickness
        hole_diameter_2 -- type: BlankModel.hole_diameter
        g_code_3 -- type: NCProgram.g_code
    Output:
        is_prepared_1 -- type: Specimen.is_prepared
    '''
    pass

    def calculate_tool_path(self,
        thickness_1: float,
        diameter_2: float,
        flange_height_3: float,
        radius_4: float,
        feed_rate_5: float,
        step_down_6: float) -> str:
    '''
    Calculate the helical tool path (with tool radius compensation) to form the hole flange part along the flange height (consider also the sheet thickness)

    Arguments:
        thickness_1 -- type: BlankModel.thickness
        diameter_2 -- type: PartModel.diameter
        flange_height_3 -- type: PartModel.flange_height
        radius_4 -- type: FormingToolModel.radius
        feed_rate_5 -- type: FormingConditions.feed_rate
        step_down_6 -- type: FormingConditions.step_down
    Output:
        toolpath_code_1 -- type: ToolPath.toolpath_code
    '''
    pass

    

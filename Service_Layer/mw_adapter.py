#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

This file has been generated automatically.
'''

from Service_Layer.mw_data import *
from Service_Layer.mw_behaviour import MwBehaviour

class Adapter:
    def __init__(self, instance_name):
        self.instance_name = instance_name

    
    @staticmethod
    def fix_properties(instance_name):
        i = DataInstance(instance_name)
        i.load()


        thickness_1, diameter_2, feed_rate_3, step_down_4, fracture_forming_limit_5 = MwBehaviour.fix_properties(instance_name)

        i.blank_model.thickness = thickness_1
        i.save()
        i.part_model.diameter = diameter_2
        i.save()
        i.forming_conditions.feed_rate = feed_rate_3
        i.forming_conditions.step_down = step_down_4
        i.save()
        i.material_properties.fracture_forming_limit = fracture_forming_limit_5
        i.save()

        return thickness_1, diameter_2, feed_rate_3, step_down_4, fracture_forming_limit_5

        
    @staticmethod
    def plot_h_df(instance_name):
        i = DataInstance(instance_name)
        i.load()

        non_dimensional_flange_height_1 = i.test_results.non_dimensional_flange_height

        flange_height_diagram_1 = MwBehaviour.plot_h_df(instance_name, non_dimensional_flange_height_1)

        i.flangeability_diagrams.flange_height_diagram = flange_height_diagram_1
        i.save()

        return flange_height_diagram_1


    @staticmethod
    def plot_t_t0(instance_name):
        i = DataInstance(instance_name)
        i.load()

        non_dimensional_average_thickness_1 = i.test_results.non_dimensional_average_thickness

        average_thickness_diagram_1 = MwBehaviour.plot_t_t0(instance_name, non_dimensional_average_thickness_1)

        i.flangeability_diagrams.average_thickness_diagram = average_thickness_diagram_1
        i.save()

        return average_thickness_diagram_1

                
    @staticmethod
    def plot_global_fld(instance_name):
        i = DataInstance(instance_name)
        i.load()

        strain_distribution_1 = i.test_results.strain_distribution
        fracture_forming_limit_2 = i.material_properties.fracture_forming_limit

        overall_fld_1 = MwBehaviour.plot_global_fld(instance_name, strain_distribution_1, fracture_forming_limit_2)

        i.fld.overall_fld = overall_fld_1
        i.save()

        return overall_fld_1


    @staticmethod
    def plot_fld_per_tool(instance_name):
        i = DataInstance(instance_name)
        i.load()

        strain_distribution_1 = i.test_results.strain_distribution
        fracture_forming_limit_2 = i.material_properties.fracture_forming_limit
        radius_3 = i.forming_tool_model.radius

        fld_per_tool_1 = MwBehaviour.plot_fld_per_tool(instance_name, strain_distribution_1, fracture_forming_limit_2, radius_3)

        i.fld.fld_per_tool = fld_per_tool_1
        i.save()

        return fld_per_tool_1


    @staticmethod
    def plot_fld_for_successful_tests(instance_name):
        i = DataInstance(instance_name)
        i.load()

        strain_distribution_1 = i.test_results.strain_distribution
        fracture_forming_limit_2 = i.material_properties.fracture_forming_limit
        is_fractured_3 = i.test_results.is_fractured

        fld_for_successful_tests_1 = MwBehaviour.plot_fld_for_successful_tests(instance_name, strain_distribution_1, fracture_forming_limit_2, is_fractured_3)

        i.fld.fld_for_successful_tests = fld_for_successful_tests_1
        i.save()

        return fld_for_successful_tests_1


    @staticmethod
    def plot_fld_for_fractured_tests(instance_name):
        i = DataInstance(instance_name)
        i.load()

        strain_distribution_1 = i.test_results.strain_distribution
        fracture_forming_limit_2 = i.material_properties.fracture_forming_limit
        is_fractured_3 = i.test_results.is_fractured

        fld_for_fractured_tests_1 = MwBehaviour.plot_fld_for_fractured_tests(instance_name, strain_distribution_1, fracture_forming_limit_2, is_fractured_3)

        i.fld.fld_for_fractured_tests = fld_for_fractured_tests_1
        i.save()

        return fld_for_fractured_tests_1

    
    @staticmethod
    def calculate_flange_height(instance_name):
        i = DataInstance(instance_name)
        i.load()

        thickness_1 = i.blank_model.thickness
        hole_diameter_2 = i.blank_model.hole_diameter
        radius_3 = i.forming_tool_model.radius
        diameter_4 = i.part_model.diameter

        flange_height_1 = MwBehaviour.calculate_flange_height(instance_name, thickness_1, hole_diameter_2, radius_3, diameter_4)

        i.part_model.flange_height = flange_height_1
        i.save()

        return flange_height_1

    
    @staticmethod
    def calculate_tool_path(instance_name):
        i = DataInstance(instance_name)
        i.load()

        thickness_1 = i.blank_model.thickness
        diameter_2 = i.part_model.diameter
        flange_height_3 = i.part_model.flange_height
        radius_4 = i.forming_tool_model.radius
        feed_rate_5 = i.forming_conditions.feed_rate
        step_down_6 = i.forming_conditions.step_down

        toolpath_code_1 = MwBehaviour.calculate_tool_path(instance_name, thickness_1, diameter_2, flange_height_3, radius_4, feed_rate_5, step_down_6)

        i.tool_path.toolpath_code = toolpath_code_1
        i.save()

        return toolpath_code_1

    
    @staticmethod
    def check_for_specimen(instance_name):
        i = DataInstance(instance_name)
        i.load()

        thickness_1 = i.blank_model.thickness
        hole_diameter_2 = i.blank_model.hole_diameter
        g_code_3 = i.nc_program.g_code

        is_prepared_1 = MwBehaviour.check_for_specimen(instance_name, thickness_1, hole_diameter_2, g_code_3)

        i.specimen.is_prepared = is_prepared_1
        i.save()

        return is_prepared_1

    
    @staticmethod
    def ask_for_properties(instance_name):
        i = DataInstance(instance_name)
        i.load()


        hole_diameter_1, radius_2 = MwBehaviour.ask_for_properties(instance_name)

        i.blank_model.hole_diameter = hole_diameter_1
        i.save()
        i.forming_tool_model.radius = radius_2
        i.save()

        return hole_diameter_1, radius_2

            
    @staticmethod
    def calculate_hole_expansion_ratio(instance_name):
        i = DataInstance(instance_name)
        i.load()

        hole_diameter_1 = i.blank_model.hole_diameter
        diameter_2 = i.part_model.diameter
        is_fractured_3 = i.test_results.is_fractured

        hole_expansion_ratio_1 = MwBehaviour.calculate_hole_expansion_ratio(instance_name, hole_diameter_1, diameter_2, is_fractured_3)

        i.test_results.hole_expansion_ratio = hole_expansion_ratio_1
        i.save()

        return hole_expansion_ratio_1


    @staticmethod
    def calculate_non_dimensional_flange_height(instance_name):
        i = DataInstance(instance_name)
        i.load()

        diameter_1 = i.part_model.diameter
        is_fractured_2 = i.test_results.is_fractured
        flange_height_3 = i.test_results.flange_height

        non_dimensional_flange_height_1 = MwBehaviour.calculate_non_dimensional_flange_height(instance_name, diameter_1, is_fractured_2, flange_height_3)

        i.test_results.non_dimensional_flange_height = non_dimensional_flange_height_1
        i.save()

        return non_dimensional_flange_height_1


    @staticmethod
    def calculate_non_dimensional_average_thickness(instance_name):
        i = DataInstance(instance_name)
        i.load()

        hole_diameter_1 = i.blank_model.hole_diameter
        thickness_2 = i.blank_model.thickness
        diameter_3 = i.part_model.diameter
        is_fractured_4 = i.test_results.is_fractured
        flange_height_5 = i.test_results.flange_height

        non_dimensional_average_thickness_1 = MwBehaviour.calculate_non_dimensional_average_thickness(instance_name, hole_diameter_1, thickness_2, diameter_3, is_fractured_4, flange_height_5)

        i.test_results.non_dimensional_average_thickness = non_dimensional_average_thickness_1
        i.save()

        return non_dimensional_average_thickness_1

        
    @staticmethod
    def calculate_global_lfr(instance_name):
        i = DataInstance(instance_name)
        i.load()

        hole_expansion_ratio_1 = i.test_results.hole_expansion_ratio
        is_fractured_2 = i.test_results.is_fractured

        overall_lfr_1 = MwBehaviour.calculate_global_lfr(instance_name, hole_expansion_ratio_1, is_fractured_2)

        i.flangeability_parameters.overall_lfr = overall_lfr_1
        i.save()

        return overall_lfr_1


    @staticmethod
    def calculate_lfr_per_tool(instance_name):
        i = DataInstance(instance_name)
        i.load()

        hole_expansion_ratio_1 = i.test_results.hole_expansion_ratio
        is_fractured_2 = i.test_results.is_fractured
        radius_3 = i.forming_tool_model.radius

        lfr_per_tool_1 = MwBehaviour.calculate_lfr_per_tool(instance_name, hole_expansion_ratio_1, is_fractured_2, radius_3)

        i.flangeability_parameters.lfr_per_tool = lfr_per_tool_1
        i.save()

        return lfr_per_tool_1

    
    @staticmethod
    def check_for_fracture(instance_name):
        i = DataInstance(instance_name)
        i.load()

        is_prepared_1 = i.specimen.is_prepared
        g_code_2 = i.nc_program.g_code

        is_fractured_1 = MwBehaviour.check_for_fracture(instance_name, is_prepared_1, g_code_2)

        i.test_results.is_fractured = is_fractured_1
        i.save()

        return is_fractured_1

        
    @staticmethod
    def measure_flange_height(instance_name):
        i = DataInstance(instance_name)
        i.load()

        is_fractured_1 = i.test_results.is_fractured

        flange_height_1 = MwBehaviour.measure_flange_height(instance_name, is_fractured_1)

        i.test_results.flange_height = flange_height_1
        i.save()

        return flange_height_1


    @staticmethod
    def measure_strain_distribution(instance_name):
        i = DataInstance(instance_name)
        i.load()

        is_fractured_1 = i.test_results.is_fractured

        strain_distribution_1 = MwBehaviour.measure_strain_distribution(instance_name, is_fractured_1)

        i.test_results.strain_distribution = strain_distribution_1
        i.save()

        return strain_distribution_1

    
    @staticmethod
    def generate_g_code(instance_name):
        i = DataInstance(instance_name)
        i.load()

        toolpath_code_1 = i.tool_path.toolpath_code

        g_code_1 = MwBehaviour.generate_g_code(instance_name, toolpath_code_1)

        i.nc_program.g_code = g_code_1
        i.save()

        return g_code_1


    

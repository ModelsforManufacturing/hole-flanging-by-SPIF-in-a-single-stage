#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

This file has been generated automatically.
'''

from Service_Layer.behaviour import Behaviour
from Data_Layer.data import *

class MediatingController:
    def __init__(self, instance_name):
        self.instance_name = instance_name

            
    @staticmethod
    def calculate_non_dimensional_flange_height(instance_name):
        i = DataInstance(instance_name)
        i.load()

        is_fractured_1 = i.test_results.is_fractured
        flange_height_2 = i.test_results.flange_height
        diameter_3 = i.part_model.diameter

        non_dimensional_flange_height_1 = Behaviour.calculate_non_dimensional_flange_height(instance_name, is_fractured_1, flange_height_2, diameter_3)

        i.test_results.non_dimensional_flange_height = non_dimensional_flange_height_1
        i.save()

        return non_dimensional_flange_height_1


    @staticmethod
    def calculate_hole_expansion_ratio(instance_name):
        i = DataInstance(instance_name)
        i.load()

        is_fractured_1 = i.test_results.is_fractured
        diameter_2 = i.part_model.diameter
        hole_diameter_3 = i.blank_model.hole_diameter

        hole_expansion_ratio_1 = Behaviour.calculate_hole_expansion_ratio(instance_name, is_fractured_1, diameter_2, hole_diameter_3)

        i.test_results.hole_expansion_ratio = hole_expansion_ratio_1
        i.save()

        return hole_expansion_ratio_1


    @staticmethod
    def calculate_non_dimensional_average_thickness(instance_name):
        i = DataInstance(instance_name)
        i.load()

        is_fractured_1 = i.test_results.is_fractured
        flange_height_2 = i.test_results.flange_height
        hole_diameter_3 = i.blank_model.hole_diameter
        diameter_4 = i.part_model.diameter
        thickness_5 = i.blank_model.thickness

        non_dimensional_average_thickness_1 = Behaviour.calculate_non_dimensional_average_thickness(instance_name, is_fractured_1, flange_height_2, hole_diameter_3, diameter_4, thickness_5)

        i.test_results.non_dimensional_average_thickness = non_dimensional_average_thickness_1
        i.save()

        return non_dimensional_average_thickness_1

    
    @staticmethod
    def calculate_flange_height(instance_name):
        i = DataInstance(instance_name)
        i.load()

        thickness_1 = i.blank_model.thickness
        hole_diameter_2 = i.blank_model.hole_diameter
        diameter_3 = i.part_model.diameter
        radius_4 = i.forming_tool_model.radius

        flange_height_1 = Behaviour.calculate_flange_height(instance_name, thickness_1, hole_diameter_2, diameter_3, radius_4)

        i.part_model.flange_height = flange_height_1
        i.save()

        return flange_height_1

        
    @staticmethod
    def measure_strain_distribution(instance_name):
        i = DataInstance(instance_name)
        i.load()

        is_fractured_1 = i.test_results.is_fractured

        strain_distribution_1 = Behaviour.measure_strain_distribution(instance_name, is_fractured_1)

        i.test_results.strain_distribution = strain_distribution_1
        i.save()

        return strain_distribution_1


    @staticmethod
    def measure_flange_height(instance_name):
        i = DataInstance(instance_name)
        i.load()

        is_fractured_1 = i.test_results.is_fractured

        flange_height_1 = Behaviour.measure_flange_height(instance_name, is_fractured_1)

        i.test_results.flange_height = flange_height_1
        i.save()

        return flange_height_1

        
    @staticmethod
    def calculate_lfr_per_tool(instance_name):
        i = DataInstance(instance_name)
        i.load()

        radius_1 = i.forming_tool_model.radius
        hole_expansion_ratio_2 = i.test_results.hole_expansion_ratio
        is_fractured_3 = i.test_results.is_fractured

        lfr_per_tool_1 = Behaviour.calculate_lfr_per_tool(instance_name, radius_1, hole_expansion_ratio_2, is_fractured_3)

        i.lfr.lfr_per_tool = lfr_per_tool_1
        i.save()

        return lfr_per_tool_1


    @staticmethod
    def calculate_global_lfr(instance_name):
        i = DataInstance(instance_name)
        i.load()

        hole_expansion_ratio_1 = i.test_results.hole_expansion_ratio
        is_fractured_2 = i.test_results.is_fractured

        global_lfr_1 = Behaviour.calculate_global_lfr(instance_name, hole_expansion_ratio_1, is_fractured_2)

        i.lfr.global_lfr = global_lfr_1
        i.save()

        return global_lfr_1

        
    @staticmethod
    def plot_t_t0(instance_name):
        i = DataInstance(instance_name)
        i.load()

        non_dimensional_average_thickness_1 = i.test_results.non_dimensional_average_thickness

        average_thickness_diagram_1 = Behaviour.plot_t_t0(instance_name, non_dimensional_average_thickness_1)

        i.technological_parameters.average_thickness_diagram = average_thickness_diagram_1
        i.save()

        return average_thickness_diagram_1


    @staticmethod
    def plot_h_df(instance_name):
        i = DataInstance(instance_name)
        i.load()

        non_dimensional_flange_height_1 = i.test_results.non_dimensional_flange_height

        flange_height_diagram_1 = Behaviour.plot_h_df(instance_name, non_dimensional_flange_height_1)

        i.technological_parameters.flange_height_diagram = flange_height_diagram_1
        i.save()

        return flange_height_diagram_1

                
    @staticmethod
    def conclusions_for_height(instance_name):
        i = DataInstance(instance_name)
        i.load()

        flange_height_diagram_1 = i.technological_parameters.flange_height_diagram

        flange_height_1 = Behaviour.conclusions_for_height(instance_name, flange_height_diagram_1)

        i.conclusions.flange_height = flange_height_1
        i.save()

        return flange_height_1


    @staticmethod
    def conclusions_for_t0_r(instance_name):
        i = DataInstance(instance_name)
        i.load()

        average_thickness_diagram_1 = i.technological_parameters.average_thickness_diagram
        flange_height_diagram_2 = i.technological_parameters.flange_height_diagram
        global_fld_3 = i.fld.global_fld
        fld_per_tool_4 = i.fld.fld_per_tool
        fld_for_successful_tests_5 = i.fld.fld_for_successful_tests
        fld_for_fractured_tests_6 = i.fld.fld_for_fractured_tests
        global_lfr_7 = i.lfr.global_lfr
        lfr_per_tool_8 = i.lfr.lfr_per_tool

        bending_ratio_1 = Behaviour.conclusions_for_t0_r(instance_name, average_thickness_diagram_1, flange_height_diagram_2, global_fld_3, fld_per_tool_4, fld_for_successful_tests_5, fld_for_fractured_tests_6, global_lfr_7, lfr_per_tool_8)

        i.conclusions.bending_ratio = bending_ratio_1
        i.save()

        return bending_ratio_1


    @staticmethod
    def conclusions_for_lfr(instance_name):
        i = DataInstance(instance_name)
        i.load()

        global_lfr_1 = i.lfr.global_lfr
        lfr_per_tool_2 = i.lfr.lfr_per_tool

        limit_forming_ratio_1 = Behaviour.conclusions_for_lfr(instance_name, global_lfr_1, lfr_per_tool_2)

        i.conclusions.limit_forming_ratio = limit_forming_ratio_1
        i.save()

        return limit_forming_ratio_1


    @staticmethod
    def conclusions_for_thickness(instance_name):
        i = DataInstance(instance_name)
        i.load()

        average_thickness_diagram_1 = i.technological_parameters.average_thickness_diagram

        average_thickness_1 = Behaviour.conclusions_for_thickness(instance_name, average_thickness_diagram_1)

        i.conclusions.average_thickness = average_thickness_1
        i.save()

        return average_thickness_1

    
    @staticmethod
    def perform_hole_flanging_test(instance_name):
        i = DataInstance(instance_name)
        i.load()

        g_code_1 = i.nc_program.g_code
        is_prepared_2 = i.specimen.is_prepared

        is_fractured_1 = Behaviour.perform_hole_flanging_test(instance_name, g_code_1, is_prepared_2)

        i.test_results.is_fractured = is_fractured_1
        i.save()

        return is_fractured_1

                
    @staticmethod
    def plot_fld_per_tool(instance_name):
        i = DataInstance(instance_name)
        i.load()

        strain_distribution_1 = i.test_results.strain_distribution
        fracture_forming_limit_2 = i.material_properties.fracture_forming_limit
        radius_3 = i.forming_tool_model.radius

        fld_per_tool_1 = Behaviour.plot_fld_per_tool(instance_name, strain_distribution_1, fracture_forming_limit_2, radius_3)

        i.fld.fld_per_tool = fld_per_tool_1
        i.save()

        return fld_per_tool_1


    @staticmethod
    def plot_fld_for_fractured_tests(instance_name):
        i = DataInstance(instance_name)
        i.load()

        strain_distribution_1 = i.test_results.strain_distribution
        fracture_forming_limit_2 = i.material_properties.fracture_forming_limit
        is_fractured_3 = i.test_results.is_fractured

        fld_for_fractured_tests_1 = Behaviour.plot_fld_for_fractured_tests(instance_name, strain_distribution_1, fracture_forming_limit_2, is_fractured_3)

        i.fld.fld_for_fractured_tests = fld_for_fractured_tests_1
        i.save()

        return fld_for_fractured_tests_1


    @staticmethod
    def plot_global_fld(instance_name):
        i = DataInstance(instance_name)
        i.load()

        strain_distribution_1 = i.test_results.strain_distribution
        fracture_forming_limit_2 = i.material_properties.fracture_forming_limit

        global_fld_1 = Behaviour.plot_global_fld(instance_name, strain_distribution_1, fracture_forming_limit_2)

        i.fld.global_fld = global_fld_1
        i.save()

        return global_fld_1


    @staticmethod
    def plot_fld_for_successful_tests(instance_name):
        i = DataInstance(instance_name)
        i.load()

        strain_distribution_1 = i.test_results.strain_distribution
        fracture_forming_limit_2 = i.material_properties.fracture_forming_limit
        is_fractured_3 = i.test_results.is_fractured

        fld_for_successful_tests_1 = Behaviour.plot_fld_for_successful_tests(instance_name, strain_distribution_1, fracture_forming_limit_2, is_fractured_3)

        i.fld.fld_for_successful_tests = fld_for_successful_tests_1
        i.save()

        return fld_for_successful_tests_1

    
    @staticmethod
    def generate_g_code(instance_name):
        i = DataInstance(instance_name)
        i.load()

        toolpath_code_1 = i.tool_path.toolpath_code

        g_code_1 = Behaviour.generate_g_code(instance_name, toolpath_code_1)

        i.nc_program.g_code = g_code_1
        i.save()

        return g_code_1

    
    @staticmethod
    def prepare_specimen(instance_name):
        i = DataInstance(instance_name)
        i.load()

        thickness_1 = i.blank_model.thickness
        hole_diameter_2 = i.blank_model.hole_diameter
        g_code_3 = i.nc_program.g_code

        is_prepared_1 = Behaviour.prepare_specimen(instance_name, thickness_1, hole_diameter_2, g_code_3)

        i.specimen.is_prepared = is_prepared_1
        i.save()

        return is_prepared_1

    
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

        toolpath_code_1 = Behaviour.calculate_tool_path(instance_name, thickness_1, diameter_2, flange_height_3, radius_4, feed_rate_5, step_down_6)

        i.tool_path.toolpath_code = toolpath_code_1
        i.save()

        return toolpath_code_1


    

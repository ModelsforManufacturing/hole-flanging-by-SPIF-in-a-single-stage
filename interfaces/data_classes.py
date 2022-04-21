#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

Definition of Objects (as classes) and its Paramenters for the Data Model.

This file has been generated automatically.
'''

class BlankModel:
    ''' Description: TODO '''
    def __init__(self, thickness, hole_diameter):
        '''
        Keyword arguments:
        thickness -- (float) Units: mm. Initial sheet thickness.
        hole_diameter -- (float) Units: mm. Diameter of the hole to be cut to the blank sheet.

        '''
        self.thickness = thickness
        self.hole_diameter = hole_diameter


class PartModel:
    ''' Description: TODO '''
    def __init__(self, diameter, flange_height):
        '''
        Keyword arguments:
        diameter -- (float) Units: mm. Inner diameter of the hole-flanged part to be manufactured.
        flange_height -- (float) Units: mm. Theoretical flange height measured from the external flat surface.

        '''
        self.diameter = diameter
        self.flange_height = flange_height


class FormingToolModel:
    ''' Description: TODO '''
    def __init__(self, radius):
        '''
        Keyword arguments:
        radius -- (float) Units: mm. Forming tool radius.

        '''
        self.radius = radius


class ToolPath:
    ''' Description: TODO '''
    def __init__(self, toolpath_code):
        '''
        Keyword arguments:
        toolpath_code -- (string) It can be APT, G-code, etc. It must contain the tool path coordinates, tool feed rate and step down.

        '''
        self.toolpath_code = toolpath_code


class FormingConditions:
    ''' Description: TODO '''
    def __init__(self, feed_rate, step_down):
        '''
        Keyword arguments:
        feed_rate -- (float) Units: mm/min. Feed rate of the forming tool.
        step_down -- (float) Units: mm. Step down of the forming tool following an helical tool path.

        '''
        self.feed_rate = feed_rate
        self.step_down = step_down


class NcProgram:
    ''' Description: TODO '''
    def __init__(self, g_code):
        '''
        Keyword arguments:
        g_code -- (string) 

        '''
        self.g_code = g_code


class Specimen:
    ''' Description: TODO '''
    def __init__(self, is_prepared):
        '''
        Keyword arguments:
        is_prepared -- (string) 

        '''
        self.is_prepared = is_prepared


class TestResults:
    ''' Description: TODO '''
    def __init__(self, is_fractured, flange_height, strain_distribution, hole_expansion_ratio, non_dimensional_flange_height, non_dimensional_average_thickness):
        '''
        Keyword arguments:
        is_fractured -- (string) 
        flange_height -- (float) Units: mm. Flange height of the produced part measured from the external flat surface.
        strain_distribution -- (string) 
        hole_expansion_ratio -- (float) Units: non-dimensional. Initial to final diameter ratio, d0/df.
        non_dimensional_flange_height -- (float) Units: non-dimensional. Flange height to final diameter ratio, h/df.
        non_dimensional_average_thickness -- (float) Units: non-dimensional. Average thickness along the flange to initial thickness ratio, t/t0.

        '''
        self.is_fractured = is_fractured
        self.flange_height = flange_height
        self.strain_distribution = strain_distribution
        self.hole_expansion_ratio = hole_expansion_ratio
        self.non_dimensional_flange_height = non_dimensional_flange_height
        self.non_dimensional_average_thickness = non_dimensional_average_thickness


class MaterialProperties:
    ''' Description: TODO '''
    def __init__(self, fracture_forming_limit):
        '''
        Keyword arguments:
        fracture_forming_limit -- (string) Table with pairs of major and minor strain values

        '''
        self.fracture_forming_limit = fracture_forming_limit


class AnalysisResults:
    ''' Description: TODO '''
    def __init__(self, ):
        '''
        Keyword arguments:

        '''


class Lfr:
    ''' Description: TODO '''
    def __init__(self, global_lfr, lfr_per_tool):
        '''
        Keyword arguments:
        global_lfr -- (float) Units: non-dimensional. Limit forming ratio from all experimental tests.
        lfr_per_tool -- (float) Units: non-dimensional. Limit forming ratio from experimental tests using the same forming tool.

        '''
        self.global_lfr = global_lfr
        self.lfr_per_tool = lfr_per_tool


class Fld:
    ''' Description: TODO '''
    def __init__(self, global_fld, fld_per_tool, fld_for_successful_tests, fld_for_fractured_tests):
        '''
        Keyword arguments:
        global_fld -- (string) Name of image file. FLD includes FFL curve and strain distribution for all tests.
        fld_per_tool -- (string) 
        fld_for_successful_tests -- (string) 
        fld_for_fractured_tests -- (string) 

        '''
        self.global_fld = global_fld
        self.fld_per_tool = fld_per_tool
        self.fld_for_successful_tests = fld_for_successful_tests
        self.fld_for_fractured_tests = fld_for_fractured_tests


class TechnologicalParameters:
    ''' Description: TODO '''
    def __init__(self, flange_height_diagram, average_thickness_diagram):
        '''
        Keyword arguments:
        flange_height_diagram -- (string) 
        average_thickness_diagram -- (string) 

        '''
        self.flange_height_diagram = flange_height_diagram
        self.average_thickness_diagram = average_thickness_diagram


class Conclusions:
    ''' Description: TODO '''
    def __init__(self, limit_forming_ratio, flange_height, average_thickness, bending_ratio):
        '''
        Keyword arguments:
        limit_forming_ratio -- (string) 
        flange_height -- (string) 
        average_thickness -- (string) 
        bending_ratio -- (string) 

        '''
        self.limit_forming_ratio = limit_forming_ratio
        self.flange_height = flange_height
        self.average_thickness = average_thickness
        self.bending_ratio = bending_ratio




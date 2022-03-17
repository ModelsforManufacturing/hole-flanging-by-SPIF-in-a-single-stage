#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

Definition of Objects (as classes) and its Paramenters for the Data Model.

This file has been generated automatically.
'''

class BlankSheet:
    ''' Description: TODO '''
    def __init__(self, hole_diameter):
        '''
        Keyword arguments:
        hole_diameter -- (float) Units: mm. Diameter of the hole cut to the blank sheet.

        '''
        self.hole_diameter = hole_diameter


class RawMaterial:
    ''' Description: TODO '''
    def __init__(self, thickness):
        '''
        Keyword arguments:
        thickness -- (float) Units: mm. 

        '''
        self.thickness = thickness


class DesignPart:
    ''' Description: TODO '''
    def __init__(self, diameter, height, part_3d):
        '''
        Keyword arguments:
        diameter -- (float) Units: mm. Diameter of the hole-flanged part measured in the inner surface.
        height -- (float) Units: mm. Flange height measured from the external flat surface.
        part_3d -- (string) Pathname of the file containing the 3D part model to be updated with ‘diameter’ and ‘height’ parameters.

        '''
        self.diameter = diameter
        self.height = height
        self.part_3d = part_3d


class FormingTool:
    ''' Description: TODO '''
    def __init__(self, radius):
        '''
        Keyword arguments:
        radius -- (float) Units: mm. 

        '''
        self.radius = radius


class ElasticBehaviour:
    ''' Description: TODO '''
    def __init__(self, elasticity_modulus, poisson_ratio):
        '''
        Keyword arguments:
        elasticity_modulus -- (float) Units: GPa. 
        poisson_ratio -- (float) Units: adimensional. 

        '''
        self.elasticity_modulus = elasticity_modulus
        self.poisson_ratio = poisson_ratio


class PlasticBehaviour:
    ''' Description: TODO '''
    def __init__(self, strain_stress_curve, anisotropy_coefficients):
        '''
        Keyword arguments:
        strain_stress_curve -- (string) 
        anisotropy_coefficients -- (string) 

        '''
        self.strain_stress_curve = strain_stress_curve
        self.anisotropy_coefficients = anisotropy_coefficients


class FractureBehaviour:
    ''' Description: TODO '''
    def __init__(self, fracture_curve):
        '''
        Keyword arguments:
        fracture_curve -- (string) 

        '''
        self.fracture_curve = fracture_curve


class Strategy:
    ''' Description: TODO '''
    def __init__(self, step_down, feedrate):
        '''
        Keyword arguments:
        step_down -- (float) Units: mm. 
        feedrate -- (float) Units: mm/min. 

        '''
        self.step_down = step_down
        self.feedrate = feedrate


class NcProgram:
    ''' Description: TODO '''
    def __init__(self, apt_code):
        '''
        Keyword arguments:
        apt_code -- (string) 

        '''
        self.apt_code = apt_code


class NcModel:
    ''' Description: TODO '''
    def __init__(self, process_3d):
        '''
        Keyword arguments:
        process_3d -- (string) 

        '''
        self.process_3d = process_3d


class ToolTrajectory:
    ''' Description: TODO '''
    def __init__(self, toolpath_code):
        '''
        Keyword arguments:
        toolpath_code -- (string) 

        '''
        self.toolpath_code = toolpath_code


class SimulationModel:
    ''' Description: TODO '''
    def __init__(self, analysis_model):
        '''
        Keyword arguments:
        analysis_model -- (string) 

        '''
        self.analysis_model = analysis_model


class SimulationResults:
    ''' Description: TODO '''
    def __init__(self, analysis_output):
        '''
        Keyword arguments:
        analysis_output -- (string) 

        '''
        self.analysis_output = analysis_output


class SimulatedPart:
    ''' Description: TODO '''
    def __init__(self, strain_distribution, fracture_location):
        '''
        Keyword arguments:
        strain_distribution -- (string) 
        fracture_location -- (string) 

        '''
        self.strain_distribution = strain_distribution
        self.fracture_location = fracture_location


class SimulationIssues:
    ''' Description: TODO '''
    def __init__(self, flange_height):
        '''
        Keyword arguments:
        flange_height -- (float) Units: mm. 

        '''
        self.flange_height = flange_height


class ManufacturedPart:
    ''' Description: TODO '''
    def __init__(self, failed, fracture_location, height, diameter, photos):
        '''
        Keyword arguments:
        failed -- (string) 
        fracture_location -- (string) 
        height -- (float) Units: mm. 
        diameter -- (float) Units: mm. 
        photos -- (string) 

        '''
        self.failed = failed
        self.fracture_location = fracture_location
        self.height = height
        self.diameter = diameter
        self.photos = photos


class AnalyzedPart:
    ''' Description: TODO '''
    def __init__(self, strain_distribution, thickness_profile, fractographies):
        '''
        Keyword arguments:
        strain_distribution -- (string) 
        thickness_profile -- (string) 
        fractographies -- (string) 

        '''
        self.strain_distribution = strain_distribution
        self.thickness_profile = thickness_profile
        self.fractographies = fractographies


class ManufacturingIssues:
    ''' Description: TODO '''
    def __init__(self, flange_height):
        '''
        Keyword arguments:
        flange_height -- (float) Units: mm. 

        '''
        self.flange_height = flange_height




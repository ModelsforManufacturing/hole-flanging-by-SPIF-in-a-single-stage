#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

Functions to retrieve/save data from/t0 the Data Layer.
"""

import configparser # Configuration file parser
import shutil       # High-level file operations
import datetime     # Basic date and time types


''' SPIF Design Model '''

class BlankSheet:
    '''
    '''
    def __init__(self, hole_diameter):
        '''
        Creates a BlankSheet object.
        
        Keyword arguments:
        hole_diameter -- float
        '''
        self.hole_diameter = hole_diameter

class RawMaterial:
    '''
    '''
    def __init__(self, thickness):
        '''
        Creates a RawMaterial object.
        
        Keyword arguments:
        thickness -- float
        '''
        self.thickness = thickness

class DesignPart:
    '''
    '''
    def __init__(self, diameter, height, part3d):
        '''
        Creates a DesignPart object.
        
        Keyword arguments:
        diameter -- float
        height -- float
        part3d -- string
        '''
        self.diameter = diameter
        self.height = height
        self.part3d = part3d

class FormingTool:
    '''
    '''
    def __init__(self, radius):
        '''
        Creates a FormingTool object.
        
        Keyword arguments:
        radius -- float
        '''
        self.radius = radius

class ElasticBehaviour:
    '''
    '''
    def __init__(self, elasticity_modulus, poisson_ratio):
        '''
        Creates a ElasticBehaviour object.
        
        Keyword arguments:
        elasticity_modulus -- float
        poisson_ratio -- float
        '''
        self.elasticity_modulus = elasticity_modulus
        self.poisson_ratio = poisson_ratio

class PlasticBehaviour:
    '''
    '''
    def __init__(self, strain_stress_curve, anisotropy_coefficients):
        '''
        Creates a PlasticBehaviour object.
        
        Keyword arguments:
        strain_stress_curve -- string
        anisotropy_coefficients -- string
        '''
        self.strain_stress_curve = strain_stress_curve
        self.anisotropy_coefficients = anisotropy_coefficients

class FractureBehaviour:
    '''
    '''
    def __init__(self, fracture_curve):
        '''
        Creates a FractureBehaviour object.
        
        Keyword arguments:
        fracture_curve -- float
        '''
        self.fracture_curve = fracture_curve



''' SPIF CNC Model '''

class Strategy:
    '''
    '''
    def __init__(self, stepdown, feedrate):
        '''
        Creates a Strategy object.
        
        Keyword arguments:
        stepdown -- float
        feedrate -- float
        '''
        self.stepdown = stepdown
        self.feedrate = feedrate

class NCModel:
    '''
    '''
    def __init__(self, process3d):
        '''
        Creates a NCModel object.
        
        Keyword arguments:
        process3d -- string
        '''
        self.process3d = process3d

class NCProgram:
    '''
    '''
    def __init__(self, apt_code):
        '''
        Creates a NCProgram object.
        
        Keyword arguments:
        apt_code -- string
        '''
        self.apt_code = apt_code




''' SPIF Simulation Model '''

class ToolTrajectory:
    '''
    '''
    def __init__(self, toolpath_code):
        '''
        Creates a ToolTrajectory object.
        
        Keyword arguments:
        toolpath_code -- string
        '''
        self.toolpath_code = toolpath_code

class SimulationModel:
    '''
    '''
    def __init__(self, analysis3d_model):
        '''
        Creates a SimulationModel object.
        
        Keyword arguments:
        analysis3d_model -- string
        '''
        self.analysis3d_model = analysis3d_model

class SimulationResults:
    '''
    '''
    def __init__(self, analysis3d_output):
        '''
        Creates a SimulationResults object.
        
        Keyword arguments:
        analysis3d_output -- string
        '''
        self.analysis3d_output = analysis3d_output

class SimulatedPart:
    '''
    '''
    def __init__(self, strain_distribution, fracture_location):
        '''
        Creates a SimulatedPart object.
        
        Keyword arguments:
        strain_distribution -- string
        fracture_location -- string
        '''
        self.strain_distribution = strain_distribution
        self.fracture_location = fracture_location

class SimulationIssues:
    '''
    '''
    def __init__(self, flange_height):
        '''
        Creates a SimulationIssues object.
        
        Keyword arguments:
        flange_height -- float
        '''
        self.flange_height = flange_height




''' SPIF Manufacturing Model '''

class ManufacturedPart:
    '''
    '''
    def __init__(self, failed, fracture_location, height, diameter, photos):
        '''
        Creates a ManufacturedPart object.
        
        Keyword arguments:
        failed -- string
        fracture_location -- string
        height -- float
        diameter -- float
        photos -- string
        '''
        self.failed = failed
        self.fracture_location = fracture_location
        self.height = height
        self.diameter = diameter
        self.photos = photos

class AnalyzedPart:
    '''
    '''
    def __init__(self, strain_distribution, thickness_profile, fractographies):
        '''
        Creates a AnalyzedPart object.
        
        Keyword arguments:
        strain_distribution -- string
        thickness_profile -- string
        fractographies -- string
        '''
        self.strain_distribution = strain_distribution
        self.thickness_profile = thickness_profile
        self.fractographies = fractographies

class ManufacturingIssues:
    '''
    '''
    def __init__(self, flange_height):
        '''
        Creates a ManufacturingIssues object.
        
        Keyword arguments:
        flange_height -- float
        '''
        self.flange_height = flange_height



''' Instance '''

class Instance:
    '''
    '''
    def __init__(self, instance_name):
        '''
        Creates a Instance object from `data.ini`.
        
        Keyword arguments:
        instance_name -- string
        '''
        self.instance_name = instance_name

        datafile = 'Data_Layer/%s/data.ini' % instance_name
#        datafile = '%s/data.ini' % instance_name
        self.datafile = datafile
        
        parser = configparser.ConfigParser()
        parser.read(datafile)
        blank_d = float(parser.get('Blank Sheet', 'hole diameter'))
        blank_t = float(parser.get('Raw Material', 'thickness'))
        part_d = float(parser.get('Design Part', 'diameter'))
        part_h = float(parser.get('Design Part', 'height'))
        part_3d = parser.get('Design Part', '3d part')        
        tool_r = float(parser.get('Forming Tool', 'radius'))
        elastic_E = parser.get('Elastic behaviour', 'elasticity modulus')
        elastic_nu = parser.get('Elastic behaviour', 'poisson ratio')
        plastic = parser.get('Plastic behaviour', 'strain-stress curve')
        anisotr = parser.get('Plastic behaviour', 'anisotropy coefficients')
        fracture = parser.get('Fracture behaviour', 'fracture curve')
        stepdown = float(parser.get('Strategy', 'step down'))
        feedrate = float(parser.get('Strategy', 'feedrate'))
        process_3d = parser.get('NC Model', '3d process')
        apt = parser.get('NC Program', 'apt code')
        toolpath = parser.get('Tool Trajectory', 'toolpath code')
        analysis = parser.get('Simulation Model', '3d analysis model')
        sim_results = parser.get('Simulation Results', '3d analysis output')
        sim_strain = parser.get('Simulated Part', 'strain distribution')
        sim_fract = parser.get('Simulated Part', 'fracture location')
        issues_h = float(parser.get('Simulation Issues', 'flange height'))
        manuf_fail = parser.get('Manufactured Part', 'failed')
        manuf_fract = parser.get('Manufactured Part', 'fracture location')
        manuf_h = float(parser.get('Manufactured Part', 'height'))
        manuf_d = float(parser.get('Manufactured Part', 'diameter'))
        manuf_photos = parser.get('Manufactured Part', 'photos')
        analyze_strain = parser.get('Analyzed Part', 'strain distribution')
        analyze_t = parser.get('Analyzed Part', 'thickness profile')
        analyze_fractogr = parser.get('Analyzed Part', 'fractographies')
        manuf_issues_h = float(parser.get('Mahufacturing Issues', 'flange height'))

        self.blank_sheet = BlankSheet(blank_d)
        self.raw_material = RawMaterial(blank_t)
        self.design_part = DesignPart(part_d, part_h, part_3d)
        self.forming_tool = FormingTool(tool_r)
        self.elastic_behaviour = ElasticBehaviour(elastic_E, elastic_nu)
        self.plastic_behaviour = PlasticBehaviour(plastic, anisotr)
        self.fracture_behaviour = FractureBehaviour(fracture)
        self.strategy = Strategy(stepdown, feedrate)
        self.nc_model = NCModel(process_3d)
        self.nc_program = NCProgram(apt)
        self.trajectory = ToolTrajectory(toolpath)
        self.simulation_model = SimulationModel(analysis)
        self.simulation_results = SimulationResults(sim_results)
        self.simulated_part = SimulatedPart(sim_strain, sim_fract)
        self.simulation_issues = SimulationIssues(issues_h)
        self.manufactured_part = ManufacturedPart(manuf_fail, manuf_fract, manuf_h, manuf_d, manuf_photos)
        self.analyzed_part = AnalyzedPart(analyze_strain, analyze_t, analyze_fractogr)
        self.manufacturing_issues = ManufacturingIssues(manuf_issues_h)

    def save(self):
        '''
        Make a backup copy of `data.ini` before saving the data.
        '''
        # Backup of 'data.ini'
        date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        datafile_backup = 'Data_Layer/%s/data_%s.ini' % (self.instance_name, date)
#        datafile_backup = '%s/data_%s.ini' % (self.instance_name, date)
        shutil.copyfile(self.datafile, datafile_backup)

        parser = configparser.ConfigParser()
        parser.add_section('Blank Sheet')
        parser.set('Blank Sheet', 'hole diameter', '%s' % self.blank_sheet.hole_diameter)
        parser.add_section('Raw Material')
        parser.set('Raw Material', 'thickness', '%s' % self.raw_material.thickness)
        parser.add_section('Design Part')
        parser.set('Design Part', 'diameter', '%s' % self.design_part.diameter)
        parser.set('Design Part', 'height', '%s' % self.design_part.height)
        parser.set('Design Part', '3d part', '%s' % self.design_part.part3d)
        parser.add_section('Forming Tool')
        parser.set('Forming Tool', 'radius', '%s' % self.forming_tool.radius)
        parser.add_section('Elastic behaviour')
        parser.set('Elastic behaviour', 'elasticity modulus', '%s' % self.elastic_behaviour.elasticity_modulus)
        parser.set('Elastic behaviour', 'poisson ratio', '%s' % self.elastic_behaviour.poisson_ratio)
        parser.add_section('Plastic behaviour')
        parser.set('Plastic behaviour', 'strain-stress curve', '%s' % self.plastic_behaviour.strain_stress_curve)
        parser.set('Plastic behaviour', 'anisotropy coefficients', '%s' % self.plastic_behaviour.anisotropy_coefficients)
        parser.add_section('Fracture behaviour')
        parser.set('Fracture behaviour', 'fracture curve', '%s' % self.fracture_behaviour.fracture_curve)
        parser.add_section('Strategy')
        parser.set('Strategy', 'step down', '%s' % self.strategy.stepdown)
        parser.set('Strategy', 'feedrate', '%s' % self.strategy.feedrate)
        
        parser.add_section('NC Model')
        parser.set('NC Model', '3d process', '%s' % self.nc_model.process3d)
        parser.add_section('NC Program')
        parser.set('NC Program', 'apt code', '%s' % self.nc_program.apt_code)
        parser.add_section('Tool Trajectory')
        parser.set('Tool Trajectory', 'toolpath code', '%s' % self.trajectory.toolpath_code)
        parser.add_section('Simulation Model')
        parser.set('Simulation Model', '3d analysis model', '%s' % self.simulation_model.analysis3d_model)
        parser.add_section('Simulation Results')
        parser.set('Simulation Results', '3d analysis output', '%s' % self.simulation_results.analysis3d_output)
        parser.add_section('Simulated Part')
        parser.set('Simulated Part', 'strain distribution', '%s' % self.simulated_part.strain_distribution)
        parser.set('Simulated Part', 'fracture location', '%s' % self.simulated_part.fracture_location)
        parser.add_section('Simulation Issues')
        parser.set('Simulation Issues', 'flange height', '%s' % self.simulation_issues.flange_height)
        parser.add_section('Manufactured Part')
        parser.set('Manufactured Part', 'failed', '%s' % self.manufactured_part.failed)
        parser.set('Manufactured Part', 'fracture location', '%s' % self.manufactured_part.fracture_location)
        parser.set('Manufactured Part', 'height', '%s' % self.manufactured_part.height)
        parser.set('Manufactured Part', 'diameter', '%s' % self.manufactured_part.diameter)
        parser.set('Manufactured Part', 'photos', '%s' % self.manufactured_part.photos)
        parser.add_section('Analyzed Part')
        parser.set('Analyzed Part', 'strain distribution', '%s' % self.analyzed_part.strain_distribution)
        parser.set('Analyzed Part', 'thickness profile', '%s' % self.analyzed_part.thickness_profile)
        parser.set('Analyzed Part', 'fractographies', '%s' % self.analyzed_part.fractographies)
        parser.add_section('Mahufacturing Issues')
        parser.set('Mahufacturing Issues', 'flange height', '%s' % self.manufacturing_issues.flange_height)

        with open(self.datafile, 'w') as configfile:
            parser.write(configfile)
    

    
if __name__ == '__main__':

    i = Instance('instance01')
    i.design_part.diameter = 100
    i.design_part.part3d = 'hole_flanged_part.CATPart'
    i.elastic_behaviour.elasticity_modulus = 70000
    i.save()
    

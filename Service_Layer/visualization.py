#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

"""

import os
from tabulate import tabulate

from Data_Layer.data import *

class Visualization:
        
    @staticmethod
    def find_instances():
        data_layer = 'Data_Layer/'
        instances = []
        for root, dirs, files in os.walk(data_layer):
            for name in files:
                if name == 'data.ini':
                    instance = root.split(data_layer)[1]
                    instances.append(instance)
#        print(instances)
        return instances

    @staticmethod
    def print_instances():
        instances = Visualization.find_instances()
        data = []
        for instance_name in instances:
            i = DataInstance(instance_name)
            i.load()
            t0 = i.blank_model.thickness
            d0 = i.blank_model.hole_diameter
            R = i.forming_tool_model.radius
            f = i.forming_conditions.feed_rate
            sd = i.forming_conditions.step_down
            prep = i.specimen.is_prepared
            fract = i.test_results.is_fractured
            strain = i.test_results.strain_distribution
            her = round(i.test_results.hole_expansion_ratio, 2)
            lfr = round(i.lfr.global_lfr, 2)
            if her==0:
                her=''
            h_df = round(i.test_results.non_dimensional_flange_height, 2)
            if h_df==0:
                h_df=''
            t_t0 = round(i.test_results.non_dimensional_average_thickness, 2)
            if t_t0==0:
                t_t0=''
            next_action = Visualization._get_next_action(instance_name)
            if next_action==8:
                next_action='Completed'
            data.append([instance_name, d0, R, f, sd, prep, fract, her, h_df, t_t0, strain, lfr, next_action])
#            print('%s: d0 = %.1f mm, R = %d mm' % (instance_name, d0, R))
        print(tabulate(data, headers=['Instance', 'd0\nmm', 'R\nmm', 'Feedrate\nmm/min', 'Step down\nmm', 
            'Specimen', 'Fracture', 'HER', 'h/df', 't/t0', 'Strain\ndistrib.', 'LFR',
            'Next\naction']))

    @staticmethod
    def _get_next_action(instance_name):
        data_layer = 'Data_Layer/'
        if not os.path.isdir(data_layer + instance_name):
            print('Instance not found.')
            return 0
        try:
            i = DataInstance(instance_name)
            i.load()
            g_code = i.nc_program.g_code
            if g_code == '':
                return 1

            is_prepared = i.specimen.is_prepared
            if not is_prepared in ['yes', 'y']:
                return 2
            
            is_fractured = i.test_results.is_fractured
            if not is_fractured in ['yes', 'y', 'no', 'n']:
                return 3

            fh = i.test_results.flange_height
            if is_fractured in ['no', 'n']:
                if not fh > 0:
                    return 4

            strain = i.test_results.strain_distribution
            if is_fractured in ['yes', 'y', 'no', 'n']:
                if strain == '':
                    return 5

            her = i.test_results.hole_expansion_ratio
            if is_fractured in ['no', 'n']:
                if not her > 0:
                    return 6

            c_lfr = i.conclusions.limit_forming_ratio
            if c_lfr == '':
                return 7
            else:
                return 8
        except Exception as e:
            print('***** Exception found:')
            print(e)

    """
    @staticmethod
    def print_status(instance_name):
        print('')
        print('Status of instance "%s":' % instance_name)
        data_layer = 'Data_Layer/'
        if not os.path.isdir(data_layer + instance_name):
            print('Instance not found.')
            return 0
        try:
            i = DataInstance(instance_name)
            i.load()
            t0 = i.blank_model.thickness
            d0 = i.blank_model.hole_diameter
            R = i.forming_tool_model.radius
            f = i.forming_conditions.feed_rate
            sd = i.forming_conditions.step_down
            h = i.part_model.flange_height
            toolpath = i.tool_path.toolpath_code
            g_code = i.nc_program.g_code
            if g_code == '':
                print('G-code not found: run Action 1.')
                return
            else:
                print('Action 1 completed:')
                print('    t0 = %0.1f mm, d0 = %0.1f mm, R = %d mm, feedrate = %d mm/min, step-down = %0.1f mm' % (t0, d0, R, f, sd))
                print('    theoretical flange height, h = %0.1f mm' % h)
                print('    tool path in file "%s"' % toolpath)
                print('    G-code in file "%s"' % g_code)

            is_prepared = i.specimen.is_prepared
            if not is_prepared in ['yes', 'y']:
                print('The specimen has not been prepared yet: run Action 2.')
                return
            else:
                print('Action 2 completed:')
                print('    The specimen has been prepared.')
            
            is_fractured = i.test_results.is_fractured
            if not is_fractured in ['yes', 'y', 'no', 'n']:
                print('The experimental hole flanging test has not been performed yet: run Action 3.')
                return
            else:
                print('Action 3 completed:')
                print('    The experimental hole flanging test has been performed.')

            if is_fractured in ['yes', 'y']:
                print('    The experimental test failed: a fracture was found.')
            else:
                print('    The experimental test was successful, no fracture was found.')

            fh = i.test_results.flange_height
            if is_fractured in ['yes', 'y']:
                print('Action 4 not applicable:')
                print('    The flange height cannot be measured in fractured specimens.')
            elif is_fractured in ['no', 'n']:
                if not fh > 0:
                    print('The flange height has not been measured yet: run Action 4.')
                    return
                else:
                    print('Action 4 completed:')
                    print('    Measured flange height = %.1f mm' % fh)

            strain = i.test_results.strain_distribution
            if is_fractured in ['yes', 'y', 'no', 'n']:
                if strain == '':
                    print('The strain distribution has not been measured yet: run Action 5.')
                    return
                else:
                    print('Action 5 completed:')
                    print('    Measured strain distribution in file "%s".' % strain)

            her = i.test_results.hole_expansion_ratio
            h_df = i.test_results.non_dimensional_flange_height
            t_t0 = i.test_results.non_dimensional_average_thickness
            global_lfr = i.lfr.global_lfr
            lfr_per_tool = i.lfr.lfr_per_tool
            if is_fractured in ['no', 'n']:
                if not t_t0 > 0:
                    print('Variables not calculated yet: HER, h/df, t/t0, global LFR and LFR per tool radius %d.' % R)
                    print('    Run Action 6.')
                    return
                else:
                    print('Action 6 completed:')
                    print('    HER = %.2f, h/df = %.2f, t/t0 = %.2f.' % (her, h_df, t_t0))
                    print('    Global LFR = %.2f, LFR using R%d = %.2f.' % (global_lfr, R, lfr_per_tool))

            c_lfr = i.conclusions.limit_forming_ratio
            c_h = i.conclusions.flange_height
            c_t = i.conclusions.average_thickness
            c_t0R = i.conclusions.bending_ratio
            if c_lfr == '':
                print('Conclusions not yet provided: run Action 7.')
                return
            else:
                print('Action 7 completed:')
                print('    Conclusions regarding the LFR: %s' % c_lfr)
                print('    Conclusions regarding the HER vs. h/df diagram: %s' % c_h)
                print('    Conclusions regarding the HER vs. t/t0 diagram: %s' % c_t)
                print('    Conclusions regarding the bending ratio t0/R: %s' % c_t0R)
        except Exception as e:
            print('***** Exception found:')
            print(e)
    """


    @staticmethod
    def print_status(instance_name):
        next_action = Visualization._get_next_action(instance_name)

        print('')
        print('Status of instance "%s":' % instance_name)
        i = DataInstance(instance_name)
        i.load()
        
        if next_action > 1:
            t0 = i.blank_model.thickness
            d0 = i.blank_model.hole_diameter
            R = i.forming_tool_model.radius
            f = i.forming_conditions.feed_rate
            sd = i.forming_conditions.step_down
            h = i.part_model.flange_height
            toolpath = i.tool_path.toolpath_code
            g_code = i.nc_program.g_code
            print('Action 1 completed:')
            print('    t0 = %0.1f mm, d0 = %0.1f mm, R = %d mm, feedrate = %d mm/min, step-down = %0.1f mm' % (t0, d0, R, f, sd))
            print('    theoretical flange height, h = %0.1f mm' % h)
            print('    tool path in file "%s"' % toolpath)
            print('    G-code in file "%s"' % g_code)
        if next_action > 2:
            print('Action 2 completed:')
            print('    The specimen has been prepared.')
        if next_action > 3:
            print('Action 3 completed:')
            print('    The experimental hole flanging test has been performed.')
            is_fractured = i.test_results.is_fractured
            if is_fractured in ['yes', 'y']:
                print('    The experimental test failed: a fracture was found.')
                print('Action 4 not applicable:')
                print('    The flange height cannot be measured in fractured specimens.')
            else:
                print('    The experimental test was successful, no fracture was found.')
        if next_action > 4 and is_fractured in ['no', 'n']:
            fh = i.test_results.flange_height
            print('Action 4 completed:')
            print('    Measured flange height = %.1f mm' % fh)
        if next_action > 5:
            strain = i.test_results.strain_distribution
            print('Action 5 completed:')
            print('    Measured strain distribution in file "%s".' % strain)
        if next_action > 6:
            her = i.test_results.hole_expansion_ratio
            h_df = i.test_results.non_dimensional_flange_height
            t_t0 = i.test_results.non_dimensional_average_thickness
            global_lfr = i.lfr.global_lfr
            lfr_per_tool = i.lfr.lfr_per_tool
            print('Action 6 completed:')
            if is_fractured in ['no', 'n']:
                print('    HER = %.2f, h/df = %.2f, t/t0 = %.2f.' % (her, h_df, t_t0))
            print('    Global LFR = %.2f, LFR using R%d = %.2f.' % (global_lfr, R, lfr_per_tool))
        if next_action > 7:
            c_lfr = i.conclusions.limit_forming_ratio
            c_h = i.conclusions.flange_height
            c_t = i.conclusions.average_thickness
            c_t0R = i.conclusions.bending_ratio
            print('Action 7 completed:')
            print('    Conclusions regarding the LFR: %s' % c_lfr)
            print('    Conclusions regarding the HER vs. h/df diagram: %s' % c_h)
            print('    Conclusions regarding the HER vs. t/t0 diagram: %s' % c_t)
            print('    Conclusions regarding the bending ratio t0/R: %s' % c_t0R)
            print('All actions completed!')

        if next_action == 1:
            print('G-code not found: run Action 1.')
        elif next_action == 2:
            print('The specimen has not been prepared yet: run Action 2.')
        elif next_action == 3:
            print('The experimental hole flanging test has not been performed yet: run Action 3.')
        elif next_action == 4:
            print('The flange height has not been measured yet: run Action 4.')
        elif next_action == 5:
            print('The strain distribution has not been measured yet: run Action 5.')
        elif next_action == 6:
            print('Variables not calculated yet: HER, h/df, t/t0, global LFR and LFR per tool radius %d: run Action 6.' % R)
        elif next_action == 7:
            print('Conclusions not yet provided: run Action 7.')









    

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    from Data_Layer.data import *
    
    os.chdir('..')
    
    v = Visualization('instance01')
    v.print_instances()
    v.print_status()

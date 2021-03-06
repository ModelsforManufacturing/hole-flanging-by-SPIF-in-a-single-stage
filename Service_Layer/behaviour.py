# this is optional:
#from interfaces.service_interface import ServiceInterface
#class Behaviour(ServiceInterface):

import os
from Data_Layer.data import DataInstance

class Behaviour:
    def __init__(self, instance_name):
        self.instance_name = instance_name

    @staticmethod
    def __find_instances():
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
    def calculate_flange_height(instance_name, t0, d0, df, R):
        '''
        Simple estimation for the final flange height.
        '''
        h = (df - d0)/2
        print('Calculating flange height:')
        print('   t0 = %f mm, d0 = %f mm, R = %f mm, df = %f mm' % (t0, d0, R, df))
        print('   Output: flange height = %f mm' % h)
        return h

    @staticmethod
    def calculate_tool_path(instance_name, t0, df, h, R, f, sd):
        print('Generating toolpath code:')
        print('   t0 = %f mm, df = %f mm, h = %f mm, R = %f mm, f = %f mm/min, sd = %f mm' % (t0, df, h, R, f, sd))
        
        import Service_Layer.nc_program_SPIF_helix.toolpath_helix as tp
        filename = tp.toolpath_helix(instance_name, R, h, df, f, sd)
        
        print('   Output: tool path in file "%s"' % filename)
        return filename # toolpath_code

    @staticmethod
    def generate_g_code(instance_name, toolpath):
        g_code = "nc-program.gcode"
        print('Generating G-code:')
        print('   tool path in file "%s"' % toolpath)

        import Service_Layer.nc_program_SPIF_helix.toolpath2gcode as tp
        g_code = tp.toolpath2gcode(instance_name, toolpath)

        print('   Output: G-code in file "%s"' % g_code)
        return g_code

    @staticmethod
    def prepare_specimen(instance_name, t0, d0, g_code):
        if g_code == '':
            print('Warning: the G-code is required before executing this action.')
            is_prepared = ''
        else:
            print('To perform the experimental test, a specimen is required with a %f-mm sheet thickness and a %f-mm hole diameter.' % (t0, d0))
            is_prepared = input('Has the specimen already been manufactured? ')
            is_prepared = is_prepared.lower()
            if is_prepared in ['yes', 'y']:
                print('Ok, task completed.')
            elif is_prepared in ['no', 'n']:
                print('Ok. Please note that this task has not been completed yet.')
            else:
                print('Answer not valid.')
                is_prepared = ''
        return is_prepared

    @staticmethod
    def perform_hole_flanging_test(instance_name, gcode, is_prepared):
        if not is_prepared in ['yes', 'y']:
            print('Warning: the specimen has not been prepared yet.')
            is_fractured = ''
        else:
            print('Use the prepared speciment to perform an experimental hole flanging test.')
            print('G-code: %s' % gcode)
            print("Enter Yes or No if the speciment has fractured or not, respectively. Enter anything else if the experiment hasn't been done yet.")
            is_fractured = input('Is the specimen fractured (Yes/No)? ')
            is_fractured = is_fractured.lower()
            if is_fractured in ['yes', 'y', 'no', 'n']:
                print('Ok, task completed.')
            else:
                print('Ok. Please note that this task has not been completed yet.')
                is_fractured = ''
        return is_fractured

    @staticmethod
    def measure_flange_height(instance_name, is_fractured):
        if not is_fractured in ['yes', 'y', 'no', 'n']:
            print('Wait, wait... was the specimen fractured or not?')
            h = 0
        elif is_fractured in ['yes', 'y']:
            print('Flange height cannot be measured for a fractured specimen.')
            h = 0
        else: # is_fractured == "no"
            h = float(input('Enter the measured flange height (mm): '))
        return h

    @staticmethod
    def measure_strain_distribution(instance_name, is_fractured):
        strain = ''
        if not is_fractured in ['yes', 'y', 'no', 'n']:
            print('Wait, wait... was the specimen fractured or not?')
        else: # is_fractured == "no" or "yes"
            print('Use ARGUS to obtain the strain distribution along the flange.')
            print('Save the results as a text file "strain.csv" and upload it to "Data_Layer/%s".' % instance_name)
            q = input('Is the file already uploaded? (Yes/No) ')
            q = q.lower()
            if q in ['yes', 'y']:
                strain = 'strain.csv'
        return strain

    @staticmethod
    def calculate_hole_expansion_ratio(instance_name, is_fractured, df, d0):
        if not is_fractured in ['no', 'n']:
            print('Warning: this task can only be executed for non fractured specimens.')
            her = 0
        else:
            print('Calculating HER...')
            her = df/d0
            print('    Output: HER = df/d0 = %f' % her)
        return her

    @staticmethod
    def calculate_non_dimensional_flange_height(instance_name, is_fractured, h, df):
        if not is_fractured in ['no', 'n']:
            print('Ups! h/df can be only calculated if the specimen was no fractured')
            h_df = 0
        else:
            print('Calculating h/df...')
            h_df = h/df
            print('    Output: h/df = %f' % h_df)
        return h_df

    @staticmethod
    def calculate_non_dimensional_average_thickness(instance_name, is_fractured, h, d0, df, t0):
        if not is_fractured in ['no', 'n']:
            print('Ups! t/t0 can be only calculated if the specimen was no fractured')
            t_t0 = 0
        else:
            print('Calculating t/t0...')
            t = t0*(df-d0)/2/h                      # only for test purposes
            t_t0 = t/t0
            print('    Output: t/t0 = %f' % t_t0)
        return t_t0

    @staticmethod
    def calculate_global_lfr(instance_name, her, is_fracture):
        # search in all succesful tests and calculate LFR=max(HER)
        instances = Behaviour.__find_instances()
        her_list = []
        for instance_name in instances:
            i = DataInstance(instance_name)
            i.load()
            her = i.test_results.hole_expansion_ratio
            her_list.append(her)
        global_lfr = max(her_list)    
        return global_lfr

    @staticmethod
    def calculate_lfr_per_tool(instance_name, R, her, is_fracture):
        # search in all succesful tests using tool radius R and calculate LFR=max(HER)
        instances = Behaviour.__find_instances()
        her_list = []
        for instance_name in instances:
            i = DataInstance(instance_name)
            i.load()
            tool_R = i.forming_tool_model.radius
            if tool_R == R:
                her = i.test_results.hole_expansion_ratio
                her_list.append(her)
        lfr_per_tool = max(her_list)    
        return lfr_per_tool

    @staticmethod
    def plot_global_fld(instance_name, strain_distribution, fracture_forming_limit):
        ffl_file    = 'Data_Layer/%s' % fracture_forming_limit
        strain_file = 'Data_Layer/%s/%s' % (instance_name, strain_distribution)
        instances   = Behaviour.__find_instances()
        strain_files = []
        for i in instances:
            fn = 'Data_Layer/%s/strain.csv' % i
            if i!=instance_name and os.path.isfile(fn):
                strain_files.append(fn)

        print('Plotting FLD for all specimens...')
        
        import Service_Layer.plot_results.plot_FLD as plot
        global_fld = 'FLD_successful_tests.png'
        plot.plot_fld(instance_name, ffl_file, strain_file, strain_files, 
            'Data_Layer/%s/%s' % (instance_name, global_fld))

        return global_fld
        
    @staticmethod
    def plot_fld_per_tool(instance_name, strain_distribution, fracture_forming_limit, R):
        ffl_file    = 'Data_Layer/%s' % fracture_forming_limit
        strain_file = 'Data_Layer/%s/%s' % (instance_name, strain_distribution)
        instances   = Behaviour.__find_instances()
        strain_files = []
        for i in instances:
            di = DataInstance(i)
            di.load()
            tool_R = di.forming_tool_model.radius
            fn = 'Data_Layer/%s/strain.csv' % i
            if i!=instance_name and os.path.isfile(fn) and tool_R==R:
                strain_files.append(fn)

        print('Plotting FLD for specimens tested with a tool radius R=%s...' % R)
        import Service_Layer.plot_results.plot_FLD as plot
        fld_per_tool = 'FLD_R%d.png' % R
        plot.plot_fld(instance_name, ffl_file, strain_file, strain_files, 
            'Data_Layer/%s/%s' % (instance_name, fld_per_tool))

        return fld_per_tool

    @staticmethod
    def plot_fld_for_successful_tests(instance_name, strain_distribution, fracture_forming_limit, is_fractured):
        ffl_file    = 'Data_Layer/%s' % fracture_forming_limit
        strain_file = 'Data_Layer/%s/%s' % (instance_name, strain_distribution)
        instances   = Behaviour.__find_instances()
        strain_files = []
        for i in instances:
            di = DataInstance(i)
            di.load()
            fract = di.test_results.is_fractured
            fn = 'Data_Layer/%s/strain.csv' % i
            if i!=instance_name and os.path.isfile(fn) and fract in ['no', 'n']:
                strain_files.append(fn)

        print('Plotting FLD for this specimen along with successful tests...')
        import Service_Layer.plot_results.plot_FLD as plot
        fld_for_successful_tests = 'FLD_successful_tests.png'
        plot.plot_fld(instance_name, ffl_file, strain_file, strain_files, 
            'Data_Layer/%s/%s' % (instance_name, fld_for_successful_tests))

        return fld_for_successful_tests

    @staticmethod
    def plot_fld_for_fractured_tests(instance_name, strain_distribution, fracture_forming_limit, is_fractured):
        ffl_file    = 'Data_Layer/%s' % fracture_forming_limit
        strain_file = 'Data_Layer/%s/%s' % (instance_name, strain_distribution)
        strain_files = []
        instances = Behaviour.__find_instances()
        for i in instances:
            di = DataInstance(i)
            di.load()
            fract = di.test_results.is_fractured
            fn = 'Data_Layer/%s/strain.csv' % i
            if i!=instance_name and os.path.isfile(fn) and fract in ['yes', 'y']:
                strain_files.append(fn)

        print('Plotting FLD for this specimen along with failed tests...')
        import Service_Layer.plot_results.plot_FLD as plot
        fld_for_fractured_tests = 'FLD_failed_tests.png'
        plot.plot_fld(instance_name, ffl_file, strain_file, strain_files, 
            'Data_Layer/%s/%s' % (instance_name, fld_for_fractured_tests))

        return fld_for_fractured_tests

    @staticmethod
    def plot_h_df(instance_name, h_df):
        data_SPIF = []
        instances = Behaviour.__find_instances()
        for i in instances:
            di = DataInstance(i)
            di.load()
            fract   = di.test_results.is_fractured
            R       = di.forming_tool_model.radius
            her     = di.test_results.hole_expansion_ratio
            h_df    = di.test_results.non_dimensional_flange_height
            if fract in ['no', 'n']:
                data_SPIF.append([R, her, h_df])
        
        print('Plotting HER versus h/df...')
        import Service_Layer.plot_results.plot_HER_h as plot
        flange_height_diagram = 'diagram_HER-h.png'
        plot.plot_her_h(data_SPIF, 'Data_Layer/%s/%s' % (instance_name, flange_height_diagram))

        return flange_height_diagram

    @staticmethod
    def plot_t_t0(instance_name, t_t0):
        data_SPIF = []
        instances = Behaviour.__find_instances()
        for i in instances:
            di = DataInstance(i)
            di.load()
            fract   = di.test_results.is_fractured
            R       = di.forming_tool_model.radius
            her     = di.test_results.hole_expansion_ratio
            t_t0    = di.test_results.non_dimensional_average_thickness
            if fract in ['no', 'n']:
                data_SPIF.append([R, her, t_t0])
        
        print('Plotting HER versus (t0-t)/t0...')
        import Service_Layer.plot_results.plot_HER_t as plot
        average_thickness_diagram = 'diagram_HER-t.png'
        plot.plot_her_t(data_SPIF, 'Data_Layer/%s/%s' % (instance_name, average_thickness_diagram))

        return average_thickness_diagram

    @staticmethod
    def conclusions_for_lfr(instance_name, global_lfr, lfr_per_tool):
        conclusions_limit_forming_ratio = input('Write the main conclusions regarding the LFR = %.2f: ' % global_lfr)
        return conclusions_limit_forming_ratio
        
    @staticmethod
    def conclusions_for_height(instance_name, flange_height_diagram):
        print('Showing the HER vs. h/df diagram...')

        from matplotlib import pyplot as plt
        from matplotlib import image as mpimg
        image = mpimg.imread('Data_Layer/%s/%s' % (instance_name, flange_height_diagram))
        plt.imshow(image)
        plt.show()
        conclusions_flange_height = input('Write the main conclusions regarding the HER vs. h/df diagram: ')

        return conclusions_flange_height
        
    @staticmethod
    def conclusions_for_thickness(instance_name, average_thickness_diagram):
        print('Showing the HER vs. t/t0 diagram...')

        from matplotlib import pyplot as plt
        from matplotlib import image as mpimg
        image = mpimg.imread('Data_Layer/%s/%s' % (instance_name, average_thickness_diagram))
        plt.imshow(image)
        plt.show()
        conclusions_average_thickness = input('Write the main conclusions regarding the HER vs. t/t0 diagram: ')

        return conclusions_average_thickness
        
    @staticmethod
    def conclusions_for_t0_r(instance_name, average_thickness_diagram, flange_height_diagram, global_fld, fld_per_tool, fld_for_successful_tests, fld_for_fractured_tests, global_lfr, lfr_per_tool):
        from matplotlib import pyplot as plt
        from matplotlib import image as mpimg

        print('Showing the FLD...')
        image = mpimg.imread('Data_Layer/%s/%s' % (instance_name, global_fld))
        plt.imshow(image)
        plt.show()

        print('Showing the FLD for successful tests...')
        image = mpimg.imread('Data_Layer/%s/%s' % (instance_name, fld_for_successful_tests))
        plt.imshow(image)
        plt.show()

        conclusions_bending_ratio = input('Write the main conclusions regarding the bending ratio t0/R: ')

        return conclusions_bending_ratio
        

    

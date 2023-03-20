#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

from string import Template
import pydot        # Python interface to Graphviz's Dot language
import shutil       # High-level file operations
import datetime     # Basic date and time types
import Ontology_Layer.parse_graphviz_data_model as pgv
import Ontology_Layer.parse_csv_semantic_model as pcsv


### templates to write Python code

indent = 4 # number of whitespaces for indentation in Python


template_interface_head = Template("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

Interfaces for the definition of Objects and Parameters of the Data Model.
Implementation must be done in module:
    Data_Layer.data_interface_implementation

This file has been generated automatically.
'''

$interfaces
""")


template_interface = Template("""class ${class_name}Interface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    ${class_description}
    '''
    def __init__(self, ${args}):
        '''
        Use the object constructor to retrieve these parameters:
${args_comment}
        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

""")


template_class = Template("""class ${class_name}:
    def __init__(self, ${args}):
${class_init}
    def load(self, instance_name):
${class_load}
    def save(self, instance_name):
${class_save}
""")


template_data_head = Template("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

Functions to retrieve/save data from/to the Data Layer.

Implementation of all interfaces:
    <Class>Interface
in module:
    interfaces.data_interface

This file has been generated automatically.
'''

import os           # Miscellaneous operating system interfaces
import configparser # Configuration file parser
import shutil       # High-level file operations
import datetime     # Basic date and time types

$classes

class DataInstance:
    '''
    '''
    def __init__(self, instance_name):
        '''
        Creates a DataInstance object with 2 parameters:
        instance_name -- string
        datafile -- string
        '''
        self.instance_name = instance_name
        self.datafile = 'Data_Layer/%s/data.ini' % instance_name
        

    def new(self):
        '''
        Populates DataInstance object with empty parameters (string='' and float=0).
        '''
${parser_set_empty_parameter_values}
${parser_define_object_parameters}
        self.save()

    def load(self):
        '''
        Creates a Instance object with data from a `data.ini` file.
        '''
        config = configparser.ConfigParser()
        config.read(self.datafile)
${parser_get_parameter_values}
${parser_define_object_parameters}

    def save(self):
        '''
        Make a backup copy of `data.ini` before saving the data.
        '''
        if not os.path.isfile(self.datafile):
            os.makedirs(self.datafile.replace('data.ini', ''))
            open(self.datafile, 'a').close()
        else:
            # Backup of 'data.ini'
            date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            datafile_backup = 'Data_Layer/%s/data_%s.ini' % (self.instance_name, date)
            shutil.copyfile(self.datafile, datafile_backup)

        config = configparser.ConfigParser()
${parser_save_parameter_values}
        with open(self.datafile, 'w') as configfile:
            config.write(configfile)
    
""")



### functions to write Python code using the templates above

def code_parameter_list(args):
    ''' Return a string with parameters separated by comas '''
    s = ''
    for p in args:
        s = '%s, %s' % (s, p)
    if len(args) > 0:
        s = s[2:]  # remove the first ', ' from the argument list string
    return s

def code_class_init(args, n_indent):
    ''' Return a string with multiple lines with indentation '''
    count = 0
    d = {}
    s=''''''
    if len(args)==0:
        s += '%spass' % (' '*n_indent)
    for i in args:
        d['i_%d' % count] = ('%s' % i['param_name'])        # dictionary: {i_1=args[1], i_2=...}
        s += ' '*n_indent                                   # indentation with whitespaces
        s = '%sself.$i_%d = $i_%d\n' % (s, count, count)    # string: '    self.$i_1 = $i_1\n'
        count += 1
    s = Template(s)
    s = s.substitute(d)
    return s

def code_class_load(class_name, object_name, params, n_indent):
    ''' Return a string with multiple lines with indentation '''
    d = {}
    s=''''''
    s = '%s%si = DataInstance(instance_name)\n' % (s, ' '*n_indent)
    s = '%s%si.load()\n' % (s, ' '*n_indent)
    for i in params:
        p = i['param_name']
        d[p] = ('%s' % i['param_name'])
        s = '%s%sself.$%s = i.%s.$%s\n' % (s, ' '*n_indent, p, object_name, p)
    s = Template(s)
    s = s.substitute(d)
    return s

def code_class_save(class_name, object_name, params, n_indent):
    ''' Return a string with multiple lines with indentation '''
    d = {}
    s=''''''
    s = '%s%si = DataInstance(instance_name)\n' % (s, ' '*n_indent)
    s = '%s%si.load()\n' % (s, ' '*n_indent)
    for i in params:
        p = i['param_name']
        d[p] = ('%s' % i['param_name'])
        s = '%s%si.%s.$%s = self.$%s\n' % (s, ' '*n_indent, object_name, p, p)
    s = '%s%si.save()\n' % (s, ' '*n_indent)
    s = Template(s)
    s = s.substitute(d)
    return s

def code_parameter_comment(args, n_indent):
    ''' Return a string with multiple lines with indentation '''
    count = 0
    d = {}
    s=''''''
    for i in args:
        d['i_{}'.format(count)] = ''.join(i['param_name']) # dictionary: {i_1=args[1], i_2=...}
        s+=' '*n_indent                         # indentation with whitespaces
        s = '%s$i_%d -- (%s) %s\n' % (s, count, i['param_type'], i['param_description']) # string: '    $i_1 -- float, Description\n'
        count += 1
    s = Template(s)
    s = s.substitute(d)
    return s

def generate_names(nodes, semantic_data):
    ''' Return a dictionary with objects and parameters data '''
    param_counter = 1
    data = []
    for c in nodes: # c=class, p=parameter
        node = nodes[c]
        class_name = c.title().replace(' ', '')     # remove withespaces in class name
        object_name = c.lower().replace(' ', '_')   # replace withespaces with '_' in parameter name
        params = [] # [param_name, param_type, param_description, param_n]
        if 'parameter' in node:
            for p in node['parameter']:
                param_name = p.lower().replace(' ', '_').replace('-', '_')
                param_num = '%s_%s' % (param_name, param_counter) # add counter to parameter name
                param_type, param_description = pcsv.get_semantic_data(semantic_data, c, p)
                pd = dict(
                    param = p,
                    param_name = param_name,
                    param_num = param_num,
                    param_type = param_type,
                    param_description = param_description,
                )
                params.append(pd)
                param_counter += 1
        cd = dict(
            concept = c,
            class_name = class_name,
            object_name = object_name,
            params = params
        )
        data.append(cd)
    return data


def generate_data_interface_file(graphviz_file, semantic_file):
    ''' Return a string with the definition of all classes in Python '''
    graphs = pydot.graph_from_dot_file(graphviz_file)
    graph = graphs[0]
    nodes = pgv.get_nodes(graph)
    nodes = pgv.mfm_format(nodes)
    
    semantic_data = pcsv.read_semantic_model(semantic_file)
    data = generate_names(nodes, semantic_data)
    r = ''
    for d in data:
        p = [i['param_name'] for i in d['params']]
        s = code_parameter_list(p)
        comment_params = code_parameter_comment(d['params'], indent*2)
        d = dict(
            class_name = d['class_name'],
            class_description = 'Description: TODO',
            args = s,
            args_comment = comment_params,
        )
        r = r + template_interface.substitute(d)
    r = template_interface_head.substitute(interfaces = r)
    return r


def generate_data_file(graphviz_file, semantic_file):
    ''' Return a string with the definition of interfaces in Python '''
    graphs = pydot.graph_from_dot_file(graphviz_file)
    graph = graphs[0]
    nodes = pgv.get_nodes(graph)
    nodes = pgv.mfm_format(nodes)
    
    semantic_data = pcsv.read_semantic_model(semantic_file)
    data = generate_names(nodes, semantic_data)
    
    r = ''
    for d in data:
        p = [i['param_name'] for i in d['params']]
        s = code_parameter_list(p)
        class_init = code_class_init(d['params'], indent*2)
        class_load = code_class_load(d['class_name'], d['object_name'], d['params'], indent*2)
        class_save = code_class_save(d['class_name'], d['object_name'], d['params'], indent*2)
        d = dict(
            class_name = d['class_name'],
            args = s,
            class_init = class_init,
            class_load = class_load,
            class_save = class_save,
        )
        r = r + template_class.substitute(d)
    classes = r

    str0 = ''
    str1 = ''
    str2 = ''
    str3 = ''
    for d in data:
        # str0: set_empty_parameter_values
        # str1: get_parameter_values
        for p in d['params']:
            if p['param_type'] == 'float':
                str0 = "%s%s%s = 0\n" % (str0, ' '*8, p['param_num'])
                str1 = "%s%s%s = float(config.get('%s', '%s'))\n" % (str1, ' '*8, p['param_num'], d['concept'], p['param'])
            else:
                str0 = "%s%s%s = ''\n" % (str0, ' '*8, p['param_num'])
                str1 = "%s%s%s = config.get('%s', '%s')\n" % (str1, ' '*8, p['param_num'], d['concept'], p['param'])

        # str2: define_object_parameters
        p = [i['param_num'] for i in d['params']]
        s = code_parameter_list(p)
        str2 = "%s%sself.%s = %s(%s)\n" % (str2, ' '*8, d['object_name'], d['class_name'], s)

        # str3: save_parameter_values
        str3 = "%s%sconfig['%s'] = {\n" % (str3, ' '*8, d['concept'])
        for p in d['params']:
            str3 = "%s%s'%s': self.%s.%s,\n" % (str3, ' '*12, p['param'], d['object_name'], p['param_name'])
        str3 = "%s%s}\n" % (str3, ' '*8)

    d = dict(
        classes = classes,
        parser_set_empty_parameter_values = str0,
        parser_get_parameter_values = str1,
        parser_define_object_parameters = str2,
        parser_save_parameter_values = str3,
    )
    r = template_data_head.substitute(d)
    return r


def backup_and_regenerate_data_interface_file(graphviz_file, semantic_file, python_file):
    # Backup
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    python_file_backup = '%s_%s' % (python_file, date)
    shutil.copyfile(python_file, python_file_backup)

    with open(python_file, 'w') as f:
        f.write(generate_data_interface_file(graphviz_file, semantic_file))


def backup_and_regenerate_data_file(graphviz_file, semantic_file, python_file):
    # Backup
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    python_file_backup = '%s_%s' % (python_file, date)
    shutil.copyfile(python_file, python_file_backup)

    with open(python_file, 'w') as f:
        f.write(generate_data_file(graphviz_file, semantic_file))


if __name__ == '__main__':
    data_enriched = 'Ontology_Layer/Data_Model/Data_Model.gv'
    semantic = 'Ontology_Layer/Semantic_Model/Semantic_Model.csv'
    
    backup_and_regenerate_data_interface_file(data_enriched, semantic, 
        'Service_Layer/if_data.py')

    backup_and_regenerate_data_file(data_enriched, semantic, 
        'Service_Layer/mw_data.py')


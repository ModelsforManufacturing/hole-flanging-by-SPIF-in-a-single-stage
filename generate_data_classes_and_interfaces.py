#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

from string import Template
import pydot        # Python interface to Graphviz's Dot language
import csv          # CSV File Reading and Writing
import shutil       # High-level file operations
import datetime     # Basic date and time types
import Ontology_Layer.parse_graphviz_data_model as pgv


### templates to write Python code

indent = 4 # number of whitespaces for indentation in Python


template_classes = Template("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

Definition of Objects (as classes) and its Paramenters for the Data Model.

This file has been generated automatically.
'''

$classes
""")


template_class = Template("""class ${class_name}:
    ''' ${class_description} '''
    def __init__(self, ${args}):
        '''
        Keyword arguments:
${args_comment}
        '''
${args_def}

""")


template_interfaces_data = Template("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

Functions to retrieve/save data from/to the Data Layer.

This file has been generated automatically.
'''

import configparser # Configuration file parser
import shutil       # High-level file operations
import datetime     # Basic date and time types
from interfaces.data_classes import *


class Instance:
    '''
    '''
    def __init__(self, instance_name):
        '''
        Creates a Instance object with data from a `data.ini` file.
        
        Keyword arguments:
        instance_name -- string
        '''
        self.instance_name = instance_name

        datafile = 'Data_Layer/%s/data.ini' % instance_name
        self.datafile = datafile
        
        parser = configparser.ConfigParser()
        parser.read(datafile)
${parser_str1}

${parser_str2}

    def save(self):
        '''
        Make a backup copy of `data.ini` before saving the data.
        '''
        # Backup of 'data.ini'
        date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        datafile_backup = 'Data_Layer/%s/data_%s.ini' % (self.instance_name, date)
        shutil.copyfile(self.datafile, datafile_backup)

        config = configparser.ConfigParser()
${parser_str3}
        
        with open(self.datafile, 'w') as configfile:
            config.write(configfile)
    
""")



### read CSV and return a dictionary

def read_semantic_model(semantic_model_file):
    ''' Read a CSV file and return a list of dictionaries '''
    data = []
    with open(semantic_model_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def get_semantic_data(semantic_data, data_object, parameter):
    for row in semantic_data:
        if (row['Object name'] == data_object) and (row['Parameter name'] == parameter):
            return (row['Type'], row['Description'])
    print("Warning: Parameter's type not found!")





### functions to write Python code using the templates above

def code_parameter_list(args):
    ''' Return a string with parameters separated by comas '''
    s = ''
    for p in args:
        s = '%s, %s' % (s, p)
    if len(args) > 0:
        s = s[2:]  # remove the first ', ' from the argument list string
    return s

def code_parameter_definition(args, n_indent):
    ''' Return a string with multiple lines with indentation '''
    count = 0
    d = {}
    s=''''''
    for i in args:
        d['i_%d' % count] = ('%s' % i['param_name'])       # dictionary: {i_1=args[1], i_2=...}
        s += ' '*n_indent                       # indentation with whitespaces
        s = '%sself.$i_%d = $i_%d\n' % (s, count, count) # string: '    self.$i_1 = $i_1\n'
        count += 1
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
                param_type, param_description = get_semantic_data(semantic_data, c, p)
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


def generate_classes(graphviz_file, semantic_file):
    ''' Return a string with the definition of all classes in Python '''
    graphs = pydot.graph_from_dot_file(graphviz_file)
    graph = graphs[0]
    nodes = pgv.get_nodes(graph)
    nodes = pgv.mfm_format(nodes)
    
    semantic_data = read_semantic_model(semantic_file)
    data = generate_names(nodes, semantic_data)
    r = ''
    for d in data:
        p = [i['param_name'] for i in d['params']]
        s = code_parameter_list(p)
        comment_params = code_parameter_comment(d['params'], indent*2)
        define_params = code_parameter_definition(d['params'], indent*2)
        d = dict(
            class_name = d['class_name'],
            class_description = 'Description: TODO',
            args = s,
            args_comment = comment_params,
            args_def = define_params,
        )
        r = r + template_class.substitute(d)
    r = template_classes.substitute(classes = r)
    return r


def generate_interfaces(graphviz_file, semantic_file):
    ''' Return a string with the definition of interfaces in Python '''
    graphs = pydot.graph_from_dot_file(graphviz_file)
    graph = graphs[0]
    nodes = pgv.get_nodes(graph)
    nodes = pgv.mfm_format(nodes)
    
    semantic_data = read_semantic_model(semantic_file)
    data = generate_names(nodes, semantic_data)
    
    r = ''
    str1 = ''
    str2 = ''
    str3 = ''
    for d in data:
        # str1
        for p in d['params']:
            if p['param_type'] == 'float':
                str1 = "%s%s%s = float(parser.get('%s', '%s'))\n" % (str1, ' '*8, p['param_num'], d['concept'], p['param'])
            else:
                str1 = "%s%s%s = parser.get('%s', '%s')\n" % (str1, ' '*8, p['param_num'], d['concept'], p['param'])

        # str2
        p = [i['param_num'] for i in d['params']]
        s = code_parameter_list(p)
        str2 = "%s%sself.%s = %s(%s)\n" % (str2, ' '*8, d['object_name'], d['class_name'], s)

        # str3
        str3 = "%s%sconfig['%s'] = {\n" % (str3, ' '*8, d['concept'])
        for p in d['params']:
            str3 = "%s%s'%s': self.%s.%s,\n" % (str3, ' '*12, p['param'], d['object_name'], p['param_name'])
        str3 = "%s%s}\n" % (str3, ' '*8)

    d = dict(
        parser_str1 = str1,
        parser_str2 = str2,
        parser_str3 = str3,
    )
    r = template_interfaces_data.substitute(d)
    return r


def backup_and_regenerate_classes(graphviz_file, semantic_file, python_file):
    # Backup
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    python_file_backup = '%s_%s' % (python_file, date)
    shutil.copyfile(python_file, python_file_backup)

    with open(python_file, 'w') as f:
        f.write(generate_classes(graphviz_file, semantic_file))


def backup_and_regenerate_interfaces(graphviz_file, semantic_file, python_file):
    # Backup
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    python_file_backup = '%s_%s' % (python_file, date)
    shutil.copyfile(python_file, python_file_backup)

    with open(python_file, 'w') as f:
        f.write(generate_interfaces(graphviz_file, semantic_file))


if __name__ == '__main__':
    data_enriched = 'Ontology_Layer/Data_Model/Data_Model_2_enriched.gv'
    semantic = 'Ontology_Layer/Semantic_Model/Semantic_Model.csv'
    
    backup_and_regenerate_classes(data_enriched, semantic, 
        'interfaces/data_classes.py')

    backup_and_regenerate_interfaces(data_enriched, semantic, 
        'interfaces/interfaces_data.py')


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
import os
import json
import Ontology_Layer.parse_graphviz_data_model as pgv
import Ontology_Layer.parse_csv_semantic_model as pcsv

### templates to write Python code

semantic_file = 'Ontology_Layer/Semantic_Model/Semantic_Model.csv'
indent = 4 # number of whitespaces for indentation in Python

template_behaviour_interface_method = Template("""${parser_method_declare}
    '''
${parser_interface_comments}
    '''
    pass
""")


template_mediating_controller_method = Template("""@staticmethod
    def ${parser_method_declare}(instance_name):
        i = DataInstance(instance_name)
        i.load()
${parser_method_inputs}
${parser_method_action}
${parser_method_outputs}

""")

template_behaviour_interface_head = Template("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

This file has been generated automatically.
'''

class BehaviourInterface:
${parser_methods}
    
""")

template_mediating_controller_head = Template("""#!/usr/bin/env python3
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

${parser_methods}
    
""")



### read GraphViz and return dictionaries

def get_nodes(s):
    ''' Find nodes in a block between comments and returns a dictionary '''
    
    s = 'digraph behaviourmodel {\n%s\n}' % s           # wrap string to define digraph
    graphs = pydot.graph_from_dot_data(s)
    graph = graphs[0]

    nodes = {}
    for n in graph.get_nodes():
        name = n.get_name()
        if name == 'node' or name == 'edge':            # skip 'node' and 'edge'
            continue

        label = n.get_label()

        if label:                                       # skip nodes like 'Start' and 'End'
            label = label.replace('\\n', ' ')           # remove \n
            label = ' '.join(label.split())             # remove duplicate spaces
            for c in '"{}':                             # remove characters
                label = label.replace(c, '')
            
            l = label.split('|')                        # find object
            obj = l[0].strip()                          # remove spaces at start and end

            if len(l) > 1:                              # object has parameters
                param = label.split('|')[-1].split('\l')
                param = [a.strip() for a in param]      # remove spaces at start and end
                param = [a for a in param if a != '']   # remove empty strings
            else:
                param = False
            
            if param:
                nodes[name] = {'class': obj, 'parameters': param}
            else:
                nodes[name] = obj

    return nodes


def get_edges(s):
    ''' Find edges in a block between comments and returns a list of [source, destination] '''
    
    s = 'digraph behaviourmodel {\n%s\n}' % s           # wrap string to define digraph
    graphs = pydot.graph_from_dot_data(s)
    graph = graphs[0]

    edges = []
    for e in graph.get_edges():
        src = e.get_source()
        dst = e.get_destination()
        lbl = e.get_label()
        
        src_nodes = []
        if type(src) is pydot.frozendict:
            for i in src['nodes']:
                if i != ',':
                    src_nodes.append(i)
        else:
            src_nodes = [src]
                
        dst_nodes = []
        if type(dst) is pydot.frozendict:
            for i in dst['nodes']:
                dst_nodes.append(i)
        else:
            dst_nodes = [dst]
        
        edges.append([src_nodes, dst_nodes, lbl])
                
    return edges


def attach_rules(s, tasks, rules):
    edges = get_edges(s)
    d = {}
    for e in edges:
        src, dst, lbl = e
        dt = {
            'name': tasks[src[0]], 
            'rule': rules[dst[0]], 
            }
        d[src[0]] = dt
    return d


def attach_mechanisms(s, tasks, mechanisms):
    edges = get_edges(s)
    for e in edges:
        src, dst, lbl = e
        if dst[0] == 'Start':
            for t in tasks:
                x = tasks[t]
                x['mechanism'] = mechanisms[src[0]]
        else:
            tasks[dst[0]]['mechanism'] = mechanisms[src[0]]
    return tasks


def attach_objects(s, tasks):
    edges = get_edges(s)
    for t in tasks:
        inputs, outputs = [], []
        for e in edges:
            src, dst, lbl = e
            if t in src:
                outputs = dst
            if t in dst:
                inputs = src
        tasks[t]['inputs'] = inputs
        tasks[t]['outputs'] = outputs
    return tasks

def attach_internal_objects(s, tasks):
    edges = get_edges(s)
    d = {}
    for e in edges:
        src, dst, lbl = e
        if lbl:
            for s in '"(),.':
                lbl = lbl.replace(s, '')
            lbl = lbl.replace(' ', '_')
            for t in tasks:
                if t in src:
                    x = tasks[t]
                    x['outputs'].append(lbl)
                if t in dst:
                    x = tasks[t]
                    x['inputs'].append(lbl)
    return tasks


def attach_constraints(s, tasks, constraints):
    edges = get_edges(s)
    d = {}
    for e in edges:
        src, dst, lbl = e
        for c in constraints:
            if dst[0] in c:                     # e.g. '{o1, o2} -> c1'
                d[constraints[c]] = src         # e.g. d = {'description': ['o1', 'o2']}
            if src[0] in c:                     # e.g. 'c1 -> t1'
                t = dst[0]
                tasks[t]['constraints'] = d
    return tasks




### functions to write Python code using the templates above

def generate_interface_method(task, objects):
    ''' Return a string with the definition of a Python function '''

    semantic_data = pcsv.read_semantic_model(semantic_file)

    # declare
    function_name = task['name'].lower()
    for xx in ' -/':
        function_name = function_name.replace(xx, '_')
    declare = '%sdef %s(self' % (' '*indent, function_name)
    
    args_counter = 0
    for i in task['inputs']:
        if i in objects:                                            # external objects
            c = objects[i]['class']
            p = objects[i]['parameters']
            for x in range(len(objects[i]['parameter_name'])):
                a = objects[i]['parameter_name'][x]
                args_counter += 1
                param_type, param_description = pcsv.get_semantic_data(semantic_data, c, p[x])
                declare = '%s,\n%s%s_%d: %s' % (declare, ' '*2*indent, a, args_counter, param_type)
        else:                                                       # internal objects
            args_counter += 1
            declare = '%s\n%s%s_%d = 0 # TO BE DEFINED' % (declare, ' '*indent, i, args_counter)
    declare = '%s) -> ' % (declare)

    for i in task['outputs']:
        if i in objects:                                            # external objects
            c = objects[i]['class']
            for a in objects[i]['parameters']:
                param_type, param_description = pcsv.get_semantic_data(semantic_data, c, a)
                declare = '%s%s, ' % (declare, param_type)
        else:                                                       # internal objects
            declare = '%s\n# TO BE DEFINED: %s' % (declare, i)
    declare = declare[:-2]                  # remove last 2 characters: ', '
    declare = '%s:' % (declare)
    
    # comments
    comments = '%s%s\n' % (' '*indent, task['rule'])
    comments = '%s\n%sArguments:' % (comments, ' '*indent)
    args_counter = 0
    for i in task['inputs']:
        if i in objects:                                            # external objects
            for a in objects[i]['parameter_name']:
                args_counter += 1
                c = objects[i]['class_name']
                comments = '%s\n%s%s_%d -- type: %s.%s' % (comments, ' '*2*indent, 
                    a, args_counter, c, a)
        else:                                                       # internal objects
            args_counter += 1
            comments = '%s\n%s%s_%d -- type: object' % (comments, ' '*2*indent, 
                i, args_counter)
    comments = '%s\n%sOutput:' % (comments, ' '*indent)
    args_counter = 0
    for i in task['outputs']:
        if i in objects:                                            # external objects
            for a in objects[i]['parameter_name']:
                args_counter += 1
                c = objects[i]['class_name']
                comments = '%s\n%s%s_%d -- type: %s.%s' % (comments, ' '*2*indent, 
                    a, args_counter, c, a)
        else:                                                       # internal objects
            args_counter += 1
            comments = '%s\n%s%s_%d -- type: object' % (comments, ' '*2*indent, 
                i, args_counter)
    
    return template_behaviour_interface_method.substitute(
        parser_method_declare = declare, 
        parser_interface_comments = comments, 
        )
    
def generate_method(task, objects):
    ''' Return a string with the definition of a Python function '''

    # declare
    function_name = task['name'].lower()
    for xx in ' -/':
        function_name = function_name.replace(xx, '_')
    declare = '%s' % (function_name)
    
    # inputs
    inputs = ''
    args_counter = 0
    for i in task['inputs']:
        if i in objects:                                            # external objects
            for a in objects[i]['parameter_name']:
                args_counter += 1
                c = objects[i]['object_name']
                inputs = '%s\n%s%s_%d = i.%s.%s' % (inputs, ' '*indent*2, a, args_counter, c, a)
        else:                                                       # internal objects
            args_counter += 1
            inputs = '%s\n%s%s_%d = 0 # TO BE DEFINED' % (inputs, ' '*indent*2, i, args_counter)
    
    # outputs
    outputs = ''
    args_counter = 0
    for i in task['outputs']:
        if i in objects:                                            # external objects
            for a in objects[i]['parameter_name']:
                args_counter += 1
                c = objects[i]['object_name']
                outputs = '%s\n%si.%s.%s = %s_%d' % (outputs, ' '*indent*2, c, a, a, args_counter)
                outputs = '%s\n%si.save()' % (outputs, ' '*indent*2)
        else:                                                       # internal objects
            args_counter += 1
            outputs = '%s\n%s# TO BE DEFINED: %s_%d' % (outputs, ' '*indent*2, i, args_counter)
    outputs = '%s\n' % (outputs)
    
    # return
    args = ''
    args_counter = 0
    for i in task['outputs']:
        if i in objects:                                            # external objects
            for a in objects[i]['parameter_name']:
                args_counter += 1
                args = '%s, %s_%d' % (args, a, args_counter)
        else:                                                       # internal objects
            args_counter += 1
            args = '%s, %s_%d' % (args, i, args_counter)
    if len(args) > 0:
        args = args[2:]  # remove the first ', ' from the argument list string
    outputs = '%s\n%sreturn %s' % (outputs, ' '*indent*2, args)

    # action
    args_counter = 0
    action_args = 'instance_name'                                        # by default
    for i in task['inputs']:
        if i in objects:                                            # external objects
            for a in objects[i]['parameter_name']:
                args_counter += 1
                action_args = '%s, %s_%d' % (action_args, a, args_counter)
        else:                                                       # internal objects
            args_counter += 1
            action_args = '%s, %s_%d' % (action_args, i, args_counter)
#    if len(action_args) > 0:
#        action_args = action_args[2:]  # remove the first ', ' from the argument list string
    action = '\n%s%s = Behaviour.%s(%s)' % (' '*indent*2, args, function_name, action_args)

    return template_mediating_controller_method.substitute(
        parser_method_declare = declare, 
        parser_method_inputs = inputs, 
        parser_method_action = action, 
        parser_method_outputs = outputs, 
        )
    

def get_tasks(graphviz_file):
    ''' Return a string with the definition of interfaces in Python '''
    with open(graphviz_file, 'r') as f:
        s = f.read()

    gv_comments = [
        '# activity title', 
        '# inputs and outputs', 
        '# mechanisms', 
        '# tasks definition', 
        '# rules', 
        '# attaching rules', 
        '# task sequence', 
        '# attaching mechanisms', 
        '# attaching inputs and outputs', 
        '# constraints', 
        '# attaching constraints', 
    ]

    # split graphviz between gv_comments
    block = []
    for x in range(len(gv_comments)-1):
        i0 = s.find(gv_comments[x]) + len(gv_comments[x])
        i1 = s.find(gv_comments[x+1])
        t = s[i0:i1].strip()        # string between comments
        block.append(t)
    block.append(s[i1:].strip())

    objects = get_nodes(block[1])           # inputs and outputs
    mechanisms = get_nodes(block[2])        # mechanisms
    tasks = get_nodes(block[3])             # tasks definition
    rules = get_nodes(block[4])             # rules
    constraints = get_nodes(block[9])       # constraints

    # format name of classes and parameters
    new_objs = {}
    for o in objects:
        c = objects[o]['class']
        p = objects[o]['parameters']
        
        new_obj = {}
        new_obj['class_name'] = c.replace(' ', '')     # remove spaces in class name
        new_obj['object_name'] = c.lower().replace(' ', '_')   # replace spaces with '_' in parameter name
        new_obj['parameter_name'] = []
        for i in range(len(p)):
            new_obj['parameter_name'].append(p[i].replace(' ', '_').replace('-', '_'))
        objects[o].update(new_obj)
    
    tasks = attach_rules(block[5], tasks, rules)                # attach rules
    tasks = attach_mechanisms(block[7], tasks, mechanisms)      # attach mechanisms
    tasks = attach_objects(block[8], tasks)                     # attach inputs and outputs
    tasks = attach_internal_objects(block[6], tasks)            # attach internal inputs and outputs
    tasks = attach_constraints(block[10], tasks, constraints)   # attach constraints

#    print(json.dumps(tasks, indent=4))

    return tasks, objects


def generate_interface_from_file(graphviz_file):
    ''' Return a string with the definition of interfaces in Python '''
    tasks, objects = get_tasks(graphviz_file)
    s = ''
    for t in tasks:
        s = '%s\n%s' % (s, generate_interface_method(tasks[t], objects))
    return s

def generate_methods_from_file(graphviz_file):
    ''' Return a string with the definition of interfaces in Python '''
    tasks, objects = get_tasks(graphviz_file)
    s = ''
    for t in tasks:
        s = '%s%s\n%s%s' % (' '*indent, s, ' '*indent, generate_method(tasks[t], objects))
    return s


def generate_behaviour_interface(graphviz_dir):
    s = ''
    for root, dirs, files in os.walk(graphviz_dir):
        # TODO: order files alphabetically
        for name in files:
            if name.endswith((".gv", ".dot")):
                graphviz_file = '%s/%s' % (graphviz_dir, name)
                r = generate_interface_from_file(graphviz_file)
                s += r
    r = template_behaviour_interface_head.substitute(parser_methods = s)
    return r

def generate_mediating_controller(graphviz_dir):
    s = ''
    for root, dirs, files in os.walk(graphviz_dir):
        # TODO: order files alphabetically
        for name in files:
            if name.endswith((".gv", ".dot")):
                graphviz_file = '%s/%s' % (graphviz_dir, name)
                r = generate_methods_from_file(graphviz_file)
                s += r
    r = template_mediating_controller_head.substitute(parser_methods = s)
    return r


def backup_and_regenerate_behaviour_interface(graphviz_dir, python_file):
    # Backup
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    python_file_backup = '%s_%s' % (python_file, date)
    shutil.copyfile(python_file, python_file_backup)

    with open(python_file, 'w') as f:
        f.write(generate_behaviour_interface(graphviz_dir))

def backup_and_regenerate_mediating_controller(graphviz_dir, python_file):
    # Backup
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    python_file_backup = '%s_%s' % (python_file, date)
    shutil.copyfile(python_file, python_file_backup)

    with open(python_file, 'w') as f:
        f.write(generate_mediating_controller(graphviz_dir))


if __name__ == '__main__':
    backup_and_regenerate_behaviour_interface(
        'Ontology_Layer/Behaviour_Model', 
        'interfaces/behaviour_interface.py')

    backup_and_regenerate_mediating_controller(
        'Ontology_Layer/Behaviour_Model', 
        'interfaces/mediating_controller.py')



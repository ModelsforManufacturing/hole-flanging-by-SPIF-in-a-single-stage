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

### templates to write Python code

indent = 4 # number of whitespaces for indentation in Python


template_function = Template("""def ${function_declare}:
    '''
${function_comments}
    '''
${function_inputs}
    
${function_action}

${function_output}

""")


template_interfaces_service = Template("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

This file has been generated automatically.

Functions to implement the Behaviour Model.

Format:

def <task>(<input_1>, ...(<input_n>):
    # <rule>
    if <constraint>:
        <action>
    else:
        <another_action>
    return (<output_1>, ...<output_n>)

'''

import interfaces.interfaces_data as data


${parser_functions}
    
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




template_function = Template("""def ${function_declare}:
    '''
${function_comments}
    '''
    
${function_inputs}
    
${function_action}

${function_output}

""")


### functions to write Python code using the templates above

def generate_function(task, objects):
    ''' Return a string with the definition of a Python function '''

    # declare
    function_name = task['name'].lower().replace(' ', '_')
    declare = '%s(instance)' % (function_name)
    
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
    
    # inputs
    inputs = '%si = data.Instance(instance)' % (' '*indent)
    args_counter = 0
    for i in task['inputs']:
        if i in objects:                                            # external objects
            for a in objects[i]['parameter_name']:
                args_counter += 1
                c = objects[i]['object_name']
                inputs = '%s\n%s%s_%d = i.%s.%s' % (inputs, ' '*indent, a, args_counter, c, a)
        else:                                                       # internal objects
            args_counter += 1
            inputs = '%s\n%s%s_%d = 0 # TO BE DEFINED' % (inputs, ' '*indent, i, args_counter)
    
    # action
    action = '%s# INSERT YOUR CODE HERE' % (' '*indent)

    # outputs
    outputs = ''
    args_counter = 0
    for i in task['outputs']:
        if i in objects:                                            # external objects
            for a in objects[i]['parameter_name']:
                args_counter += 1
                c = objects[i]['object_name']
                outputs = '%s\n%si.%s.%s = %s_%d' % (outputs, ' '*indent, c, a, a, args_counter)
        else:                                                       # internal objects
            args_counter += 1
            outputs = '%s\n%s%s_%d = 0 # TO BE DEFINED' % (outputs, ' '*indent, i, args_counter)
    outputs = '%s\n%si.save()' % (outputs, ' '*indent)
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
    outputs = '%s\n%sreturn %s' % (outputs, ' '*indent, args)

    return template_function.substitute(
        function_declare = declare, 
        function_comments = comments, 
        function_inputs = inputs, 
        function_action = action, 
        function_output = outputs, 
        )
    

def generate_functions_from_file(graphviz_file):
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
        new_objs[o] = new_obj
    objects = new_objs
    
    tasks = attach_rules(block[5], tasks, rules)                # attach rules
    tasks = attach_mechanisms(block[7], tasks, mechanisms)      # attach mechanisms
    tasks = attach_objects(block[8], tasks)                     # attach inputs and outputs
    tasks = attach_internal_objects(block[6], tasks)            # attach internal inputs and outputs
    tasks = attach_constraints(block[10], tasks, constraints)   # attach constraints

#    print(json.dumps(tasks, indent=4))

    s = ''
    for t in tasks:
        s = '%s\n%s' % (s, generate_function(tasks[t], objects))
    return s


def generate_interfaces(graphviz_dir):
    s = ''
    for root, dirs, files in os.walk(graphviz_dir):
        for name in files:
            if name.endswith((".gv", ".dot")):
                graphviz_file = '%s/%s' % (graphviz_dir, name)
                r = generate_functions_from_file(graphviz_file)
                s += r
    r = template_interfaces_service.substitute(parser_functions = s)
    return r


def backup_and_regenerate_interfaces(graphviz_dir, python_file):
    # Backup
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    python_file_backup = '%s_%s' % (python_file, date)
    shutil.copyfile(python_file, python_file_backup)

    with open(python_file, 'w') as f:
        f.write(generate_interfaces(graphviz_dir))


if __name__ == '__main__':
    backup_and_regenerate_interfaces(
        'Ontology_Layer/Behaviour_Model', 
        'interfaces/interfaces_service.py')


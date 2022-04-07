#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

Read the definition of the enriched data model in GraphViz format and generate a CSV file with the list of objects and parameters and two additional columns for the later definition of parameter's type and description.
"""

import pydot        # Python interface to Graphviz's Dot language
import csv          # CSV File Reading and Writing
import shutil       # High-level file operations
import datetime     # Basic date and time types
 
fieldnames = ['Object name', 'Parameter name', 'Type', 'Description']
data_model_file = 'Data_Model/Data_Model_2_enriched.gv'
semantic_model_file = 'Semantic_Model/Semantic_Model.csv'

def get_node_data(node):
    name = node.get_name()
    label = node.get_label()
    for c in '"{}':                             # remove characters from label
        label = label.replace(c, '')
    
    l = label.split('|')                        # find object
    obj = l[0].strip()                          # remove whitespaces at start and end

    if len(l) > 1:                              # object has parameters
        param = label.split('|')[-1].split('\l')
        param = [a.strip() for a in param]      # remove whitespaces at start and end
        param = [a for a in param if a != '']   # remove empty strings
    else:
        param = False
    
    return obj, param

def get_nodes(graph):
    ''' Find nodes in a graph and returns a dictionary with objects and parameters '''
    nodes = {}
    
    # graph without subgraphs
    if graph.get_subgraph_list() == []:
        for n in graph.get_nodes():
            if n.get_name() != 'node':
                obj, param = get_node_data(n)
                nodes[obj] = param
    # all nodes defined into subgraphs
    else:
        for subgraph in graph.get_subgraphs():
            for n in subgraph.get_nodes():
                obj, param = get_node_data(n)
                nodes[obj] = param
    return nodes

# read graohviz file and get nodes for Objects and Parameters
graphs = pydot.graph_from_dot_file(data_model_file)
graph = graphs[0]
nodes = get_nodes(graph)

# from nodes to dictionary
data = []
for n in nodes:
    class_name = n
    if not nodes[n]:
        print('"%s" has no parameters' % class_name)
        data.append({
            'Object name': class_name, 
            'Parameter name': '', 
            'Type': '', 
            'Description': ''})
        pass
    else:
        for p in nodes[n]:
            param_name = p
            data.append({
                'Object name': class_name, 
                'Parameter name': param_name, 
                'Type': '', 
                'Description': ''})

# Backup
date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
python_file_backup = '%s_%s' % (semantic_model_file, date)
shutil.copyfile(semantic_model_file, python_file_backup)

# save dictionary to a csv file
with open(semantic_model_file, 'w') as csvfile:    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
     


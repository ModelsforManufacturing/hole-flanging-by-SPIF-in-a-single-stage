#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

Parse the definition of the enriched Data Model in GraphViz Dot language to a dictionary.

Usage example:

    import pathlib
    import parse_graphviz_data_model as pgv
    
    gv_path = pathlib.Path('Data_Model/Data_Model.gv')
    data_objects = pgv.parse_data_model(gv_path)


Main function:

parse_data_model()
    Arguments:
        gv_path     -- graphviz file name path
    Call to auxiliary functions:
        get_nodes()
        add_edge_data_to_nodes()
        mfm_format()
    Return:
        nodes       -- dictionary with 'object' and lists of 'parameter', 'child' and 'parent'


Auxiliary functions:

get_nodes()
    Arguments:
        graph       -- graphviz graph or subgraph
    Return:
        nodes       -- dictionary, e.g. {"tool": {'object':"Forming Tool", 'parameters': ["diameter", "length"]}}
    Call to auxiliary functions:
        parse_node()

add_edge_data_to_nodes()
    Arguments:
        edge        -- graphviz edge
        nodes       -- nodes dictionary with 'object' and list of 'parameter'
    Return:
        nodes       -- dictionary updated with lists of 'child' and 'parent'
    Call to auxiliary functions:
        parse_edge()

parse_node()
    Arguments:
        node        -- a graphviz node, e.g. tool [label="{Forming Tool | diameter \l length \l}"]
    Return:
        short_name  -- short name of the graphviz node, e.g. "tool"
        obj         -- object name, e.g. "Forming Tool"
        param       -- list of parameters, e.g. ["diameter", "length"]
        
parse_edge()
    Arguments:
        edge        -- a graphviz edge, e.g. tools -> {holder, plate, rig} [label="has"]
    Return:
        src_nodes   -- list of source nodes, e.g. ["tools"]
        dst_nodes   -- list of destination nodes, e.g. ["holder", "plate", "rig"]
        lbl         -- edge label, e.g. "has"

mfm_format()
    Arguments:
        nodes       -- dictionary, e.g. {"tool": {'object':"Forming Tool", 'parameters': ["diameter", "length"]}}
    Return:
        new_nodes   -- dictionary, e.g. {"Forming Tool": {'parameter': ["diameter", "length"]}}

"""

import pathlib      # Object-oriented filesystem paths
import pydot        # Python interface to Graphviz's Dot language


def parse_node(node):
    '''
    Extract the object and its parameters from a graphviz 'node'.
    
    Format of a 'node' without parameters:
        <object short name> [label="<object name>"] 
    Format of a 'node' wit parameters:
        <object short name> [label="{<object name>|<parameter 1>\l<parameter 2>\l}"] 
    
    Examples:
        tool [label="Forming Tool Definition"] 
        tool [label="{Forming Tool Definition | diameter \l length \l}"] 
    '''
    short_name = node.get_name()
    label = node.get_label()
    for c in '"{}':                             # remove characters from 'label'
        label = label.replace(c, '')
    
    label = label.split('|')                    # get object
    obj = label[0].strip()                      # and remove whitespaces at start and end, if any

    if len(label) > 1:                          # if object has parameters
        param = label[-1].split('\l')           # select all parameters and separate them
        param = [a.strip() for a in param]      # remove whitespaces at start and end
        param = [a for a in param if a != '']   # remove empty strings
    else:
        param = False                           # if object has no parameters 
    
    return short_name, obj, param


def get_nodes(graph):
    ''' Find nodes in a graph and returns a dictionary with objects and parameters '''
    nodes = {}
    
    # for a graph without subgraphs
    if graph.get_subgraph_list() == []:
        for n in graph.get_nodes():                     # get nodes
            if not n.get_name() in ['node', r'"\n"']:   # skip 'node' node (and other stuff)
                short_name, obj, param = parse_node(n)  # call parse_node() to obtain the object and its paremeters
                if param:
                    nodes[short_name] = {'object':obj, 'parameters':param}
                else:
                    nodes[short_name] = {'object':obj}
    # when all nodes are defined into subgraphs
    else:
        for subgraph in graph.get_subgraphs():
            for n in subgraph.get_nodes():
                short_name, obj, param = parse_node(n)
                if param:
                    nodes[short_name] = {'object':obj, 'parameters':param}
                else:
                    nodes[short_name] = {'object':obj}
    return nodes


def parse_edge(edge):
    '''
    Extract sources, destinations and label from a graphviz 'edge'.
    Return a list of sources, a list of destinations and the label.
    
    Format of a 'edge' in graphviz:
        <object short name 1> -> <object short name 2> [label="<relation name>"] 
        {<obj name 1>, <obj name 2>} -> {<obj name 3>, <obj name 4>} [label="<relation name>"] 
    
    Examples:
        tools -> {holder, plate, rig} [label="has"]
        setup -> machine [label="defined by"]
    '''
    src = edge.get_source()
    dst = edge.get_destination()
    lbl = edge.get_label()
    if lbl:
        lbl = lbl.replace('"', '')
    
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
            if i != ',':
                dst_nodes.append(i)
    else:
        dst_nodes = [dst]
        
    return src_nodes, dst_nodes, lbl

def add_edge_data_to_nodes(edge, nodes):
    ''' Update graphviz nodes with data from a given graphviz edge '''
    src, dst, lbl = parse_edge(edge)        # call parse_edge()
    
    if lbl in [None, 'has', 'is', 'can be', 'can has']: # if edge is a parent-child relation
    
        # update childs of nodes
        for s in src:
            n = nodes[s]
            childs = []
            if 'child' in n:
                childs = n['child']
            for d in dst:
                if not d in childs:
                    childs.append(d)
                    n.update({'child': childs})

        # update parents of nodes
        for d in dst:
            n = nodes[d]
            parents = []
            if 'parent' in n:
                parents = n['parent']
            for s in src:
                if not s in parents:
                    parents.append(s)
                    n.update({'parent': parents})
    
    else:                                       # if edge is a not parent-child relation
    
        for s in src:
            n = nodes[s]
            relations = []
            if 'relation' in n:
                relations = n['relation']
            for d in dst:
                if not lbl in relations:
                    d_name = nodes[d]['object']
                    relations.append({lbl: {'to': d_name}})
                    n.update({'relation': relations})
            if 'child' in n:
                childs = n['child']
                if d in childs:
                    childs.remove(d)
                    n.update({'child': childs})
            
        for d in dst:
            n = nodes[d]
            relations = []
            if 'relation' in n:
                relations = n['relation']
            for s in src:
                if not lbl in relations:
                    s_name = nodes[s]['object']
                    relations.append({lbl: {'from': s_name}})
                    n.update({'relation': relations})
            if 'parent' in n:
                parents = n['parent']
                if s in parents:
                    parents.remove(s)
                    n.update({'parent': parents})
    
    return nodes


def parse_data_model(gv_path):
    ''' Find edges in a block between comments and returns a list of [source, destination] '''
    graphs = pydot.graph_from_dot_file(gv_path)
    graph = graphs[0]
    nodes = get_nodes(graph)                            # parse nodes

    # for a graph without subgraphs
    if graph.get_subgraph_list() == []:
        for e in graph.get_edges():
            nodes = add_edge_data_to_nodes(e, nodes)    # parse edges and update nodes
    # when all nodes are defined into subgraphs
    else:
        for subgraph in graph.get_subgraphs():
            for e in subgraph.get_edges():
                nodes = add_edge_data_to_nodes(e, nodes)

    return mfm_format(nodes)


def mfm_format(nodes):
    ''' Convert to a dictionary according to the MfM Metamodel '''
    new_nodes = {}
    for n in nodes:
        node = nodes[n]

        obj_name = node['object']
        obj_values = {}

        if 'parameters' in node:
            obj_values.update({'parameter': node['parameters']})

        if 'parent' in node:
            parent = [nodes[p]['object'] for p in node['parent']]
            obj_values.update({'parent': parent})

        if 'child' in node:
            child = [nodes[p]['object'] for p in node['child']]
            obj_values.update({'child': child})

        if 'relation' in node:
            obj_values.update({'relation': node['relation']})

        new_nodes.update({obj_name: obj_values})

    return new_nodes
    

if __name__ == '__main__':
    gv_path = pathlib.Path('Data_Model/Data_Model.gv')
    data_objects = parse_data_model(gv_path)

    import json
    print(json.dumps(data_objects, indent=4))


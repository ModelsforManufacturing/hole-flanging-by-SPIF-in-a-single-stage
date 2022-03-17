# MfM case study: hole flanging by SPIF in a single stage


## 3-Layer Model Overview

![](overview.png)


## Ontology Layer

See [Ontology_Layer/README.md](Ontology_Layer/README.md)


## Data Layer

### `files`

All original complementary files required to perform the MfM simulation (CAD/CAM models, Finite Element models, tables with material properties, etc.) are stored in the directory `Data_Layer/files`.


### `data.ini`

A directory `Data_Layer/<instance_name>` must be created for every instance that must contain a configuration file `data.ini` with all the instance data. 
Example of a configuration file:

    # Hole flanging by SPIF in a single stage
    # Units:
    #    [length] = mm
    #    [time] = min
    #    [stress, elasticity modulus] = MPa
    
    [Blank Sheet]
    hole diameter = 58
    
    [Raw Material]
    thickness = 1.6
    
    [Design Part]
    diameter = 96.8
    height = 0
    part 3d = "files/CATIA/Hole-flanged Part D95.8.CATpart"
    
    [Forming Tool]
    radius = 10
    
    [Elastic behaviour]
    poisson ratio = 0.3
    elasticity modulus = 70000
    
    [Plastic behaviour]
    strain-stress curve = 'files/AA7075O-Hollomon340n175.csv'
    # format: ((strain, stress in MPa))
    
    anisotropy coefficients = (1, 1, 1)
    # format: (r0, r45, r90)
    
    [Fracture behaviour]
    fracture curve = 'files/AA7075O-FFL.csv'
    # format: ((minor strain, major strain))
    
    [Strategy]
    step down = 0.2
    feedrate = 1000
    
    [NC Model]
    process 3d = 'files/CATIA/HF1-D58-R10.CATProcess'
    
    [NC Program]
    apt code = 'files/CATIA/HF1-D58-R10_Hole-Flanging_Tool_R10.aptsource'
    
    [Tool Trajectory]
    toolpath code = ('files/CATIA/toolpath-X.csv', 'files/CATIA/toolpath-Y.csv', 'files/CATIA/toolpath-Z.csv')
    
    [Simulation Model]
    analysis model = 'files/ABAQUS/model.py'
    
    [Simulation Results]
    analysis output = 'files/ABAQUS/model.odb'
    
    [Simulated Part]
    strain distribution = 
    fracture location = 
    
    [Simulation Issues]
    flange height = 0
    
    [Manufactured Part]
    failed = 
    fracture location = 
    height = 0
    diameter = 0
    photos = 
    
    [Analyzed Part]
    strain distribution = 
    thickness profile = 
    fractographies = 
    
    [Mahufacturing Issues]
    flange height = 0



## Service Layer

Scripts or batch files to execute the tasks using external software.

#### Example 1: A Python script `a11_t1_flange_height.py` to calculate the flange height:

    def flange_height(part_diameter, blank_hole_diameter):
        ''' A simple estimation for the final flange height of the design part '''
        return (part_diameter - blank_hole_diameter)/2

    def alternative_flange_height(part_diameter, blank_hole_diameter, simulated_flange_height):
        ''' A simple correction for the final flange height of the design part given the flange height obtained in the numerical simulation '''
        return simulated_flange_height


#### Example 2: A CATIA VBA script to update the flange height of the design part.

#### Example 3: A Python script to update the ABAQUS model and run the simulation.


## Interfaces

An `interfaces` directory that contains:

### `interfaces_data.py`

Python classes/functions to retrieve/save the instance data from/to `data.ini`.
A backup of `data.ini` is made as `data_<timestamp>.ini` before running a simulation.


### `interfaces_service.py`

Python functions to implement the Behaviour Model using the scripts/batch files in the `Service Layer`.

There is a function for each `Task` of the `Elementary Activities`.
The function structure is generated from the definition of the `Task`:

    def <task>(<input_1>, ...(<input_n>):
        ''' <rule> '''
        if <constraint>:
            <action>
        else:
            <another_action>
        return (<output_1>, ...<output_n>)

where `<action>` is a call to a script/batch file in `actions`.

    


## `run.py`

Python script to perform a MfM simulation from the command line. Usage:

    run.py --help
    run.py --instance instance01 --task a11t1

The argument `--help` shows the full list of Activities and Tasks and instructions for use. 

Before running a simulation it is required:

- All original external files must be stored in the directory `Data_Layer/files`
- A directory `Data_Layer/<instance_name>` with all instance data in a configuration file `data.ini`.

Before running the task, a backup copy of `data.ini` is made.


#### Example 1

    run.py --help

Output:

    usage: run.py [-h] [--instance INSTANCE] [--task TASK]

    MfM simulator: hole-flanging-by-SPIF-in-a-single-stage
    ------------------------------------------------------
    List of Activities and Tasks:

    A0 - Produce a hole flanged part by SPIF in a single stage
        A1 - Define NC Program
            A11 - Update Design Part
                T1 - Calculate Flange Height
                T2 - Generate CAD Model
            A12 - Generate NC
                T1 - Create NC Model
                T2 - Simulate NC Model
                T3 - Generate NC Code
        A2 - Simulate and Analyze SPIF Operation
            A21 - Extract Tool Trajectory
                T1 - Read next line
                T2 - Calculate time
                T3 - Write results
            A22 - Simulate SPIF Process
                T1 - Create Simulation Model
                T2 - Run Simulation Model
            A23 - Validate Simulation
                T1 - Check Fracture
                T2 - Check Finished Flange
            A24 - Analyze Simulation
                T1 - Extract strain distribution
                T2 - Find fracture location
        A3 - Inspect Manufactured Part
                T1 - Check Finished Flange
                T2 - Measure Strain Distribution
                T3 - Measure Thickness Profile
                T4 - Make Fractographies
    ------------------------------------------------------

    Example of usage:

        run.py --instance instance01 --task a11t1

    where 'instance01' is the directory that contains 'data.ini'

    optional arguments:
      -h, --help           show this help message and exit
      --instance INSTANCE  Directory name that contains 'data.ini'
      --task TASK          Task of an activity to be executed, example: --task a11t1



#### Example 2

    run.py --instance instance01 --task a11t1

Output:

    Executing A11 Update Design Part, T1 Calculate flange height
        Output: flange height = 19.400000 mm



#### Example 3

    run.py --instance instance01 --task a11t2

Output:

    Executing A21 Extract Tool Trajectory, T3 Write Results
        Output: toolpath_code = (toolpath-from.csv, toolpath-x.csv, toolpath-y.csv, toolpath-z.csv)




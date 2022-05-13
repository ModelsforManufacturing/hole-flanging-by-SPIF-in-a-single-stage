# MfM case study: hole flanging by SPIF in a single stage


## 3-Layer Model Overview

![](packages.png)


## Ontology Layer

See [Ontology_Layer/README.md](Ontology_Layer/README.md)

The following files are automatically generated from the model defined in the Ontology Layer:

- `interfaces/data_interface.py`
- `interfaces/behaviour_interface.py`
- `interfaces/mediating_controller.py`
- `Data_Layer/data.py`

## Interfaces

### `interfaces/data_interface.py`

Python interfaces with instructions for implementing the Data Model.


### `interfaces/behaviour_interface.py`

Python interfaces with instructions for implementing the Behaviour Model.

There is a interface for each `Task` of the `Elementary Activities`.
The interface structure is generated from the definition of the `Task` as:

    def <task>(
            <input_1>: type, 
            ...
            <input_n>: type
            ) -> output type:
        '''
        Comments section with instructions for implementing the interface:
        <rule>
        <input>
        <output>
        <constraint>
        '''
        pass

### `interfaces/mediating_controller.py`

The Behaviour Layer is completely decoupled from the Data Layer such that both can interact only via the mediating controller.


## Data Layer

### `Data_Layer/files`

Directory that contains all original complementary files required to perform the MfM simulation (CAD/CAM models, Finite Element models, tables with material properties, etc.).


### `Data_Layer/<instance_name>/data.ini`

Configuration file with all the instance data. 
Example of a configuration file:

    [Blank Model]
    thickness = 1.6
    hole diameter = 64.5
    
    [Part Model]
    diameter = 95.8
    flange height = 15.65
    
    [Forming Tool Model]
    radius = 6.0
    
    [Forming Conditions]
    feed rate = 1000.0
    step down = 0.2
    
    [Material Properties]
    fracture forming limit = files/fracture_forming_limit.csv
    
    [Tool Path]
    toolpath code = toolpath.csv
    
    [NC Program]
    g-code = nc-program.gcode
    
    [Specimen]
    is prepared = y
    
    [Test Results]
    non-dimensional flange height = 0.1931106471816284
    is fractured = n
    hole expansion ratio = 1.4852713178294574
    non-dimensional average thickness = 0.8459459459459459
    strain distribution = strain.csv
    flange height = 18.5
    
    [LFR]
    lfr per tool = 1.4852713178294574
    global lfr = 1.4852713178294574
    
    [FLD]
    fld per tool = FLD_R6.png
    fld for fractured tests = FLD_failed_tests.png
    fld for successful tests = FLD_successful_tests.png
    global fld = FLD_successful_tests.png
    
    [Technological Parameters]
    flange height diagram = diagram_HER-h.png
    average thickness diagram = diagram_HER-t.png
    
    [Conclusions]
    bending ratio = test
    flange height = test
    limit forming ratio = test
    average thickness = test


### `Data_Layer/data.py`

Implementation of `interfaces/data_interface.py` to retrieve/save the instance data from/to `Data_Layer/<instance_name>/data.ini`.

`data.ini` is backed up as `data_<timestamp>.ini` before running a simulation.


## Service Layer

### `Service_Layer/behaviour.py`

Implementation of `interfaces/behaviour_interface.py` that can call scripts or batch files to execute the tasks using external software. Examples:

1. A Python script to calculate the flange height
2. A CATIA VBA script to update the flange height of the design part. 
3. A Python script to update the ABAQUS model and run the simulation.


### `Service_Layer/visualization.py`

`Visualization` class with methods to display information of data instances.

### `Service_Layer/simulation.py`

`Simulation` class with methods to perform a MfM simulation from the command line.


## `main.py`

Python script to call `Service_Layer/simulation.py`.


## `main.ipynb`

Jupyter notebook to run `main.py` in the cloud via mybinder:

[![Binder](https://mybinder.org/badge_logo.svg)](
https://mybinder.org/v2/gh/ModelsforManufacturing/hole-flanging-by-SPIF-in-a-single-stage/HEAD?labpath=main.ipynb)


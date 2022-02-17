# MfM case study: hole flanging by SPIF in a single stage


## Service Layer

### `interfaces.py`

Functions to implement the Behaviour Model.

There is a function for each `Task` of the `Elementary Activities`.

Function definition in Python:

    def <task>(<input_1>, ...(<inputn_>):
        ''' <rule> '''
    
        ...
    
        return (<output_1>, ...<output_n>)


Example:



    def calculate_flange_height(blank_d, part_d, part_h, simul_issues_h):
        ''' Update the flange height according to an equation '''
        if !simul_issues_h or part_h == 0:
            part_h = (part_d - blank_d)/2
        else:
            part_h = simul_issues_h     # increase flange height
        return part_h
    

### `simulation.py`

Execute functions from `interfaces.py` to retrieve/save data from/to the Data Layer.

Example:

    import interfaces
    
    
    """
    Retrieve input data from the Data Layer.
    """
    datafile = 'example_01.ini'
    
    import configparser
    parser = configparser.SafeConfigParser()
    parser.read(datafile)
    
    blank_d = float(parser.get('Blank Sheet', 'hole diameter'))
    blank_t = float(parser.get('Raw Material', 'thickness'))
    part_d = float(parser.get('Design Part', 'diameter'))
    part_h = float(parser.get('Design Part', 'height'))
    part_tol = float(parser.get('Design Part', 'tolerance'))
    part_3d = string(parser.get('Design Part', '3d part'))
    tool_r = string(parser.get('Forming Tool', 'radius'))
    
    """
    Execute a task defined in 'interfaces'
    
    Activity: A11 Update Design Part
    Task: T1 Calculate flange height
    Rule: R1 Update the flange height according to an equation
    """
    part_h = interfaces.calculate_flange_height(blank_d, part_d, part_h, simul_issues_h)
    
    
    
    """
    Save output data to the Data Layer.
    Save all data to another file and trace life cycle of files.
    File name format: <instance_name>_A<activity_number>_T<task_number>.ini
    """
    datafile = 'example_01_A11_T1.ini'
    parser.write(datafile)




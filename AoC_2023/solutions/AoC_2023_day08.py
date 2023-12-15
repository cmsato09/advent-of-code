import re

input_file = 'input_files\AoC_2023_day08_input.txt'

def parse_data() -> str and dict:
    """ parses data from input file
    extracts step directions as a string
    converts node data into dictionary
    """

    with open(input_file, 'r') as input:
        data_string = input.read()
    lines = data_string.split('\n')

    step_sequence = lines[0]

    node_pattern = re.compile(r'(\w+) = \((\w+), (\w+)\)')
    network_dict = {match.group(1): (match.group(2), match.group(3)) for line in lines[1:] if (match := node_pattern.match(line))}

    return step_sequence, network_dict

def step_direction(direction: str, curr_node: tuple) -> str:
    """ takes direction L or R and returns the next node """
    if direction == 'L':
        next_node = curr_node[0]
    else:
        next_node = curr_node[1]
    return next_node

def reach_end(directions: str, network_node) -> int:
    """ counts how many steps it takes to reach 'ZZZ' from 'AAA' following a certain pattern of steps 
    """

    steps = 0
    current_node = 'AAA'
    
    while current_node != 'ZZZ':
        for LorR in directions:
            current_node = step_direction(LorR, network_node[current_node])
            steps += 1

    return steps

if __name__ == "__main__":
    steps, network = parse_data()
    print(reach_end(steps, network))
"""
Part 1 idea
find symbol, check if there is a number around it. If so, add it to a list of numbers to sum up in the end
"""
import string

schematic = []
input_file = 'input_files\AoC_2023_day03_input.txt'
with open(input_file, 'r') as input:
    for line in input:
        schematic.append(line)
print(schematic[0])

def checkvalue(line: str):
    """ finds symbol, checks if there's a number nearby """
    for char in line:
        if char != '.' and char in string.punctuation:
            

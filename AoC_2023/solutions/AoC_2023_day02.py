"""
Part 1 ideas
Read file, get game ID#, get number of cubes per subset, check if it exceeds limit, and add ID if it does.
"""
import re

input_file_path = 'AoC_2023\input_files\AoC_2023_day02_input.txt'

possible_bag = {
    "red" : 12,
    "green" : 13,
    "blue" : 14,
}

def possiblegame(line: str) -> int:
    game = re.split(r':|;', line)
    subsets = game[1:]
    for subgame in subsets:
        colors = [x.lstrip() for x in subgame.split(",")]
        for score in colors:
            x = score.split()
            if possible_bag[x[1]] < int(x[0]):
                return 0
    
    gameID = int(game[0].split()[1])
    
    return gameID

def findsumofpossiblegame():
    total = 0
    with open(input_file_path) as input:
        for line in input:
            val = possiblegame(line)
            total += val
    print(total)

def findminimumblocks(line: str):
    minimum_blocks = {
        "red" : 0,
        "blue" : 0,
        "green" : 0, 
    }

    game = re.split(r':|;', line)
    subsets = game[1:]
    for subgame in subsets:
        colors = [x.lstrip() for x in subgame.split(",")]
        for scores in colors:
            x = scores.split()
            if minimum_blocks[x[1]] < int(x[0]):
                minimum_blocks[x[1]] = int(x[0])
    power = 1
    for value in minimum_blocks.values():
        power *= value
    return power

def findpower():
    total = 0
    with open(input_file_path) as input:
        for line in input:
            val = findminimumblocks(line)
            total += val
    print(total)

if __name__ == "__main__":
    findsumofpossiblegame()
    findpower()
    

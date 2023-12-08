input_file = 'input_files\AoC_2023_day06_input.txt'

def wincondition(total_time: int, distance_to_beat: int):
    """ Part One soln """

    ways_to_win = 0
    
    for hold_time in range(1,total_time):
        if distance_to_beat < (hold_time * (total_time - hold_time)):
            ways_to_win += 1
    
    return ways_to_win

def multiplypoints():
    with open(input_file) as input:
        data = [line.split() for line in input]
    
    total_points = 1

    for data_val in range(1,len(data[0])):
        total_points *= wincondition(int(data[0][data_val]), int(data[1][data_val]))
    
    print(total_points)

def findminimumholdtime(total_time: int, distance_to_beat: int):
    for hold_time in range(1, total_time):
        if distance_to_beat < (hold_time * (total_time - hold_time)):
            print(total_time - hold_time*2 +1)
            break

if __name__ == "__main__":
    multiplypoints()
    findminimumholdtime(71530, 940200)
    findminimumholdtime(52947594, 426137412791216)
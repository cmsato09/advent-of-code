# Part 1 ideas 
# loop through each line to find first number and last number -- seems inefficient. 
# loop from the front to find first value, loop from the back to find last value

# if there is only 1 number, it acts as the first and last number
# e.g. treb7uchet only has a '7', so the calibration value is 77

def findFirstandLast(line: str) -> int:
    """ Part 1 soln """
    calibration_value = ""
    for char in line:
        if char.isdigit():
            calibration_value += char
            break
    
    for char in line[::-1]:
        if char.isdigit():
            calibration_value += char
            break

    return int(calibration_value)

def findcalibrationsum():
    """ Solves Part 1 of Advent of Code Day 1 """
    file_path = 'AoC_2023\input files\AoC_2023_day01_input.txt'
    total = 0
    with open(file_path) as input:
        for line in input:
            val = findFirstandLast(line)
            total += val
    print(total)

# Part 2 ideas
# use index and find lowest and highest index of digits that are spelled out
# can use .index() and .rindex()

def findFirstandLastletterdigit(line: str):
    digits = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
    }
    first_val = 0
    last_val = 0
    first_index = len(line)
    last_index = 0

    for letters in digits:
        if 0 <= line.find(letters) < first_index:
            first_index = line.index(letters)
            first_val = digits[letters]
        if 0 < line.rfind(letters) and line.rfind(letters) > last_index:
            last_index = line.rindex(letters)
            last_val = digits[letters]
    
    for index, char in enumerate(line):
        if char.isdigit():
            if index < first_index:
                first_index = index
                first_val = int(char)
            if index > last_index:
                last_index = index
                last_val = int(char)

    if last_val == 0:
        return first_val*10 + first_val
    else:
        return first_val*10 + last_val

def findcalibrationsum2():
    """ Solves Part 2 of Advent of Code Day 1 """
    file_path = 'AoC_2023\input files\AoC_2023_day01_input.txt'
    total = 0
    with open(file_path) as input:
        for line in input:
            val = findFirstandLastletterdigit(line)
            total += val
    print(total)


if __name__ == "__main__":
    findcalibrationsum()
    findcalibrationsum2()
    
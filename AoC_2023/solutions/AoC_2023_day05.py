input_file = open('AoC_2023\input_files\AoC_2023_day05_input.txt').read()

def num_conversion(source: int, map: list) -> int:
    for line in map:
        dest_range_start, source_range_start, range_len = line
        if source >= source_range_start and source <= source_range_start + range_len:
            return source - (source_range_start - dest_range_start)

    return source

def parse_data(input_lines):
    data = input_lines.splitlines()
    
    return [data[0], [[int(x) for x in line.split()] for line in data[1:]]]
    
def create_data_map(input):
    data_map = {}
    data_parts = input.split('\n\n')
    seeds = [int(x) for x in data_parts[0].split()[1:]]
    data_map['seeds:'] = seeds

    for map in data_parts[1:]:
        cleaned_data = parse_data(map)
        data_map[cleaned_data[0]] = cleaned_data[1]
    
    return data_map

def seednum_to_location():
    """ Part One Solution 
    converts seed number to location number
    """
    input_data_map = create_data_map(input_file)
    seed_map = input_data_map.pop('seeds:')
    final_location = seed_map
    
    for index in range(len(final_location)):
        for key, value in input_data_map.items():
            final_location[index] = num_conversion(final_location[index], value)
    
    print(min(final_location))

if __name__ == "__main__":
    seednum_to_location()
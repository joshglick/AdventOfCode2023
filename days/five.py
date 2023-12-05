from common.utils import parse_input_as_list_of_strings

DAY_FIVE_INPUT = 'input/five.txt'

def parse_file_input(lines):
    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    seeds = [int(num) for num in lines[0].split(':')[1].split(' ') if num != '']

    line_ctr = 3
    current_list = seed_to_soil

    while (line_ctr < len(lines)):
        current_line = lines[line_ctr]
        if current_line.strip() == '':
            current_list = None
        elif not current_line[0].isdigit():
            if current_line.startswith('soil-to-fertilizer'):
                current_list = soil_to_fertilizer
            elif current_line.startswith('fertilizer-to-water'):
                current_list = fertilizer_to_water
            elif current_line.startswith('water-to-light'):
                current_list = water_to_light
            elif current_line.startswith('light-to-temperature'):
                current_list = light_to_temperature
            elif current_line.startswith('temperature-to-humidity'):
                current_list = temperature_to_humidity
            elif current_line.startswith('humidity-to-location'):
                current_list = humidity_to_location
        else:
                current_list.append(current_line)
        line_ctr += 1

    for l in [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]:
        for i in range(0, len(l)):
            l[i] = [int(num) for num in l[i].split(' ') if num != '']

    return seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location

"""
Used for part 1 and anytime you need to map a single int to a almanac formatted map that contains a list of ranges
"""
def lookup_in_almanac(number, almanac):
    for row in almanac:
        source_start = row[1]
        dest_start = row[0]
        len_range = row[2]

        if source_start <= number <= source_start+len_range:
            return dest_start + (number-source_start)
    return number # no entry found return the original

def is_overlap(a_start, a_count, b_start, b_count):
    if a_start <= b_start <= a_start + a_count:
        return True
    if b_start <= a_start <= b_start+b_count:
        return True
    return False

"""
return a list of range pairs whos count is equal to the input but represents the mapping. 
almanac must be sorted by source start
"""
def lookup_range_in_almanac(start, count, almanac):
    lower_bound = start
    lower_bound_count = count
    result_ranges = []
    for row in almanac:
        source_start = row[1]
        dest_start = row[0]
        len_range = row[2]
        if is_overlap(lower_bound, lower_bound_count, source_start, len_range):
            if lower_bound < source_start:
                result_ranges.append([lower_bound, source_start-lower_bound])
                lower_bound_count = lower_bound_count - (source_start-lower_bound)
            # two cases here,
            overlap_count = lower_bound_count
            if lower_bound+lower_bound_count > source_start+len_range:
                overlap_count = len_range - (lower_bound-source_start)
            result_ranges.append([dest_start + (lower_bound-source_start), overlap_count])
            lower_bound = lower_bound+overlap_count
            lower_bound_count = lower_bound_count - overlap_count
            if lower_bound_count == 0:
                return result_ranges

    result_ranges.append([lower_bound, lower_bound_count]) #append any remaining map after the range lookups are done
    return result_ranges
            # first capture the part of lower bound not contained in this range







def part_one():
    data = parse_input_as_list_of_strings(DAY_FIVE_INPUT)
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = parse_file_input(data)

    min_location = -1

    for seed in seeds:
        soil = lookup_in_almanac(seed, seed_to_soil)
        fertilizer = lookup_in_almanac(soil, soil_to_fertilizer)
        water = lookup_in_almanac(fertilizer, fertilizer_to_water)
        light = lookup_in_almanac(water, water_to_light)
        temperature = lookup_in_almanac(light, light_to_temperature)
        humidity = lookup_in_almanac(temperature, temperature_to_humidity)
        location = lookup_in_almanac(humidity, humidity_to_location)
        if min_location < 0:
            min_location = location
        else:
            min_location = min(min_location, location)

    return min_location




def part_two():
    data = parse_input_as_list_of_strings(DAY_FIVE_INPUT)
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = parse_file_input(data)

    for l in [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]:
        l.sort(key= lambda x: x[1])


    seed_pairs = []
    for i in range(0, len(seeds), 2):
        seed_pairs.append([seeds[i], seeds[i+1]])

    seeds = seed_pairs
    min_location = -1

    for seed in seeds:
        soils = lookup_range_in_almanac(seed[0], seed[1], seed_to_soil)
        for soil in soils:
            fertilizers = lookup_range_in_almanac(soil[0], soil[1], soil_to_fertilizer)
            for f in fertilizers:
                water = lookup_range_in_almanac(f[0], f[1], fertilizer_to_water)
                for w in water:
                    light = lookup_range_in_almanac(w[0], w[1], water_to_light)
                    for l in light:
                        temperature = lookup_range_in_almanac(l[0], l[1], light_to_temperature)
                        for t in temperature:
                            humidity = lookup_range_in_almanac(t[0], t[1], temperature_to_humidity)
                            for h in humidity:
                                location = lookup_range_in_almanac(h[0], h[1], humidity_to_location)
                                for location_range in location:
                                    if min_location < 0:
                                        min_location = location_range[0]
                                    else:
                                        min_location = min(min_location, location_range[0])

    return min_location







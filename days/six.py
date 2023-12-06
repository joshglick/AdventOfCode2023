from common.utils import parse_input_as_list_of_strings

DAY_SIX_INPUT = 'input/six.txt'

MAX_INT = 999999999
MIN_INT = -99999999

def distance(total, time_held):
    return (total-time_held) * time_held


"""
We could write a recursive function but easy enough to iteratively approach the problem of doing the binary searches
"""
def find_min_and_max_hold_times(total_time, record_distance):
    # find a starting mid point
    mid_point = int(total_time/2)
    while distance(total_time, mid_point) <= record_distance:
        mid_point = int((total_time+mid_point)/2)

    # find min pont

    # first jump to half of the remaining distance
    min_point = mid_point
    next_jump = int((0+min_point)/2)

    while next_jump != min_point:
        if distance(total_time, next_jump) > record_distance:
            min_point = next_jump
            next_jump = int(min_point/2)
        else:
            if min_point-next_jump <= 1: # because we only are dealing with ints this means we found our exit case
                next_jump = min_point
            else:
                next_jump = int((min_point+next_jump)/2)

    # find max point

    # first jump to half of the remaining distance
    max_point = mid_point
    next_jump = int((total_time+max_point)/2)

    while next_jump != max_point:
        if distance(total_time, next_jump) > record_distance:
            max_point = next_jump
            next_jump = int((max_point+total_time)/2)
        else:
            if next_jump-max_point <= 1: # because we only are dealing with ints this means we found our exit case
                next_jump = max_point
            else:
                next_jump = int((max_point+next_jump)/2)

    return min_point, max_point





def part_one():
    data = parse_input_as_list_of_strings(DAY_SIX_INPUT)

    times = [int(n) for n in data[0].split(':')[1].strip().split(' ') if n.isdigit()]
    distances = [int(n) for n in data[1].split(':')[1].strip().split(' ') if n.isdigit()]

    total = 1

    x, y = find_min_and_max_hold_times(15, 40)


    for i in range(0, len(times)):
        min, max = find_min_and_max_hold_times(times[i], distances[i])
        winning_range = max-min+1
        total *= winning_range

    return total






def part_two():
    data = parse_input_as_list_of_strings(DAY_SIX_INPUT)

    time = int(''.join([str(n) for n in data[0].split(':')[1].strip().split(' ') if n.isdigit()]))
    dist = int(''.join([str(n) for n in data[1].split(':')[1].strip().split(' ') if n.isdigit()]))
    min, max = find_min_and_max_hold_times(time, dist)

    return (max-min+1)









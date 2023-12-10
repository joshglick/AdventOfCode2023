from common.utils import parse_input_as_list_of_ints


DAY_NINE_INPUT = 'input/nine.txt'
DAY_NINE_SAMPLE_INPUT = 'input/nine.sample.txt'


""" 
a simple recursive function to find the next value in the current step
"""
def find_next_value(num_list):
    if all([n == 0 for n in num_list]):
        return 0
    else:
        next_list = []
        for i in range(1, len(num_list)):
            next_list.append(num_list[i]-num_list[i-1])
        return num_list[-1] + find_next_value(next_list)

""" 
a simple recursive function to find the next value in the current step
"""
def find_prev_value(num_list):
    if all([n == 0 for n in num_list]):
        return 0
    else:
        next_list = []
        for i in range(1, len(num_list)):
            next_list.append(num_list[i]-num_list[i-1])
        return num_list[-0] - find_prev_value(next_list)



def part_one():
    data = parse_input_as_list_of_ints(DAY_NINE_INPUT)
    sum = 0
    for sequence in data:
        sum += find_next_value(sequence)

    return sum

def part_two():
    data = parse_input_as_list_of_ints(DAY_NINE_INPUT)
    sum = 0
    for sequence in data:
        sum += find_prev_value(sequence)

    return sum

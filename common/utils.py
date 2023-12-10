import time

# I stole this from Matt Hodges (https://github.com/hodgesmr/aoc_2023/tree/main)
def timed(func, args):
    t_start = time.perf_counter()
    result = func(*args)
    t_end = time.perf_counter()
    print(f"{func.__name__} : {result} ({(t_end * 1000 - t_start * 1000):0.4f}ms)")

def parse_input_as_lines_of_chars(filename):
    parsed = []
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()

        for line in lines:
            parsed.append([char for char in line.strip()])

    return parsed

def parse_input_as_list_of_strings(filename):
    parsed = []
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()

        for line in lines:
            parsed.append(line.strip())

    return parsed

def parse_input_as_list_of_ints(filename):
    parsed = []
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()

        for line in lines:
            parsed.append([int(n) for n in line.strip().split(' ')])

    return parsed

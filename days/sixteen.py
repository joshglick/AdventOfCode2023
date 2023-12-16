from functools import cache

from common.utils import parse_input_as_lines_of_chars


INPUT = 'input/sixteen.txt'
SAMPLE_INPUT = 'input/sixteen.sample.txt'

NORTH=0
WEST=1
EAST=2
SOUTH=3

def next_point(p, direction):

    if direction == NORTH:
        return (p[0]-1, p[1])
    elif direction == SOUTH:
        return (p[0]+1, p[1])
    elif direction == WEST:
        return (p[0], p[1]-1)
    elif direction == EAST:
        return (p[0], p[1]+1)


def energize(starting_point, direction, grid, energized_set, beams):
    # to defeat recursion limit, if we have a beam at this starting point and direction already return
    if (starting_point, direction) in beams:
        return
    beams.add((starting_point, direction))

    energized_set.add(starting_point)
    next = next_point(starting_point, direction)
    continue_beam = True
    while continue_beam:
        if (next[0] < 0 or next[0] >= len(grid)) or (next[1] < 0 or next[1] >= len(grid[0])):
            # we are out of bounds, return
            return
        if grid[next[0]][next[1]] == '|':
            if direction == EAST or direction == WEST:
                energize(next, NORTH, grid, energized_set, beams)
                energize(next, SOUTH, grid, energized_set, beams)
                return
        elif grid[next[0]][next[1]] == '-':
            if direction == NORTH or direction == SOUTH:
                energize(next, WEST, grid, energized_set, beams)
                energize(next, EAST, grid, energized_set, beams)
                return
        elif grid[next[0]][next[1]] == '/':
            if direction == NORTH:
                energize(next, EAST, grid, energized_set, beams)
                return
            elif direction == SOUTH:
                energize(next, WEST, grid, energized_set, beams)
                return
            elif direction == WEST:
                energize(next, SOUTH, grid, energized_set, beams)
                return
            elif direction == EAST:
                energize(next, NORTH, grid, energized_set, beams)
                return
        elif grid[next[0]][next[1]] == '\\':
            if direction == NORTH:
                energize(next, WEST, grid, energized_set, beams)
                return
            elif direction == SOUTH:
                energize(next, EAST, grid, energized_set, beams)
                return
            elif direction == WEST:
                energize(next, NORTH, grid, energized_set, beams)
                return
            elif direction == EAST:
                energize(next, SOUTH, grid, energized_set, beams)
                return
        energized_set.add(next)
        next = next_point(next, direction)



def part_one():
    data = parse_input_as_lines_of_chars(INPUT)
    # the top left corner can be something other than a dot... this kinda messes up energize so lets "fix" it
    for i in range(0, len(data)):
        data[i] = ['.'] + data[i]

    energized_set = set()
    beams = set()
    energize((0,0), EAST, data, energized_set, beams)

    for i in range(0, len(data)):
        energized_set.discard((i, 0))

    return len(energized_set)

def discard_edges(data, energized_set):
    for i in range(0, len(data)):
        energized_set.discard((i, 0))
        energized_set.discard((i, len(data)-1))

    for i in range(0, len(data[0])):
        energized_set.discard((0, i))
        energized_set.discard((len(data)-1, i))

def part_two():
    data = parse_input_as_lines_of_chars(INPUT)
    # the top left corner can be something other than a dot... this kinda messes up energize so lets "fix" it
    for i in range(0, len(data)):
        data[i] = ['.'] + data[i] + ['.']

    data.insert(0, ['.']*len(data[0]))
    data.append(['.']*len(data[0]))

    max_energized = 0
    for i in range(0, len(data)):
        energized_set = set()
        beams = set()
        energize((i, 0), EAST, data, energized_set, beams)
        discard_edges(data, energized_set)
        max_energized = max(max_energized, len(energized_set))

    for i in range(0, len(data)):
        energized_set = set()
        beams = set()
        energize((i, len(data[0])-1), WEST, data, energized_set, beams)
        discard_edges(data, energized_set)
        max_energized = max(max_energized, len(energized_set))

    for i in range(0, len(data[0])):
        energized_set = set()
        beams = set()
        energize((0, i), SOUTH, data, energized_set, beams)
        discard_edges(data, energized_set)
        max_energized = max(max_energized, len(energized_set))

    for i in range(0, len(data[0])):
        energized_set = set()
        beams = set()
        energize((len(data)-1, i), NORTH, data, energized_set, beams)
        discard_edges(data, energized_set)
        max_energized = max(max_energized, len(energized_set))

    return max_energized










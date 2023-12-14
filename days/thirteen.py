import re
from functools import cache

from common.utils import parse_input_as_list_of_strings


INPUT = 'input/thirteen.txt'
SAMPLE_INPUT = 'input/thirteen.sample.txt'

def horizontal_reflection(galaxy, index=1):
    if index == len(galaxy):
        return -1
    else:
        top = galaxy[0:index]
        bottom = galaxy[index:]
        top_index = index-1
        bottom_index = 0
        while top_index >= 0 and bottom_index < len(bottom):
            if top[top_index] != bottom[bottom_index]:
                return horizontal_reflection(galaxy, index+1)
            top_index -= 1
            bottom_index += 1

        return len(top)

def transpose_galaxy(galaxy):
    new_galaxy = []

    for j in range(0, len(galaxy[0])):
        new_galaxy.append('')
        for i in range(0, len(galaxy)):
            new_galaxy[j] += galaxy[i][j]

    return new_galaxy

@cache
def diffs(s1, s2):
    diffs = 0
    if len(s1) != len(s2):
        raise Exception("Need to be equal length")
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            diffs += 1

    return diffs

def horizontal_reflection_with_error(galaxy, index=1):
    if index == len(galaxy):
        return -1
    else:
        num_errors = 0
        top = galaxy[0:index]
        bottom = galaxy[index:]
        top_index = index-1
        bottom_index = 0
        while top_index >= 0 and bottom_index < len(bottom):
            if top[top_index] != bottom[bottom_index]:
                delta = diffs(top[top_index], bottom[bottom_index])
                num_errors = delta
                if num_errors > 1:
                    return horizontal_reflection_with_error(galaxy, index+1)
            top_index -= 1
            bottom_index += 1

        if num_errors == 0:
            return horizontal_reflection_with_error(galaxy, index+1)

        return len(top) #else it must be 1 because of other checks

def part_one():
    data = parse_input_as_list_of_strings(INPUT)

    galaxies = []
    galaxy = []
    for d in data:
        if d == '':
            galaxies.append(galaxy)
            galaxy = []
        else:
            galaxy.append(d)

    galaxies.append(galaxy)

    sum = 0

    for g in galaxies:
        reflection = horizontal_reflection(transpose_galaxy(g))
        if reflection < 0:
            reflection = horizontal_reflection(g) * 100
            if reflection < 0:
                raise Exception
        sum += reflection

    return sum

def part_two():
    data = parse_input_as_list_of_strings(INPUT)

    galaxies = []
    galaxy = []
    for d in data:
        if d == '':
            galaxies.append(galaxy)
            galaxy = []
        else:
            galaxy.append(d)

    galaxies.append(galaxy)

    sum = 0

    for g in galaxies:
        reflection = horizontal_reflection_with_error(transpose_galaxy(g))
        if reflection < 0:
            reflection = horizontal_reflection_with_error(g) * 100
            if reflection < 0:
                raise Exception
        sum += reflection

    return sum


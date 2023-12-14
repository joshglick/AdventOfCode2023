import re
from functools import cache

from common.utils import parse_input_as_lines_of_chars


INPUT = 'input/fourteen.txt'
SAMPLE_INPUT = 'input/fourteen.sample.txt'

EMPTY = '.'
ROCK = 'O'

NORTH=0
WEST=1
EAST=2
SOUTH=3

def swap2d(l, p1, p2):
    tmp = l[p1[0]][p1[1]]
    l[p1[0]][p1[1]] = l[p2[0]][p2[1]]
    l[p2[0]][p2[1]] = tmp



def part_one():
    data = parse_input_as_lines_of_chars(INPUT)

    for j in range(0, len(data[0])):
        for i in range(0, len(data)):
            if data[i][j] == ROCK:
                current = (i, j)
                above = (i-1, j)
                while above[0] >= 0 and data[above[0]][above[1]] == EMPTY:
                    swap2d(data, current, above)
                    current = above
                    above = (current[0]-1, current[1])

    sum = 0
    for i in range(0, len(data)):
        weight = len(data)- i
        for j in range(0, len(data[0])):
            if data[i][j] == ROCK:
                sum += weight

    return sum

"""
Making this hashable so I can abuse python cache
"""
def data_to_string(data):
    output = ''
    for row in data:
        row_string = ''.join(row)
        output+=row_string+"|"

    return output[0:-1] #strip last |

def string_to_data(string):
    data = []
    split = string.split('|')
    for s in split:
        data.append([c for c in s])

    return data

"""
The pattern will naturally repeat so instead of tracking results and finding where it loops, lets just cache it and make 1 billion cache hits :)

I think the correct way to do this efficiently is to figure out when the pattern repeats (after rotation n it is always same as n-m) 
then use that to skip to as close to 1 billion as m is a multiple of. Then just do the diff rotations. But that sounds like it'd require a little more 
trial and error from me. So if the cache finishes in under a few minutes without memory issues it might be the play for today. 
"""
@cache
def rotate(dish_string, direction=NORTH):
    data = string_to_data(dish_string)

    if direction == NORTH:
        for j in range(0, len(data[0])):
            for i in range(0, len(data)):
                if data[i][j] == ROCK:
                    current = (i, j)
                    prev = (i - 1, j)
                    while prev[0] >= 0 and data[prev[0]][prev[1]] == EMPTY:
                        swap2d(data, current, prev)
                        current = prev
                        prev = (current[0] - 1, current[1])
    elif direction == SOUTH:
        for j in range(0, len(data[0])):
            for i in range(len(data)-1, -1, -1):
                if data[i][j] == ROCK:
                    current = (i, j)
                    prev = (i + 1, j)
                    while prev[0] < len(data) and data[prev[0]][prev[1]] == EMPTY:
                        swap2d(data, current, prev)
                        current = prev
                        prev = (current[0] + 1, current[1])
    elif direction == WEST:
        for i in range(0, len(data)):
            for j in range(0, len(data[0])):
                if data[i][j] == ROCK:
                    current = (i, j)
                    prev = (i, j-1)
                    while prev[1] >= 0 and data[prev[0]][prev[1]] == EMPTY:
                        swap2d(data, current, prev)
                        current = prev
                        prev = (current[0], current[1]-1)
    elif direction == EAST:
        for i in range(0, len(data)):
            for j in range(len(data[0])-1, -1, -1):
                if data[i][j] == ROCK:
                    current = (i, j)
                    prev = (i, j+1)
                    while prev[1] < len(data[i]) and data[prev[0]][prev[1]] == EMPTY:
                        swap2d(data, current, prev)
                        current = prev
                        prev = (current[0], current[1]+1)



    return data_to_string(data)

@cache
def weight(dish_string):
    data = string_to_data(dish_string)
    sum = 0
    for i in range(0, len(data)):
        weight = len(data)- i
        for j in range(0, len(data[0])):
            if data[i][j] == ROCK:
                sum += weight
    return sum

def part_two():
    data = parse_input_as_lines_of_chars(INPUT)
    s = data_to_string(data)
    i = 0
    while i < 1000000000:
        s = rotate(s, NORTH)
        s = rotate(s, WEST)
        s = rotate(s, SOUTH)
        s = rotate(s, EAST)
        i+=1

    return weight(s)





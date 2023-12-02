from common.utils import parse_input_as_list_of_strings

DAY_TWO_INPUT = 'input/two.txt'

COLOR_RED = 'red'
COLOR_BLUE = 'blue'
COLOR_GREEN = 'green'

"""
Takes input as the string a la 'Game 1: 8 green; 5 green, 6 blue, 1 red; 2 green, 1 blue, 4 red; 10 green, 1 red, 2 blue; 2 blue, 3 red'
and return a dictionary with each colors minimum values
"""
def parse_game_min_cubes(game_string):
    bag_min = {
        COLOR_GREEN:0,
        COLOR_BLUE:0,
        COLOR_RED:0
    }

    game = game_string.split(':')
    game_weight = int(game[0].split(' ')[1].strip())
    pulls = game[1]
    for pull in pulls.split(';'):
        for count_color in pull.split(','): #['1 green', '2 red']
            cubes = count_color.strip().split(' ') #['1', 'green']
            count = int(cubes[0])
            color = cubes[1]
            if bag_min[color] < count:
                bag_min[color] = count

    return game_weight, bag_min

def part_one():
    data = parse_input_as_list_of_strings(DAY_TWO_INPUT)
    sum = 0
    for game in data:
        game_weight, bag_min = parse_game_min_cubes(game)
        if bag_min[COLOR_RED] <= 12 and bag_min[COLOR_GREEN] <= 13 and bag_min[COLOR_BLUE] <= 14:
            sum += game_weight

    return sum


def part_two():
    data = parse_input_as_list_of_strings(DAY_TWO_INPUT)
    sum = 0
    for game in data:
        _, bag_min = parse_game_min_cubes(game)
        sum += bag_min[COLOR_GREEN]*bag_min[COLOR_BLUE]*bag_min[COLOR_RED]

    return sum

from common.utils import parse_input_as_lines_of_chars

DAY_ONE_INPUT = 'input/one.txt'

def part_one():
    data = parse_input_as_lines_of_chars(DAY_ONE_INPUT)
    sum = 0
    for line in data:
        first_digit_found = False
        last_digit = None
        for c in line:
            if c.isdigit():
                last_digit = int(c)
            if last_digit and not first_digit_found:
                first_digit_found = True
                sum += 10 * last_digit

        sum += last_digit

    return sum


def part_two():
    data = parse_input_as_lines_of_chars(DAY_ONE_INPUT)
    sum = 0
    token_map = {
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
    }
    for line in data:
        first_digit_found = False
        last_digit = None
        token = ''
        for c in line:
            if c.isdigit():
                token = ''
                last_digit = int(c)
            else:
                token += c
                for token_key in token_map.keys():
                    if token_key in token:
                        last_digit = token_map[token_key]
                        token = token[-2:] #I AM THE DUMBEST MAN ALIVE THIS IS THE SHORTEST TOKEN THAT COULD BE PART OF THE NEXT WORD

            if last_digit and not first_digit_found:
                first_digit_found = True
                sum += 10 * last_digit

        sum += last_digit

    return sum

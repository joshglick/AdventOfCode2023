import re
from functools import cache

from common.utils import parse_input_as_list_of_strings


INPUT = 'input/twelve.txt'
SAMPLE_INPUT = 'input/twelve.sample.txt'

BROKEN = '#'
UNKNOWN = '@'
OPERATIONAL = '&'


@cache
def build_match(num_list):
    match = '^'+ OPERATIONAL + '*'
    for i in range(0, len(num_list)-1):
        match += BROKEN*num_list[i]
        match += OPERATIONAL + '+'

    match += BROKEN*num_list[-1] + OPERATIONAL + '*$'

    return match

# using this for part 2 where we need to have this between strings. It worked for sample, maybe didn't generalize wellex
@cache
def build_match_with_leading_operational(num_list):
    match = '^'+ OPERATIONAL + '+'
    for i in range(0, len(num_list)-1):
        match += BROKEN*num_list[i]
        match += OPERATIONAL + '+'

    match += BROKEN*num_list[-1] + OPERATIONAL + '*$'

    return match

#this worked great for the sample input, but the way i split the problem didn't genralize to the full input, leaving for posterity
@cache
def simple_case(string, vals):
    count = 0
    matcher = build_match_with_leading_operational(vals)

    all_strings = [string]
    first_wild = all_strings[0].find(UNKNOWN)  # return -1 on no match
    while first_wild >= 0:
        working_strings = all_strings.copy()
        broken_strings = all_strings.copy()
        for i in range(0, len(working_strings)):
            working_strings[i] = working_strings[i][:first_wild] + OPERATIONAL + working_strings[i][first_wild + 1:]
            broken_strings[i] = broken_strings[i][:first_wild] + BROKEN + broken_strings[i][first_wild + 1:]
        all_strings = working_strings + broken_strings
        first_wild = all_strings[0].find(UNKNOWN)  # return -1 on no match

    for s in all_strings:
        if bool(re.match(matcher, s)):
            count += 1

    return count


def part_one():
    data = parse_input_as_list_of_strings(INPUT)
    cleaned_input = []
    for line in data:
        split = line.split(' ')
        # change char to make regex easier
        cleaned_input.append((split[0].replace('.', OPERATIONAL).replace('?', UNKNOWN), [int(n) for n in split[1].split(',')]))
    count = 0
    for input in cleaned_input:
        matcher = build_match(input[1])
        all_strings = [input[0]]

        first_wild = all_strings[0].find(UNKNOWN) # return -1 on no match
        while first_wild >= 0:
            working_strings = all_strings.copy()
            broken_strings = all_strings.copy()
            for i in range(0, len(working_strings)):
                working_strings[i] = working_strings[i][:first_wild] + OPERATIONAL + working_strings[i][first_wild + 1:]
                broken_strings[i] = broken_strings[i][:first_wild] + BROKEN + broken_strings[i][first_wild + 1:]
            all_strings = working_strings+broken_strings
            first_wild = all_strings[0].find(UNKNOWN)  # return -1 on no match


        for s in all_strings:
            if bool(re.match(matcher, s)):
                count += 1

    return count



def num_combinations(map_string, vals, s_index=0, v_index=0, broken_length=0):
    og_string = map_string
    og_vals = vals
    try:
        total = 1
        while '#' in map_string :
            s_index = 0
            while map_string[s_index] != BROKEN:
                s_index += 1

            broken_count = 0
            while s_index < len(map_string) and map_string[s_index] == BROKEN:
                s_index += 1
                broken_count+=1

            subproblem_string = map_string[0:s_index]
            while len(vals) > 0 and broken_count not in vals:
                broken_count += 1 # increase this until we find smallest size that fits our string
            v_index = vals.index(broken_count)+1
            subproblem_vals = vals[0:v_index]
            map_string = map_string[s_index:]
            vals = vals[v_index:]

            while (len(subproblem_string) < sum(subproblem_vals)+len(subproblem_vals) or subproblem_string[-1] != '#')  and len(map_string) > 0: # need to add 1 for each OPERATIONAL required
                subproblem_string = subproblem_string+ map_string[0]
                map_string = map_string[1:]

            print(f'{subproblem_string}, {subproblem_vals}')
            unique_ways = simple_case(subproblem_string, tuple(subproblem_vals)) # cast to tuple so we can cache results
            print(f'{subproblem_string}, {subproblem_vals}: {unique_ways}')
            total *= unique_ways

        if len(map_string) > 0 and len(vals) > 0:
            total *= simple_case(map_string, tuple(vals)) # whatever is left over
            print(f'{map_string}, {vals}: {simple_case(map_string, tuple(vals))}')


        return total
    except:
        return simple_case(og_string, tuple(og_vals))


def part_two():
    data = parse_input_as_list_of_strings(SAMPLE_INPUT)
    cleaned_input = []
    for line in data:
        split = line.split(' ')
        # change char to make regex easier
        cleaned_input.append((((split[0].replace('.', OPERATIONAL).replace('?', UNKNOWN)+UNKNOWN)*5)[:-1], [int(n) for n in split[1].split(',')]*5))
    count = 0
    for input in cleaned_input:
        # we can pad the first string with an operational without changing anything and then we can enforce each split string must start with operational
        count += num_combinations(OPERATIONAL+input[0], input[1])

    return count



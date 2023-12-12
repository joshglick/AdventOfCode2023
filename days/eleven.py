from common.utils import parse_input_as_lines_of_chars


INPUT = 'input/eleven.txt'
SAMPLE_INPUT = 'input/eleven.sample.txt'

def expand_universe(universe):
    empty_rows = []
    i = 0
    for row in universe:
        if all([c == '.' for c in row]):
            empty_rows.append(i)
        i+=1

    for i in range(0, len(empty_rows)):
        universe.insert(empty_rows[i], universe[empty_rows[i]].copy()) # need copy here because otherwise when i modify in col below it gets modded twice
        for j in range(i+1, len(empty_rows)):
            empty_rows[j] = empty_rows[j]+1 # we just inserted a new row so increment our stored values

    empty_cols = []
    for j in range(0, len(universe[0])):
        empty = True
        for i in range(0, len(universe)):
            if universe[i][j] == '#':
                empty = False
        if empty:
            empty_cols.append(j)

    for z in range(0, len(empty_cols)):
        for row in range(0, len(universe)):
            universe[row].insert(empty_cols[z], '.')

        for k in range(z+1, len(empty_cols)):
            empty_cols[k] = empty_cols[k]+1 # we just inserted a new row so increment our stored values

    return universe

def empty_spaces(universe):
    empty_rows = []
    i = 0
    for row in universe:
        if all([c == '.' for c in row]):
            empty_rows.append(i)
        i+=1

    empty_cols = []
    for j in range(0, len(universe[0])):
        empty = True
        for i in range(0, len(universe)):
            if universe[i][j] == '#':
                empty = False
        if empty:
            empty_cols.append(j)

    return empty_rows, empty_cols



def part_one():
    data = parse_input_as_lines_of_chars(INPUT)
    eu = expand_universe(data)
    galaxies = []
    sum = 0
    for i in range(0, len(eu)):
        for j in range(0, len(eu[0])):
            if eu[i][j] == '#':
                galaxies.append((i, j))

    for k in range(0, len(galaxies)):
        for l in range(k+1, len(galaxies)):
            distance = abs(galaxies[k][0] - galaxies[l][0]) + abs(galaxies[k][1] - galaxies[l][1])
            sum += distance

    return sum


def part_two():
    data = parse_input_as_lines_of_chars(INPUT)
    UNIVERSE_MODIFIER = 1000000
    galaxies = []
    sum = 0
    empty_rows, empty_cols = empty_spaces(data)
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if data[i][j] == '#':
                galaxies.append((i, j))

    mod_gal = []
    for galaxy in galaxies:
        original = galaxy
        mod_i = galaxy[0]
        mod_j = galaxy[1]
        for row in empty_rows:
            if original[0] > row:
                mod_i += UNIVERSE_MODIFIER-1
        for col in empty_cols:
            if original[1] > col:
                mod_j += UNIVERSE_MODIFIER-1
        mod_gal.append((mod_i, mod_j))

    for k in range(0, len(mod_gal)):
        for l in range(k+1, len(mod_gal)):
            distance = abs(mod_gal[k][0] - mod_gal[l][0]) + abs(mod_gal[k][1] - mod_gal[l][1])
            sum += distance



    return sum


from common.utils import parse_input_as_lines_of_chars


DAY_TEN_INPUT = 'input/ten.txt'
DAY_TEN_SAMPLE_INPUT = 'input/ten.sample.txt'

class Pipe:
    map = []

    def __init__(self, pos, last_pos):
        self.pos = pos
        self.last_pos = last_pos

    def next_pos(self):
        raise Exception("Unimplemented")

    def valid(self):
        # a few common ways to be invalid if for either your last_pos or next_pos to be '.' or be out of bounds
        if self.last_pos[0] < 0 or self.last_pos[0] >= len(type(self).map):
            return False
        if self.next_pos()[0] < 0 or self.next_pos()[0] >= len(type(self).map):
            return False

        if self.last_pos[1] < 0 or self.last_pos[1] >= len(type(self).map[0]):
            return False
        if self.next_pos()[1] < 0 or self.next_pos()[1] >= len(type(self).map[0]):
            return False

        if type(self).map[self.last_pos[0]][self.last_pos[1]] == '.':
            return False
        if type(self).map[self.next_pos()[0]][self.next_pos()[1]] == '.':
            return False

        return True

class VerticalPipe(Pipe):

    def next_pos(self):
        if self.pos[0] < self.last_pos[0]:
            return (self.pos[0]-1, self.pos[1])
        return (self.pos[0]+1, self.pos[1])

    def invalid_next(self):
        if self.pos[0] < self.last_pos[0]:
            return ['-', 'L', 'J'] # moving from south to north
        return ['-', 'F', '7']

    def valid(self):
        base = super().valid()
        if base: # this makes sure we've already checked out of bounds
            return type(self).map[self.next_pos()[0]][self.next_pos()[1]] not in self.invalid_next()
        return base

class HorizontalPipe(Pipe):

    def next_pos(self):
        if self.pos[1] < self.last_pos[1]:
            return (self.pos[0], self.pos[1]-1)
        return (self.pos[0], self.pos[1]+1)

    def invalid_next(self):
        if self.pos[1] < self.last_pos[1]:
            return ['|', '7', 'J'] # moving from east to west
        return ['|', 'L', 'F']

    def valid(self):
        base = super().valid()
        if base: # this makes sure we've already checked out of bounds
            return type(self).map[self.next_pos()[0]][self.next_pos()[1]] not in self.invalid_next()
        return base

class LPipe(Pipe):

    def next_pos(self):
        if self.pos[0] > self.last_pos[0]: # if last pipe north
            return (self.pos[0], self.pos[1]+1) #east
        return (self.pos[0]-1, self.pos[1]) #else last pipe was east so return north

    def invalid_next(self):
        if self.pos[0] > self.last_pos[0]: # if last pipe north
            return ['|', 'F', 'L'] # connecting to an east pipe so it should be horizontal, or accept from west
        return ['-', 'L', 'J'] # connecting to a north pipe should be vertical or accept from south

    def valid(self):
        base = super().valid()
        if base: # this makes sure we've already checked out of bounds
            return type(self).map[self.next_pos()[0]][self.next_pos()[1]] not in self.invalid_next()
        return base

class JPipe(Pipe):

    def next_pos(self):
        if self.pos[0] > self.last_pos[0]: # if last pipe north
            return (self.pos[0], self.pos[1]-1) #west
        return (self.pos[0]-1, self.pos[1]) #else last pipe was west so return north

    def invalid_next(self):
        if self.pos[0] > self.last_pos[0]: # if last pipe north
            return ['|', 'J', '7'] # connecting to a west pipe so it should be horizontal, or accept from east
        return ['-', 'L', 'J'] # connecting to a north pipe should be vertical or accept from south

    def valid(self):
        base = super().valid()
        if base: # this makes sure we've already checked out of bounds
            return type(self).map[self.next_pos()[0]][self.next_pos()[1]] not in self.invalid_next()
        return base

class SevenPipe(Pipe):

    def next_pos(self):
        if self.pos[0] < self.last_pos[0]: # if last pipe south
            return (self.pos[0], self.pos[1]-1) #west
        return (self.pos[0]+1, self.pos[1]) #else last pipe was west so return south

    def invalid_next(self):
        if self.pos[0] < self.last_pos[0]: # if last pipe south
            return ['|', 'J', '7'] # connecting to a west pipe so it should be horizontal, or accept from east
        return ['-', '7', 'F'] # connecting to a south pipe should be vertical or accept from north

    def valid(self):
        base = super().valid()
        if base: # this makes sure we've already checked out of bounds
            return type(self).map[self.next_pos()[0]][self.next_pos()[1]] not in self.invalid_next()
        return base

class FPipe(Pipe):

    def next_pos(self):
        if self.pos[0] < self.last_pos[0]: # if last pipe south
            return (self.pos[0], self.pos[1]+1) #east
        return (self.pos[0]+1, self.pos[1]) #else last pipe was east so return south

    def invalid_next(self):
        if self.pos[0] < self.last_pos[0]: # if last pipe south
            return ['|', 'F', 'L'] # connecting to an east pipe so it should be horizontal, or accept from west
        return ['-', '7', 'F'] # connecting to a south pipe should be vertical or accept from north

    def valid(self):
        base = super().valid()
        if base: # this makes sure we've already checked out of bounds
            return type(self).map[self.next_pos()[0]][self.next_pos()[1]] not in self.invalid_next()
        return base




def part_one():
    data = parse_input_as_lines_of_chars(DAY_TEN_INPUT)

    Pipe.map = data

    s_pos = (0,0)

    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if data[i][j] == 'S':
                s_pos = (i, j)

    possible_maps = []

    # start with S and assume it could be each type of pipe, for each one choose a previous pos
    # only need to check one side because it must form loop to be valid
    # for each of these assumed list step through until it becomes invalid or we return to s
    # if we return to s, return the length of that list div 2

    NORTH = (s_pos[0]-1, s_pos[1])
    SOUTH = (s_pos[0] + 1, s_pos[1])
    WEST = (s_pos[0], s_pos[1]-1)

    possible_maps.append([VerticalPipe(s_pos, NORTH)])
    possible_maps.append([HorizontalPipe(s_pos, WEST)])
    possible_maps.append([LPipe(s_pos, NORTH)])
    possible_maps.append([JPipe(s_pos, NORTH)])
    possible_maps.append([SevenPipe(s_pos, WEST)])
    possible_maps.append([FPipe(s_pos, SOUTH)])

    while(True): # this is lazy and prone to error
        # step one in each map at same time becasue some maps me be infinite / never loop
        for map in possible_maps:
            if map[-1].valid():
                next = map[-1].next_pos()
                if next == map[0].pos:
                    # we looped around! return length
                    return len(map)/2
                else:
                    if Pipe.map[next[0]][next[1]] == '|':
                        map.append(VerticalPipe(next, map[-1].pos))
                    elif Pipe.map[next[0]][next[1]] == '-':
                        map.append(HorizontalPipe(next, map[-1].pos))
                    elif Pipe.map[next[0]][next[1]] == 'L':
                        map.append(LPipe(next, map[-1].pos))
                    elif Pipe.map[next[0]][next[1]] == '7':
                        map.append(SevenPipe(next, map[-1].pos))
                    elif Pipe.map[next[0]][next[1]] == 'J':
                        map.append(JPipe(next, map[-1].pos))
                    elif Pipe.map[next[0]][next[1]] == 'F':
                        map.append(FPipe(next, map[-1].pos))

def part_two():
    data = parse_input_as_lines_of_chars(DAY_TEN_INPUT)

    Pipe.map = data

    s_pos = (0,0)

    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if data[i][j] == 'S':
                s_pos = (i, j)

    possible_maps = []

    # start with S and assume it could be each type of pipe, for each one choose a previous pos
    # only need to check one side because it must form loop to be valid
    # for each of these assumed list step through until it becomes invalid or we return to s
    # if we return to s, return the length of that list div 2

    NORTH = (s_pos[0]-1, s_pos[1])
    SOUTH = (s_pos[0] + 1, s_pos[1])
    WEST = (s_pos[0], s_pos[1]-1)

    possible_maps.append([VerticalPipe(s_pos, NORTH)])
    possible_maps.append([HorizontalPipe(s_pos, WEST)])
    possible_maps.append([LPipe(s_pos, NORTH)])
    possible_maps.append([JPipe(s_pos, NORTH)])
    possible_maps.append([SevenPipe(s_pos, WEST)])
    possible_maps.append([FPipe(s_pos, SOUTH)])

    valid_loop = []
    found_loop = False

    while not found_loop: # this is lazy and prone to error
        # step one in each map at same time becasue some maps me be infinite / never loop
        for map in possible_maps:
            if map[-1].valid():
                next = map[-1].next_pos()
                if next == map[0].pos:
                    # we looped around! return length
                    valid_loop = map
                    found_loop = True
                else:
                    if Pipe.map[next[0]][next[1]] == '|':
                        map.append(VerticalPipe(next, map[-1].pos))
                    elif Pipe.map[next[0]][next[1]] == '-':
                        map.append(HorizontalPipe(next, map[-1].pos))
                    elif Pipe.map[next[0]][next[1]] == 'L':
                        map.append(LPipe(next, map[-1].pos))
                    elif Pipe.map[next[0]][next[1]] == '7':
                        map.append(SevenPipe(next, map[-1].pos))
                    elif Pipe.map[next[0]][next[1]] == 'J':
                        map.append(JPipe(next, map[-1].pos))
                    elif Pipe.map[next[0]][next[1]] == 'F':
                        map.append(FPipe(next, map[-1].pos))

    enclose_map = []

    for i in range(0, len(data)):
        enclose_map.append([])
        for j in range(0, len(data[0])):
            enclose_map[i].append('.')

    for pipe in valid_loop:
        enclose_map[pipe.pos[0]][pipe.pos[1]] = 'X'

    # go through and modify all of the edge nodes that are not x to be 0

    for i in range(0, len(enclose_map[0])):
        if enclose_map[0][i] != 'X':
            enclose_map[0][i] = 0

    for i in range(0, len(enclose_map[-1])):
        if enclose_map[-1][i] != 'X':
            enclose_map[-1][i] = 0

    for i in range(0, len(enclose_map)):
        if enclose_map[i][0] != 'X':
            enclose_map[i][0] = 0

    for i in range(0, len(enclose_map)):
        if enclose_map[i][-1] != 'X':
            enclose_map[i][-1] = 0

    modified = True
    while modified:
        modified = False
        for i in range(1, len(enclose_map)-1): # starting here because we did edges above and I don't need to boundary check
            for j in range(1, len(enclose_map[0])-1):
                if enclose_map[i][j] == '.':
                    # if any neighbor is 0 set to 0 and modified true
                    north = enclose_map[i-1][j] == 0
                    south = enclose_map[i+1][j] == 0
                    east = enclose_map[i][j+1] == 0
                    west = enclose_map[i][j-1] == 0
                    if any([north, south, east, west]):
                        enclose_map[i][j] = 0
                        modified = True

    enclosed_count = 0

    for i in range(0, len(enclose_map)):
        for j in range(0, len(enclose_map[0])):
            if enclose_map[i][j] == '.':
                enclosed_count += 1
    #
    # for i in range(0, len(enclose_map)):
    #     for j in range(0, len(enclose_map[0])):
    #         if enclose_map[i][j] == '.':
    #             enclosed_count += 1

    for l in enclose_map:
        print([str(c) for c in l])

    return enclosed_count

from common.utils import parse_input_as_list_of_strings

DAY_THREE_INPUT = 'input/three.txt'

class Part:

    max_x = 0
    max_y = 0

    @staticmethod
    def set_max_x(max):
        Part.max_x = max

    @staticmethod
    def set_max_y(max):
        Part.max_y = max

    def __init__(self, part_number, y, start_x, end_x):
        self.part_number = part_number
        self.y = y
        self.start_x = start_x
        self.end_x = end_x
        self.valid_neighbors = None # Declaring this here so we can use it in next function
        self.generate_valid_neighbors()

    def generate_valid_neighbors(self):
        neighbors = []
        # TODO: Create an array of valid neighbors based on the coords and the static max vars
        # Going to be lazy and accept the coordinates of the part itself as a valid neighbor because it can never be a symbol
        start_y = max(self.y - 1, 0)
        end_y = min(self.y + 1, Part.max_y)
        start_x = max(self.start_x - 1, 0)
        end_x = min(self.end_x + 1, Part.max_x)

        for i in range(start_y, end_y+1):
            for j in range(start_x, end_x+1):
                neighbors.append((i, j))

        self.valid_neighbors = neighbors



def part_one():

    data = parse_input_as_list_of_strings(DAY_THREE_INPUT)

    # set the max values for neighbors
    Part.set_max_x(len(data[0])-1)
    Part.set_max_y(len(data)-1)
    y = 0
    parts = []
    for row in data:
        current_num = None
        start_x = 0
        end_x = 0
        x = 0
        for char in row:
            if char.isdigit() and not current_num:
                current_num = char
                start_x = end_x = x
            elif char.isdigit() and current_num:
                current_num += char
                end_x = x
            elif not char.isdigit() and current_num:
                new_part = Part(int(current_num), y, start_x, end_x)
                parts.append(new_part)
                current_num = None
            else:
                pass
            x += 1
        if current_num:
            new_part = Part(int(current_num), y, start_x, end_x)
            parts.append(new_part)
            current_num = None

        y += 1

    sum = 0

    for part in parts:
        for neighbor in part.valid_neighbors:
            char = data[neighbor[0]][neighbor[1]]
            if not char.isdigit() and char != '.':
                sum += part.part_number
                break

    return sum


def part_two():
    data = parse_input_as_list_of_strings(DAY_THREE_INPUT)

    # set the max values for neighbors
    Part.set_max_x(len(data[0])-1)
    Part.set_max_y(len(data)-1)
    y = 0
    parts = []
    for row in data:
        current_num = None
        start_x = 0
        end_x = 0
        x = 0
        for char in row:
            if char.isdigit() and not current_num:
                current_num = char
                start_x = end_x = x
            elif char.isdigit() and current_num:
                current_num += char
                end_x = x
            elif not char.isdigit() and current_num:
                new_part = Part(int(current_num), y, start_x, end_x)
                parts.append(new_part)
                current_num = None
            else:
                pass
            x += 1
        if current_num:
            new_part = Part(int(current_num), y, start_x, end_x)
            parts.append(new_part)
            current_num = None

        y += 1

    y = 0
    sum = 0
    for row in data:
        x = 0
        for char in row:
            if char == '*':
                adjacent_parts = []
                for part in parts:
                    for neighbor in part.valid_neighbors:
                        if neighbor[0] == y and neighbor[1] == x:
                            adjacent_parts.append(part)
                            break
                if len(adjacent_parts) == 2:
                    sum += adjacent_parts[0].part_number*adjacent_parts[1].part_number
            x+=1
        y+=1

    return sum



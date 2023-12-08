import math
from common.utils import parse_input_as_list_of_strings
from functools import total_ordering

DAY_EIGHT_INPUT = 'input/eight.txt'
DAY_EIGHT_SAMPLE_INPUT = 'input/eight.sample.txt'


class Node:
    all_nodes = {}

    def __init__(self, name, left_name=None, right_name=None):
        self.name = name
        self.left = None
        self.right = None
        if left_name:
            if left_name not in Node.all_nodes:
                Node.all_nodes[left_name] = Node(left_name)
            self.left = Node.all_nodes.get(left_name, None)

        if right_name:
            if right_name not in Node.all_nodes:
                Node.all_nodes[right_name] = Node(right_name)
            self.right = Node.all_nodes.get(right_name, None)

        self.terminal = self.name[-1] == 'Z'

        Node.all_nodes[name] = self

    def set_left(self, left_name):
        if left_name:
            if left_name not in Node.all_nodes:
                Node.all_nodes[left_name] = Node(left_name)
            self.left = Node.all_nodes.get(left_name, None)

    def set_right(self, right_name):
        if right_name:
            if right_name not in Node.all_nodes:
                Node.all_nodes[right_name] = Node(right_name)
            self.right = Node.all_nodes.get(right_name, None)

    def __repr__(self):
        return f'Node {self.name}'


def part_one():
    data = parse_input_as_list_of_strings(DAY_EIGHT_INPUT)

    path = data[0]

    for i in range(2, len(data)):
        split_data = data[i].split('=')
        name = split_data[0].strip()
        children = split_data[1].strip().replace('(', '').replace(')', '').split(',')
        left = children[0].strip()
        right = children[1].strip()
        if name not in Node.all_nodes:
            Node(name, left, right)
        else:
            Node.all_nodes[name].set_left(left)
            Node.all_nodes[name].set_right(right)

    count = 0
    node = Node.all_nodes['AAA']
    next_instruction = 0

    while node.name != 'ZZZ':
        if path[next_instruction] == 'L':
            node = node.left
        else:
            node = node.right
        count += 1
        next_instruction += 1
        if next_instruction == len(path):
            next_instruction = 0

    return count


def part_two():
    data = parse_input_as_list_of_strings(DAY_EIGHT_INPUT)

    path = data[0]
    Node.all_nodes = {} # reset from part 1
    for i in range(2, len(data)):
        split_data = data[i].split('=')
        name = split_data[0].strip()
        children = split_data[1].strip().replace('(', '').replace(')', '').split(',')
        left = children[0].strip()
        right = children[1].strip()
        if name not in Node.all_nodes:
            Node(name, left, right)
        else:
            Node.all_nodes[name].set_left(left)
            Node.all_nodes[name].set_right(right)

    count = 0
    nodes = [n for n in Node.all_nodes.values() if n.name[-1] == 'A']
    next_instruction = 0
    end = False
    counts = []

    for i in range(0, len(nodes)):
        count = 0
        next_instruction = 0
        while not nodes[i].terminal:
            if path[next_instruction] == 'L':
                nodes[i] = nodes[i].left
            else:
                nodes[i] = nodes[i].right
            count += 1
            next_instruction += 1
            if next_instruction == len(path):
                next_instruction = 0
        counts.append(count)

    return math.lcm(*counts)

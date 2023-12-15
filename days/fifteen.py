import re
from functools import cache

from common.utils import parse_input_as_list_of_strings


INPUT = 'input/fifteen.txt'
SAMPLE_INPUT = 'input/fifteen.sample.txt'



def part_one():
    data = parse_input_as_list_of_strings(INPUT)
    data = data[0] # in this puzzle its one long string
    data = data.split(',')

    sum = 0
    for word in data:
        hash = 0
        for c in word:
            hash += ord(c)
            hash *= 17
            hash = hash % 256
        sum += hash

    return sum

class Lens:

    def __init__(self, label='', focal_length=1, priority=0):
        self.label = label
        self.focal_length = int(focal_length)
        self.priority = priority

    def hash(self):
        h = 0
        for c in self.label:
            h += ord(c)
            h *= 17
            h = h % 256
        return h

    def __repr__(self):
        return f'[{self.label} {self.focal_length}]'

    def __eq__(self, obj):
        return self.label == obj.label

    def __hash__(self):
        return hash(self.label)



def part_two():
    data = parse_input_as_list_of_strings(INPUT)
    data = data[0] # in this puzzle its one long string
    data = data.split(',')

    boxes = {}
    for i in range(0, 256):
        boxes[i] = set()

    priorty = 0
    for word in data:
        if word[-1] == '-':
            label = word[0:-1]
            lens = Lens(label)
            if lens in boxes[lens.hash()]:
                boxes[lens.hash()].remove(lens)
        else:
           tmp = word.split('=')
           lens = Lens(tmp[0], focal_length=tmp[1], priority=priorty)
           if lens in boxes[lens.hash()]:
                for i in boxes[lens.hash()]:
                    if i.label == lens.label:
                        i.focal_length = lens.focal_length
           else:
               boxes[lens.hash()].add(lens)
               priorty+=1

    sum = 0

    for i in range(0, 256):
        if len(boxes[i]) > 0:
            l = list(boxes[i])
            l.sort(key= lambda x: x.priority)
            slot = 1
            for lens in l:
                power = (i+1) * slot * lens.focal_length
                slot += 1
                sum += power

    return sum








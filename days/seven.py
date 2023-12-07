from common.utils import parse_input_as_list_of_strings
from functools import total_ordering

DAY_SEVEN_INPUT = 'input/seven.txt'

HAND_FIVE_OF_A_KIND = 0
HAND_FOUR_OF_A_KIND = 1
HAND_FULL_HOUSE = 2
HAND_THREE_OF_A_KIND = 3
HAND_TWO_PAIR = 4
HAND_PAIR = 5
HAND_HIGH_CARD = 6

@total_ordering
class CamelHand():

    @staticmethod
    def card_value(card):
        cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        return cards.index(card)

    def __init__(self, cards='AAAAA', bid=0):
        self.cards = cards
        self.bid = bid
        self.cards_dict = {}
        for char in cards:
            if char not in self.cards_dict:
                self.cards_dict[char] = 0
            self.cards_dict[char] = self.cards_dict[char] + 1

    # should store this statically with the hand like I do in wild camel hand but didn't make that optimization here
    def hand_type(self):
        if len(self.cards_dict.keys()) == 1:
            return HAND_FIVE_OF_A_KIND
        elif len(self.cards_dict.keys()) == 2:
            # i really only need to check one value not both but too lazy to cast to list and index first element
            for key, value in self.cards_dict.items():
                if value == 1 or value == 4:
                    return HAND_FOUR_OF_A_KIND
            return HAND_FULL_HOUSE
        elif len(self.cards_dict.keys()) == 3:
            for key, value in self.cards_dict.items():
                if value == 3:
                    return HAND_THREE_OF_A_KIND
            return HAND_TWO_PAIR
        elif len(self.cards_dict.keys()) == 4:
            return HAND_PAIR
        else: # len == 5
            return HAND_HIGH_CARD

    def __lt__(self, obj):
        if self.hand_type() == obj.hand_type():
            for i in range(0, 5):
                if self.cards[i] != obj.cards[i]:
                    return CamelHand.card_value(self.cards[i]) > CamelHand.card_value(obj.cards[i])
        return self.hand_type() > obj.hand_type()

    def __eq__(self, obj):
        return self.cards == obj.cards

    def __repr__(self):
        return str((self.cards, self.hand_type(), self.bid))

@total_ordering
class WildCamelHand():

    @staticmethod
    def card_value(card):
        cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
        return cards.index(card)

    @staticmethod
    def hand_type(card_dict):
        sorted_dict = dict(sorted(card_dict.items(), key=lambda item: item[1], reverse=True)) # need to sort this to ensure we tackle the largest card groups first
        joker_count = sorted_dict.get('J', 0)
        non_joker_keys = list(sorted_dict.keys())
        if 'J' in non_joker_keys:
            non_joker_keys.remove('J')
        if joker_count == 5:
            return HAND_FIVE_OF_A_KIND
        for key, value in sorted_dict.items():
            if key != 'J':
                if value+joker_count == 5:
                    return HAND_FIVE_OF_A_KIND
                elif value+joker_count == 4:
                    return HAND_FOUR_OF_A_KIND
                elif value+joker_count == 3:
                    # three of a kind or full house
                    if len(non_joker_keys) == 2:
                        return HAND_FULL_HOUSE
                    else:
                        return HAND_THREE_OF_A_KIND
                elif value+joker_count == 2:
                    # a full house could run into this first
                    if len(non_joker_keys) == 2:
                        return HAND_FULL_HOUSE
                    elif len(non_joker_keys) == 3:
                        return HAND_TWO_PAIR
                    else:
                        return HAND_PAIR
        return HAND_HIGH_CARD


    def __init__(self, cards='AAAAA', bid=0):
        self.cards = cards
        self.bid = bid
        self.cards_dict = {}

        for char in cards:
            if char not in self.cards_dict:
                self.cards_dict[char] = 0
            self.cards_dict[char] = self.cards_dict[char] + 1

        self.hand_type = WildCamelHand.hand_type(self.cards_dict)

    def __lt__(self, obj):
        if self.hand_type == obj.hand_type:
            for i in range(0, 5):
                if self.cards[i] != obj.cards[i]:
                    return WildCamelHand.card_value(self.cards[i]) > WildCamelHand.card_value(obj.cards[i])
        return self.hand_type > obj.hand_type

    def __eq__(self, obj):
        return self.cards == obj.cards

    def __repr__(self):
        return str((self.cards, self.hand_type, self.bid))



def part_one():
    data = parse_input_as_list_of_strings(DAY_SEVEN_INPUT)
    hands = []
    for line in data:
        split_line = line.split(' ')
        cards = split_line[0]
        bid = int(split_line[1])
        hands.append(CamelHand(cards, bid))

    total = 0
    rank = 1
    for hand in sorted(hands):
        total += rank*hand.bid
        rank +=1

    return total







def part_two():
    data = parse_input_as_list_of_strings(DAY_SEVEN_INPUT)
    hands = []
    for line in data:
        split_line = line.split(' ')
        cards = split_line[0]
        bid = int(split_line[1])
        hands.append(WildCamelHand(cards, bid))

    total = 0
    rank = 1
    for hand in sorted(hands):
        total += rank*hand.bid
        rank +=1

    return total










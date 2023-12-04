from common.utils import parse_input_as_list_of_strings

DAY_FOUR_INPUT = 'input/four.txt'

def part_one():
    data = parse_input_as_list_of_strings(DAY_FOUR_INPUT)
    total_score = 0
    for card in data:
        numbers = card.split(':')[1].strip()
        numbers = numbers.split('|')
        winning_numbers = sorted([int(num) for num in numbers[0].strip().split(' ') if num != ''])
        card_numbers = sorted([int(num) for num in numbers[1].strip().split(' ') if num != ''])

        winning_ptr = 0
        card_ptr = 0
        score = 0

        while winning_ptr < len(winning_numbers) and card_ptr < len(card_numbers):
            win_adv = 0
            card_adv = 0
            # check if the number is a winner
            if winning_numbers[winning_ptr] == card_numbers[card_ptr]:
                if score == 0:
                    score = 1
                else:
                    score *= 2

            # advance the pointer with the lowest number
            if winning_numbers[winning_ptr] < card_numbers[card_ptr] and winning_ptr < len(winning_numbers):
                win_adv = 1
            elif card_ptr < len(card_numbers):
                card_adv = 1
            else:
                win_adv = 1 # This case should only happen if card_ptr is finished but all winning numbers ar higher... may be able to bail here

            winning_ptr += win_adv
            card_ptr += card_adv

        total_score += score

    return total_score


def part_two():
    data = parse_input_as_list_of_strings(DAY_FOUR_INPUT)
    copies = []
    total_cards = 0

    #store an array of copies as ints and set all to 1
    for i in range(0, len(data)):
        copies.append(1)

    card_index = 0

    for card in data:
        numbers = card.split(':')[1].strip()
        numbers = numbers.split('|')
        winning_numbers = sorted([int(num) for num in numbers[0].strip().split(' ') if num != ''])
        card_numbers = sorted([int(num) for num in numbers[1].strip().split(' ') if num != ''])

        winning_ptr = 0
        card_ptr = 0
        win_count = 0

        while winning_ptr < len(winning_numbers) and card_ptr < len(card_numbers):
            win_adv = 0
            card_adv = 0
            # check if the number is a winner
            if winning_numbers[winning_ptr] == card_numbers[card_ptr]:
                win_count += 1

            # advance the pointer with the lowest number
            if winning_numbers[winning_ptr] < card_numbers[card_ptr] and winning_ptr < len(winning_numbers):
                win_adv = 1
            elif card_ptr < len(card_numbers):
                card_adv = 1
            else:
                win_adv = 1 # This case should only happen if card_ptr is finished but all winning numbers ar higher... may be able to bail here

            winning_ptr += win_adv
            card_ptr += card_adv

        for i in range(1, win_count+1):
            copies[card_index+i] += copies[card_index]

        card_index += 1


    return sum(copies)

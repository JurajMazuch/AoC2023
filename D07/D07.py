import os
from enum import IntEnum
from functools import cmp_to_key


class Type(IntEnum):
    five_of_a_kind = 6
    four_of_a_kind = 5
    full_house = 4
    three_of_a_kind = 3
    two_pair = 2
    one_pair = 1
    high_card = 0


card_labels = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
card_labels_2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def get_type(cards):
    card_counts = [0] * len(card_labels)
    for card in cards:
        card_counts[card_labels.index(card)] += 1

    card_counts.sort(reverse=True)
    if card_counts[0] == 5:
        return Type.five_of_a_kind
    elif card_counts[0] == 4:
        return Type.four_of_a_kind
    elif card_counts[0] == 3 and card_counts[1] == 2:
        return Type.full_house
    elif card_counts[0] == 3:
        return Type.three_of_a_kind
    elif card_counts[0] == 2 and card_counts[1] == 2:
        return Type.two_pair
    elif card_counts[0] == 2:
        return Type.one_pair
    else:
        return Type.high_card


def get_type_2(cards):
    card_counts = [0] * len(card_labels_2)
    for card in cards:
        card_counts[card_labels_2.index(card)] += 1

    card_counts.sort(reverse=True)
    if card_counts[0] == 5:
        return Type.five_of_a_kind
    elif card_counts[0] == 4:
        if cards.count('J') == 1 or cards.count('J') == 4:
            return Type.five_of_a_kind
        return Type.four_of_a_kind
    elif card_counts[0] == 3 and card_counts[1] == 2:
        if cards.count('J') > 0:
            return Type.five_of_a_kind
        return Type.full_house
    elif card_counts[0] == 3:
        if cards.count('J') == 3 or cards.count('J') == 1:
            return Type.four_of_a_kind
        return Type.three_of_a_kind
    elif card_counts[0] == 2 and card_counts[1] == 2:
        if cards.count("J") == 1:
            return Type.full_house
        if cards.count("J") == 2:
            return Type.four_of_a_kind
        return Type.two_pair
    elif card_counts[0] == 2:
        if cards.count("J") == 1 or cards.count("J") == 2:
            return Type.three_of_a_kind
        return Type.one_pair
    else:
        if cards.count("J") == 1:
            return Type.one_pair
        return Type.high_card


class Hand:
    def __init__(self, cards, bid, t):
        self.cards = cards
        self.bid = bid
        self.type = t


def compare_hands(x, y):
    if int(x.type) - int(y.type) != 0:
        return int(x.type) - int(y.type)

    for i in range(0, len(x.cards)):
        if x.cards[i] != y.cards[i]:
            return card_labels.index(x.cards[i]) - card_labels.index(y.cards[i])
    return 0


def compare_hands_2(x, y):
    if int(x.type) - int(y.type) != 0:
        return int(x.type) - int(y.type)

    for i in range(0, len(x.cards)):
        if x.cards[i] != y.cards[i]:
            return card_labels_2.index(x.cards[i]) - card_labels_2.index(y.cards[i])
    return 0


def get_winnings(hands):
    winnings = 0
    for hand in hands:
        rank = hands.index(hand) + 1
        winnings += rank * hand.bid

    return winnings


def part1(data):
    hands = []
    for cards, bid in sorted([line.split(' ') for line in data.split('\n')]):
        hands.append(Hand(cards, int(bid), get_type(cards)))

    return get_winnings(sorted(hands, key=cmp_to_key(compare_hands)))


def part2(data):
    hands = []
    for cards, bid in sorted([line.split(' ') for line in data.split('\n')]):
        hands.append(Hand(cards, int(bid), get_type_2(cards)))

    return get_winnings(sorted(hands, key=cmp_to_key(compare_hands_2)))


with open(os.path.join(os.path.dirname(__file__), 'D07.txt'), 'r') as file:
    input_data = file.read()

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))

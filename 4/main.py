from collections import defaultdict
from pprint import pprint

def calculate_points(cards: list[tuple[set,set]]) -> int:
    total = 0
    for winner, holding in cards:
        count = len(winner & holding)
        if count > 0:
            total += 2**(count-1)

    return total

def count_cards(cards: list[tuple[set,set]]) -> int:
    # mem = dict()
    # res = len(cards)
    # for i, card in enumerate(cards):
    #     res += count_cards_recursive(cards, i, mem)

    res = count_cards_iterative(cards)

    return res

def count_cards_iterative(cards: list[tuple[set,set]]) -> int:
    matches = []
    for card in cards:
        w, h = card
        matches.append(len(w & h))

    copies = [1]*len(cards)
    for i in range(len(cards)):
        next_cards = min(i+1+matches[i], len(cards))
        for j in range(i+1, next_cards):
            copies[j] += copies[i]

    return sum(copies)

def count_cards_recursive(cards: list[tuple[set,set]], index: int, mem:dict[int,int]) -> int:
    if index >= len(cards):
        return 0

    if index in mem:
        count = mem[index]
    else:
        winner, holding = cards[index]
        count = len(winner & holding)
        mem[index] = count

    if index == len(cards)-1:
        return count

    res = count
    for i in range(1, count+1):
        c = count_cards_recursive(cards, index+i, mem)
        res += c

    return res

def parse_input(path: str) -> list:
    out = []
    with open(path) as file:
        for line in file:
            winner, holding = line.strip().split('|')
            winner = winner.split(':')[1]
            winner = set([int(x) for x in winner.split()])
            holding = set([int(x) for x in holding.split()])

            out.append((winner, holding))
    return out

if __name__ == "__main__":
    sample_input = parse_input("./sample.input")
    sample_answer_p1 = 13
    sample_result_p1 = calculate_points(sample_input)
    print("Part 1 sample:", sample_answer_p1 == sample_result_p1, sample_result_p1)
    sample_answer_p2 = 30
    sample_result_p2 = count_cards(sample_input)
    print("Part 2 sample:", sample_answer_p2 == sample_result_p2, sample_result_p2)

    main_input = parse_input("./main.input")
    main_result_p1 = calculate_points(main_input)
    print("Part 1 main:", main_result_p1)
    main_result_p2 = count_cards(main_input)
    print("Part 2 main:", main_result_p2)

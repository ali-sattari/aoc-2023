

from pprint import pprint

def calculate_points(cards: list[tuple[set,set]]) -> int:
    total = 0
    for winner, holding in cards:
        count = len(winner & holding)
        if count > 0:
            total += 2**(count-1)

    return total

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

    main_input = parse_input("./main.input")
    main_result_p1 = calculate_points(main_input)
    print("Part 1 main:", main_result_p1)

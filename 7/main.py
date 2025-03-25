from pprint import pprint
from collections import Counter

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
hands = [
    "five_of_a_kind",
    "four_of_a_kind",
    "full_house",
    "three_of_a_kind",
    "two_pair",
    "one_pair",
    "high_card"
]
hand_freq_map = {
    '5': hands[0],       # five_of_a_kind
    '41': hands[1],      # four_of_a_kind
    '32': hands[2],      # full_house
    '311': hands[3],     # three_of_a_kind
    '221': hands[4],     # two_pair
    '2111': hands[5],    # one_pair
    '11111': hands[6],   # high_card
}

class Hand:
    def __init__(self, hand: str):
        self._hand = hand
        self._type = categorize_hand(hand)

    def __repr__(self):
        return f"{self._type}({self._hand})"

    def __eq__(self, other):
        return self._type == other._type

    def __lt__(self, other):
        if self != other:
            return hands.index(self._type) > hands.index(other._type)
        else:
            for i in range(len(self._hand)):
                c1, c2 = self._hand[i], other._hand[i]
                if c1 == c2:
                    continue
                return cards.index(c1) > cards.index(c2)

def solve_p1(hands: list[tuple[Hand,int]]) -> int:
    hands = sorted(hands, key=lambda x: x[0])
    score = 0
    for i, (_, b) in enumerate(hands):
        score += (i+1) * b

    return score

def categorize_hand(hand: str) -> str:
    f = sorted(Counter(list(hand)).values(), reverse=True)
    f = ''.join([str(x) for x in f])
    return hand_freq_map[f]

def parse_input(path: str) -> list[tuple[str,int]]:
    inp = []
    with open(path) as file:
        for line in file:
            hand, bid = line.split()
            inp.append((Hand(hand), int(bid)))
    return inp

if __name__ == "__main__":
    sample_input = parse_input("./sample.input")
    sample_answer_p1 = 6440
    sample_result_p1 = solve_p1(sample_input)
    print("Part 1 sample:", sample_answer_p1 == sample_result_p1, sample_result_p1)

    main_input = parse_input("./main.input")
    print("Part 1 main:", solve_p1(main_input))

from pprint import pprint
from collections import Counter

cards_p1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards_p2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
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
    def __init__(self, hand: str, part=1):
        self._hand = hand
        if part == 1:
            self._type = categorize_hand_p1(hand)
            self._cards = cards_p1
        elif part == 2:
            self._type = categorize_hand_p2(hand)
            self._cards = cards_p2

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
                return self._cards.index(c1) > self._cards.index(c2)

def solve(hands: list[tuple[Hand,int]]) -> int:
    hands = sorted(hands, key=lambda x: x[0])
    score = 0
    for i, (h, b) in enumerate(hands):
        # print(f"{i+1}: {h}")
        score += (i+1) * b

    return score

def categorize_hand_p1(hand: str) -> str:
    f = Counter(list(hand))
    return hand_freq_map[feq_to_str(f)]

def categorize_hand_p2(hand: str) -> str:
    f = Counter(list(hand))
    l = hand_freq_map[feq_to_str(f)]
    if 'J' in f:
        r = hands.index(l)
        nr = max(0, r - f['J'])
        nl = hands[nr] # each J can push the hand one rank up
        return nl
    else:
        return l

def feq_to_str(f: dict) -> str:
    return ''.join([str(x) for x in sorted(f.values(), reverse=True)])

def parse_input(path: str, part=1) -> list[tuple[str,int]]:
    inp = []
    with open(path) as file:
        for line in file:
            hand, bid = line.split()
            inp.append((Hand(hand, part), int(bid)))
    return inp

if __name__ == "__main__":
    sample_input_p1 = parse_input("./sample.input")
    sample_answer_p1 = 6440
    sample_result_p1 = solve(sample_input_p1)
    print("Part 1 sample:", sample_answer_p1 == sample_result_p1, sample_result_p1)

    sample_input_p2 = parse_input("./sample.input", 2)
    sample_answer_p2 = 5905
    sample_result_p2 = solve(sample_input_p2)
    print("Part 2 sample:", sample_answer_p2 == sample_result_p2, sample_result_p2)

    main_input_p1 = parse_input("./main.input")
    main_input_p2 = parse_input("./main.input", 2)
    print("Part 1 main:", solve(main_input_p1))
    print("Part 2 main:", solve(main_input_p2))

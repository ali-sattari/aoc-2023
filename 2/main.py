from pprint import pprint
import math

class Draw:
    colors = ['red', 'green', 'blue']
    def __init__(self, cubes: dict[str, int]):
        t = ()
        for c in self.colors:
            v = cubes.get(c, 0)
            t = (*t, v)
        self.cubes = t

    def __repr__(self):
        out = []
        for i, v in enumerate(self.cubes):
            out.append(f"{self.colors[i]}:{v}")

        return f"Draw({', '.join(out)})"

    def __le__(self, other):
        return all(x <= y for x, y in zip(self, other))

    def __iter__(self):
        return iter(self.cubes)

    def __getitem__(self, index):
        return self.cubes[index]

    def getMax(self, other):
        return tuple(max(a, b) for a, b in zip(self, other))


def parse_input(path: str) -> dict:
    games = dict()
    with open(path) as file:
        for line in file:
            game, rest = line.split(':')
            game = int(game.split()[1])
            rounds = []
            for round in rest.split(';'):
                r = {color: int(count) for count, color in (x.split() for x in round.split(','))}
                rounds.append(Draw(r))
            games[game] = rounds
    return games

def solution_p1(games: dict) -> int:
    bag = Draw({
        'red': 12,
        'green': 13,
        'blue': 14,
    })
    answer = 0
    for id, draws in games.items():
        for d in draws:
            if (d <= bag) == False:
                # print(f"game {id} is impossibru! {d}")
                break
        else:
            # print(f"game {id} is possibru {draws}")
            answer += id

    return answer

def solution_p2(games: dict) -> int:
    answer = 0
    for id, draws in games.items():
        m = (0, 0, 0)
        for d in draws:
            m = d.getMax(m)

        answer += math.prod(m)

    return answer

if __name__ == "__main__":
    sample_games = parse_input('./p1_sample.input')
    main_games = parse_input('./p1_main.input')

    # Part 1
    p1_sample_answer = 8
    p1_sample_result = solution_p1(sample_games)
    print("Part 1 Sample:", p1_sample_answer == p1_sample_result, p1_sample_result)
    print("Part 1 Main:", solution_p1(main_games))

    # Part 2
    p2_sample_answer = 2286
    p2_sample_result = solution_p2(sample_games)
    print("Part 2 Sample:", p2_sample_answer == p2_sample_result, p2_sample_result)
    print("Part 2 Main:", solution_p2(main_games))

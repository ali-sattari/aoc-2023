from pprint import pprint

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
        for i, v in enumerate(self.cubes):
            if (v <= other[i]) == False:
                return False

        return True

    def __iter__(self):
        return iter(self.cubes)

    def __getitem__(self, index):
        return self.cubes[index]

colors = ['red', 'green', 'blue']
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

bag = Draw({
    'red': 12,
    'green': 13,
    'blue': 14,
})

def solution_p1(games: dict) -> int:
    answer = 0
    for id, draws in games.items():
        p = True
        for d in draws:
            if (d <= bag) == False:
                # print(f"game {id} is impossibru! {d}")
                break
        else:
            # print(f"game {id} is possibru {draws}")
            answer += id

    return answer

if __name__ == "__main__":
    sample_games = parse_input('./p1_sample.input')
    p1_sample_answer = 8
    p1_sample_result = solution_p1(sample_games)
    print("Part 1 Sample:", p1_sample_answer == p1_sample_result, p1_sample_result)

    main_games = parse_input('./p1_main.input')
    print("Part 1 Main:", solution_p1(main_games))

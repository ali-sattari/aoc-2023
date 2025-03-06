from pprint import pprint
from termcolor import colored

class Solution:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.symbols = set()

    def calculate(self) -> int:
        part_nums = []
        kept = set()
        dropped = set()

        for y, row in enumerate(self.grid):
            # temporary lists per number
            _num = ""
            _pos = []

            for x, cell in enumerate(row):
                # add contiguous digits to temporary lists
                if cell.isdigit():
                    _num += cell
                    _pos.append((y,x))

                # on non digit, or at the end of line
                if cell.isdigit() is False or x == self.cols-1:
                    if len(_num) > 0:
                        n = int(_num)
                        if self.isPartNumber(_pos):
                            part_nums.append(n)
                            kept.update(_pos)
                        else:
                            dropped.update(_pos)

                        # reset anyways for the next digit
                        _num = ""
                        _pos = []

        # self.renderGrid(kept, dropped)

        return sum(part_nums)

    def renderGrid(self, valid, invalid: set):
        for y, row in enumerate(self.grid):
            line = ""
            for x, cell in enumerate(row):
                if (y, x) in valid:
                    line += colored(cell, 'green')
                elif (y, x) in invalid:
                    line += colored(cell, 'red')
                elif (y, x) in self.symbols:
                    line += colored(cell, 'yellow')
                else:
                    line += colored(cell, 'grey')
            print(line)

    def isPartNumber(self, positions: list[tuple]) -> bool:
        nbrs = set()
        for p in positions:
            nbrs.update(self.getNeighbors(p))
        nbrs -= set(positions)

        for (y, x) in nbrs:
            c = self.grid[y][x]
            if self.isSymbol(c):
                self.symbols.add((y,x))
                return True
        return False

    def isSymbol(self, cell: str) -> bool:
        return not cell.isdigit() and cell != '.'

    def inGrid(self, pos: tuple) -> bool:
        return 0 <= pos[0] < self.rows and 0 <= pos[1] < self.cols

    def getNeighbors(self, pos: tuple) -> list[tuple]:
        dirs = [ # (y, x)
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1),
        ]
        nbrs = []
        for d in dirs:
            np = (d[0] + pos[0], d[1] + pos[1])
            if self.inGrid(np):
                nbrs.append(np)

        return nbrs

def parse_input(path: str) -> list:
    out = []
    with open(path) as file:
        for line in file:
            out.append(list(line.strip()))
    return out

if __name__ == "__main__":
    sample_input = parse_input("./p1_sample.input")
    sample_answer = 4361
    sol = Solution(sample_input)
    sample_result = sol.calculate()
    print("Part 1 sample:", sample_answer == sample_result, sample_result)

    main_input = parse_input("./p1_main.input")
    sol_main = Solution(main_input)
    main_result = sol_main.calculate()
    print("Part 1 main:", main_result)

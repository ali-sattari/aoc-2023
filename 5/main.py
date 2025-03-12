
from pprint import pprint
from bisect import bisect_left

order = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity']

def solve_p1(seeds: list[int], mappings: dict[str, dict[int, int]], range_starts: dict[str, list[int]]) -> int:
    locs = []
    for seed in seeds:
        curr = seed
        for step in order:
            if curr < range_starts[step][0]:
                continue

            idx = bisect_left(range_starts[step], curr)
            src = range_starts[step][idx-1]
            dst, rng = mappings[step][src]

            # calc dst based on src
            diff = curr - src
            # skip translation if range doesn't cover the diff
            curr = diff + dst if rng >= diff else curr
            # print(f"{step}: curr {curr}, src {src}, dst {dst}, range {rng}")

        locs.append(curr)

    return min(locs)

def getDestination(category: str, src: int):
    pass

def parse_input(path: str) -> tuple[list[int], dict[str, dict], dict[str, list[int]]]:
    mappings = {}
    range_start = {}
    seeds = []
    with open(path) as file:
        ln = 0
        name, maps, starts = '', {}, []
        for line in file:
            ln += 1
            if ln == 1:
                seeds = [int(x) for x in line.split(':')[1].strip().split()]
            if ln == 2: continue
            else:
                if line.strip() == '':
                    mappings[name] = maps
                    range_start[name] = sorted(starts)
                    name, maps, starts = '', {}, []
                elif line[0].isdigit():
                    dst, src, rng = [int(x) for x in line.split()]
                    starts.append(src)
                    maps[src] = (dst, rng)
                else:
                    name = line.split('-')[0]
        # last mappings
        mappings[name] = maps
        range_start[name] = sorted(starts)

        return (seeds, mappings, range_start)

if __name__ == "__main__":
    sample_input = parse_input("./sample.input")
    sample_answer_p1 = 35
    sample_result_p1 = solve_p1(*sample_input)
    print("Part 1 sample:", sample_answer_p1 == sample_result_p1, sample_result_p1)

    main_input = parse_input("./main.input")
    main_result_p1 = solve_p1(*main_input)
    print("Part 1 main:", main_result_p1)

from bisect import bisect_left
import math

class Range:
    def __init__(self, start, end: int):
        if end < start:
            raise ValueError(f"Range length should be 0 or more: {start}, {end}")

        self.start, self.end = start, end

    def __repr__(self):
        return f"Range({self.start}, {self.end})"

    def __lt__(self, other):
        return self.start < other.start

    def __gt__(self, other):
        return self.end > other.start

    def __add__(self, dist: int):
        return Range(self.start + dist, self.end + dist)

    def distance(self, other) -> int:
        return self.start - other.start

    def overlaps(self, other):
        if not isinstance(other, Range):
            raise ValueError("{other} is not of type Range")

        return not (self.start >= other.end or self.end <= other.start)

    def intersect(self, other):
        if not self.overlaps(other):
            return None

        return Range(
            max(self.start, other.start),
            min(self.end, other.end)
        )

    def difference(self, other):
        if not self.overlaps(other):
            return []

        res = []
        if self.start < other.start:
            res.append(Range(self.start, other.start))

        if other.end < self.end:
            res.append(Range(other.end, self.end))

        return res

order = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity']

def solve_p1(seeds: list[int], mappings: dict[str, dict[int, tuple]], range_starts: dict[str, list[int]]) -> int:
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

def solve_p2(seeds: list[Range], mappings: dict[str, list[tuple[Range, Range]]]) -> int:
    loc = math.inf
    intervals = [(x, 0) for x in seeds]

    while intervals:
        rng, level = intervals.pop()

        # if all steps are processed
        if level == len(order):
            # print(f"{"-"*15} loc: {loc}, {rng}")
            loc = min(rng.start, loc)
            continue

        step = order[level]
        # print(f"{step} -> {mappings[step]}")
        for src, dst in mappings[step]:
            if not rng.overlaps(src):
                # print(f"step: {step} ({level}): \t {rng} / {src} -> no overlap!")
                continue

            diff = rng.difference(src)
            for x in diff:
                intervals.append((x, level))

            intersect = rng.intersect(src) + dst.distance(src)
            intervals.append((intersect, level+1))

            # print(f"step: {step} ({level}): \t {rng} / {src} -> intersect {intersect} (+{dst.distance(src)}) and diff {diff}")

            break

        else:
            # print(f"step: {step} ({level}): \t {rng} -> no overlap, passing on!")
            intervals.append((rng, level+1))

    return loc

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
                continue
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
                    name, _, dst_name = line.strip().split()[0].split('-')

        # last mappings
        mappings[name] = maps
        range_start[name] = sorted(starts)

        return (seeds, mappings, range_start)

def parse_input_ranges(path: str) -> tuple[list[Range], dict[str, list[tuple[Range]]]]:
    seeds = []
    mappings = {}
    with open(path) as file:
        ln = 0
        min_src, min_dst = math.inf, math.inf
        src, dst, maps = 0, 0, []
        for line in file:
            ln += 1
            if ln == 1:
                s = [int(x) for x in line.split(':')[1].strip().split()]
                for start, count in zip(s[::2], s[1::2]):
                    seeds.append(Range(start, start+count))
                continue
            if ln == 2: continue
            else:
                if line.strip() == '':
                    # maps.append((Range(0, min_src), Range(0, min_dst)))
                    mappings[src_name] = sorted(maps)
                    min_src, min_dst, maps = math.inf, math.inf, []
                elif line[0].isdigit():
                    dst, src, rng = [int(x) for x in line.split()]
                    min_src = min(min_dst, src)
                    min_dst = min(min_dst, dst)
                    maps.append((
                        Range(src, src+rng),
                        Range(dst, dst+rng)
                    ))
                else:
                    src_name, _, dst_name = line.strip().split()[0].split('-')

        # last mapping
        maps.append((Range(0, min_src), Range(0, min_dst)))
        mappings[src_name] = sorted(maps)

    return (sorted(seeds), mappings)

if __name__ == "__main__":
    sample_input = parse_input("./sample.input")
    sample_answer_p1 = 35
    sample_result_p1 = solve_p1(*sample_input)
    print("Part 1 sample:", sample_answer_p1 == sample_result_p1, sample_result_p1)

    main_input = parse_input("./main.input")
    main_result_p1 = solve_p1(*main_input)
    print("Part 1 main:", main_result_p1)

    sample_input_p2 = parse_input_ranges("./sample.input")
    sample_answer_p2 = 46
    sample_result_p2 = solve_p2(*sample_input_p2)
    print("Part 2 sample:", sample_answer_p2 == sample_result_p2, sample_result_p2)

    main_input_p2 = parse_input_ranges("./main.input")
    main_result_p2 = solve_p2(*main_input_p2)
    print("Part 2 main:", main_result_p2)

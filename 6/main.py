from math import prod

def solve_p1(races: list[tuple[int, int]]) -> int:
    answer = []
    for time, distance in races:
        answer.append(count_winning_times(time, distance))

    return prod(answer)

def count_winning_times(time, dist) -> int:
    count = 0
    for t in range(1, time-1):
        v = t * (time - t) # speed x remaining time
        if v > dist: count += 1

    return count

def parse_input(path: str):
    with open(path) as file:
        lines = file.readlines()
        times = lines[0].split(':')[1].strip().split()
        distances = lines[1].split(':')[1].strip().split()

    races = [(int(t), int(d)) for t, d in zip(times, distances)]

    return races

if __name__ == "__main__":
    sample_input = parse_input("./sample.input")
    sample_answer_p1 = 288
    sample_result_p1 = solve_p1(sample_input)
    print("Part 1 sample:", sample_answer_p1 == sample_result_p1, sample_result_p1)

    main_input = parse_input("./main.input")
    print("Part 1 main:", solve_p1(main_input))

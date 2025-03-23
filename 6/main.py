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

def solve_p2(time, dist) -> int:
    start = find_winning_boundary(time, dist, lambda x: x > 0)
    end = find_winning_boundary(time, dist, lambda x: x <= 0)
    return end - start

def find_winning_boundary(time, dist: int, condition: callable) -> int:
    left, right = 0, time - 1
    while left < right:
        mid = left + (right - left) // 2
        if condition(margin(mid, time, dist)):
            right = mid
        else:
            left = mid + 1
    return left

def margin(press, time, dist) -> int:
    return (press * (time-press)) - dist

def parse_input(path: str):
    with open(path) as file:
        lines = file.readlines()
        times = lines[0].split(':')[1].strip().split()
        distances = lines[1].split(':')[1].strip().split()

    races_1 = [(int(t), int(d)) for t, d in zip(times, distances)]
    races_2 = (
        int(''.join(times)),
        int(''.join(distances)),
    )

    return races_1, races_2

if __name__ == "__main__":
    sample_input = parse_input("./sample.input")
    sample_answer_p1 = 288
    sample_result_p1 = solve_p1(sample_input[0])
    print("Part 1 sample:", sample_answer_p1 == sample_result_p1, sample_result_p1)

    main_input = parse_input("./main.input")
    print("Part 1 main:", solve_p1(main_input[0]))

    sample_answer_p2 = 71503
    sample_result_p2 = solve_p2(*sample_input[1])
    print("Part 2 sample:", sample_answer_p2 == sample_result_p2, sample_result_p2)

    print("Part 2 main:", solve_p2(*main_input[1]))

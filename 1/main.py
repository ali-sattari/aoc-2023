def solution_p1(input: str) -> int:
    nums = []
    with open(input) as file:
        for line in file:
            l = []
            for char in line:
                if char.isdigit():
                    l.append(char)
            nums.append(l)
    
    answer = 0
    for row in nums:
        n = int(f"{row[0]}{row[-1]}")
        answer += n

    return answer

def solution_p2(input: str) -> int:
    digit_words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    nums = []
    with open(input) as file:
        for line in file:
            l = []
            for i, char in enumerate(line):
                if char.isdigit():
                    l.append(char)
                else:
                    for w, d in digit_words.items():
                        if line.startswith(w, i):
                            l.append(d)
            # print(line, l)
            nums.append(l)
    
    answer = 0
    for row in nums:
        n = int(f"{row[0]}{row[-1]}")
        answer += n

    return answer

if __name__ == "__main__":
    p1_sample_answer = 142
    print("Part 1 sample:", solution_p1('./p1_sample.input') == p1_sample_answer)
    print("Part 1 main:", solution_p1('./p1_main.input'))

    p2_sample_answer = 281
    p2_sample_result = solution_p2('./p2_sample.input')
    print("Part 2 sample:", p2_sample_result == p2_sample_answer, p2_sample_result)
    print("Part 2 main:", solution_p2('./p1_main.input'))

def solution_p1(input: str) -> int:
    nums = []
    with open(input) as file:
        for line in file:
            l = []
            for char in line:
                if char.isdigit():
                    l.append(char)
            nums.append(int(f"{l[0]}{l[-1]}"))
    
    return sum(nums)

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
            for i in range(len(line)):
                char = line[i]
                if char.isdigit():
                    l.append(char)
                else:
                    for w, d in digit_words.items():
                        if line.startswith(w, i):
                            l.append(d)
                            # jump ahead by the length of the matched word
                            i += len(w)
                            # why continue once we match any of the words?
                            break
            nums.append(int(f"{l[0]}{l[-1]}"))
    
    return sum(nums)

if __name__ == "__main__":
    p1_sample_answer = 142
    p1_sample_result = solution_p1('./p1_sample.input')
    print("Part 1 sample:", p1_sample_result == p1_sample_answer, p1_sample_result)
    print("Part 1 main:", solution_p1('./p1_main.input'))

    p2_sample_answer = 281
    p2_sample_result = solution_p2('./p2_sample.input')
    print("Part 2 sample:", p2_sample_result == p2_sample_answer, p2_sample_result)
    print("Part 2 main:", solution_p2('./p1_main.input'))

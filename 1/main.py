def solution(input: str) -> int:
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

if __name__ == "__main__":
    p1_sample_answer = 142
    print("Part 1 sample:", solution('./p1_sample.input') == p1_sample_answer)
    print("Part 1 main:", solution('./p1_main.input'))

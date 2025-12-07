# ==========================================
# Python solution for https://adventofcode.com/2025/day/2
# Credit: akeanti
# Description: Gift Shop
# `puzzle_input` should be replaced with your input from : https://adventofcode.com/2025/day/2/input
# ==========================================

def solve_gift_shop(puzzle_input):
    ranges = puzzle_input.replace('\n', '').split(',')
    total_invalid_sum = 0

    for r in ranges:
        if not r.strip():
            continue
        start, end = map(int, r.split('-'))

        for num in range(start, end + 1):
            s_num = str(num)
            length = len(s_num)

            if length % 2 == 0:
                mid = length // 2
                if s_num[:mid] == s_num[mid:]:
                    total_invalid_sum += num

    return total_invalid_sum


puzzle_input = "" # here goes the stuff u got from your input :^)

print(solve_gift_shop(puzzle_input))
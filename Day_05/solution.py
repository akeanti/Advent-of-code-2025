# ==========================================
# Python solution for https://adventofcode.com/2025/day/5
# Credit: akeanti
# Description: Cafeteria Challenge
# data should be replaced with your input from : https://adventofcode.com/2025/day/5/input
# ==========================================

import os

def solve_cafeteria(input_str):
    parts = input_str.strip().split('\n\n')

    range_lines = parts[0].split('\n')
    ranges = []
    for line in range_lines:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    id_lines = parts[1].split('\n')
    ids = [int(line) for line in id_lines]

    fresh_count = 0

    for ingredient_id in ids:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break

        if is_fresh:
            fresh_count += 1

    return fresh_count

with open('input.txt', 'r') as f:
    full_input = f.read()
    print(f"Solution finale : {solve_cafeteria(full_input)}")
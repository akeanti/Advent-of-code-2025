# ==========================================
# Python solution for https://adventofcode.com/2025/day/7
# Credit: akeanti
# Description: Laboratories Part 1 Challenge
# data should be replaced with your input from : https://adventofcode.com/2025/day/7/input
# ==========================================

import os


def solve_teleporter(input_str):
    grid = input_str.strip().split('\n')
    height = len(grid)
    width = len(grid[0])

    current_beams = set()
    split_count = 0

    for c in range(width):
        if grid[0][c] == 'S':
            current_beams.add(c)
            break

    for r in range(height):
        next_beams = set()

        if not current_beams:
            break

        for c in current_beams:
            if not (0 <= c < width):
                continue

            char = grid[r][c]

            if char == '^':
                split_count += 1

                if c - 1 >= 0:
                    next_beams.add(c - 1)
                if c + 1 < width:
                    next_beams.add(c + 1)

            elif char == 'S' or char == '.':
                next_beams.add(c)

        current_beams = next_beams

    return split_count

with open('input.txt', 'r') as f:
    full_input = f.read()
    print(f"Solution finale : {solve_teleporter(full_input)}")
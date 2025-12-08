# ==========================================
# Python solution for https://adventofcode.com/2025/day/7
# Credit: akeanti
# Description: Laboratories Part 2 Challenge
# data should be replaced with your input from : https://adventofcode.com/2025/day/7/input
# ==========================================

import os
from collections import defaultdict


def solve_part2_quantum(input_str):
    grid = input_str.strip().split('\n')
    height = len(grid)
    width = len(grid[0])

    current_counts = defaultdict(int)

    for c in range(width):
        if grid[0][c] == 'S':
            current_counts[c] = 1
            break

    for r in range(height):
        next_counts = defaultdict(int)

        if not current_counts:
            break

        for c, count in current_counts.items():
            # Vérification des bornes (sécurité)
            if not (0 <= c < width):
                continue

            char = grid[r][c]

            if char == '^':

                if c - 1 >= 0:
                    next_counts[c - 1] += count
                if c + 1 < width:
                    next_counts[c + 1] += count

            elif char == 'S' or char == '.':
                next_counts[c] += count


        current_counts = next_counts

    return sum(current_counts.values())

with open('input.txt', 'r') as f:
    full_input = f.read()
    print(f"Solution finale Partie 2 : {solve_part2_quantum(full_input)}")

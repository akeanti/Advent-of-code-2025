# ==========================================
# Python solution for https://adventofcode.com/2025/day/3
# Credit: akeanti
# Description: Lobby Challenge
# data should be replaced with your input from : https://adventofcode.com/2025/day/3/input
# ==========================================

def solve_batteries(input_text):
    total_joltage = 0
    lines = input_text.strip().split('\n')

    print(f"Processing {len(lines)} banks...")

    for line in lines:
        digits = [int(c) for c in line if c.isdigit()]

        if len(digits) < 2:
            continue

        max_bank_joltage = 0

        for i in range(len(digits) - 1):
            tens = digits[i]

            remaining_digits = digits[i + 1:]
            ones = max(remaining_digits)

            joltage = (tens * 10) + ones

            if joltage > max_bank_joltage:
                max_bank_joltage = joltage

        total_joltage += max_bank_joltage

    return total_joltage

# Here goes your input from the ~/Day_03/input.txt, i didn't put it in cuz it's soooooo long (that's what she said XD)
puzzle_input = """
17193
"""

result = solve_batteries(puzzle_input)
print(f"Total Output Joltage: {result}")
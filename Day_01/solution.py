# ==========================================
# Python solution for https://adventofcode.com/2025/day/1
# Credit: akeanti
# Description: Secret Entrance Challenge
# data should be replaced with your input from : https://adventofcode.com/2025/day/1/input
# ==========================================

data = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

pos = 50
ans = 0

lines = data.strip().split('\n')

for line in lines:
    d = line[0]
    val = int(line[1:])

    if d == 'R':
        pos = (pos + val) % 100
    else:
        pos = (pos - val) % 100

    if pos == 0:
        ans += 1

print(ans)
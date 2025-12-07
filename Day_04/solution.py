# ==========================================
# Python solution for https://adventofcode.com/2025/day/4
# Credit: akeanti
# Description: Printing Department Challenge
# data should be replaced with your input from : https://adventofcode.com/2025/day/4/input
# ==========================================

def solve_warehouse(input_str):
    grid = [list(line) for line in input_str.strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    accessible_count = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                neighbor_paper_count = 0

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            neighbor_paper_count += 1

                if neighbor_paper_count < 4:
                    accessible_count += 1

    return accessible_count

# Idk why didn't I think of using this before bruh, no need to copy input and make the code look ugly...
with open('input.txt', 'r') as f:
    full_input = f.read()
    print(f"Solution finale : {solve_warehouse(full_input)}")
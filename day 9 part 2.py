data = open('inputs/day 9.txt').read().splitlines()
matrix = []
risk = 0
for row in data:
    matrix.append([int(item) for item in list(row)])
basins = {}

def get_ending(col, row):
    found = False
    under = []
    for add_row, add_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        new_row = add_row + row
        new_col = add_col + col
        if new_row < 0 or new_row >= len(matrix[0]) or new_col < 0 or new_col >= len(matrix):
            continue
        if matrix[col][row] > matrix[new_col][new_row]:
            under.append([new_col, new_row])
            found = True
    if not found or matrix[col][row] == 9:
        return [col, row]
    if found:
        new_col, new_row = min(under, key=lambda ar:matrix[ar[0]][ar[1]])
        return get_ending(new_col, new_row)

for col in range(len(matrix)):
    for row in range(len(matrix[0])):
        ncol, nrow = get_ending(col, row)
        basins[(ncol, nrow)] = basins.get((ncol, nrow), 0) + 1

basins = sorted(list(basins.values()), reverse=True)
print(basins[0]*basins[1]*basins[2])

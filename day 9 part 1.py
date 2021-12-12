data = open('inputs/day 9.txt').read().splitlines()
matrix = []
risk = 0
for row in data:
    matrix.append([int(item) for item in list(row)])

for col in range(len(matrix)):
    for row in range(len(matrix[0])):
        arr  = []
        for add_row, add_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_row = add_row + row
            new_col = add_col + col
            if new_row < 0 or new_row >= len(matrix[0]) or new_col < 0 or new_col >= len(matrix):
                continue
            arr.append(matrix[col][row] < matrix[new_col][new_row])
        if all(arr):
            risk += (matrix[col][row] + 1)


print(risk)

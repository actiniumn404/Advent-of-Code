data = open('inputs/day 11.txt').read().split("\n")
matrix = []
for x in data:
    matrix.append(list(map(int, list(x))))

def flash(y,x):
    if (y,x) in flashed:
        return
    flashed.add((y,x))
    matrix[y][x] = 0
    for new_x, new_y in [(1,0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (-1, -1), (1, -1)]:
        if y+new_y < 0 or x+new_x < 0 or y+new_y >= len(matrix) or x+new_x >= len(matrix[0]):
            continue
        if (y+new_y,x+new_x) not in flashed:
            matrix[y+new_y][x+new_x] += 1
        if matrix[y+new_y][x+new_x] > 9:
            flash(y+new_y, x+new_x)

s = 0
while True:
    s += 1
    flashed = set()
    buffer = []
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            matrix[y][x] += 1
            if matrix[y][x] > 9:
                buffer.append([y,x])
    for y, x in buffer:
        flash(y, x)

    if matrix == [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]:
        print(s)
        break

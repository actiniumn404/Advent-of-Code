data = list(map(int, open('inputs/day 6.txt').read().split(",")))

for _ in range(80):
    len_data = len(data)
    for i in range(len_data):
        data[i] = data[i] - 1
        if data[i] == -1:
            data[i] = 6
            data.append(8)


print(len(data))

data = open('inputs/day 5.txt').read().splitlines()
points = set()
overlap = set()
for item in data:
    cord1, cord2 = list(map(lambda i: list(map(int,i.split(","))), item.split(" -> ")))
    if cord1[0] == cord2[0]:
        for y in range(min(cord2[1], cord1[1]), max(cord2[1], cord1[1])+1):
            if (cord1[0], y) in points and (cord1[0], y) not in overlap:
                overlap.add((cord1[0], y))
            else:
                points.add((cord1[0], y))
    elif cord1[1] == cord2[1]:
        for y in range(min(cord1[0], cord2[0]), max(cord1[0], cord2[0])+1):
            if (y,cord1[1]) in points and (y,cord1[1]) not in overlap:
                overlap.add((y,cord1[1]))
            else:
                points.add((y,cord1[1]))
    else:
        x = max(cord1, cord2, key=lambda it: it[1])[0]
        y = max(cord1, cord2, key=lambda it: it[1])[1]
        #print(x,y, cord1, cord2)
        increment = 1
        if x > min(cord1, cord2, key=lambda it: it[1])[0]:
            increment = -1
        while [x, y] != min(cord1, cord2, key=lambda it: it[1]):
            if (x,y) in points and (x,y) not in overlap:
                overlap.add((x,y))
            else:
                points.add((x,y))
            x += increment
            y = y - 1
            #print(x,y)

        if (x, y) in points and (x, y) not in overlap:
            overlap.add((x, y))
        else:
            points.add((x, y))

print(len(overlap))

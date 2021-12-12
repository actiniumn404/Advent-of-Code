changes = open('inputs/day 2.txt').read().splitlines()
depth = 0
horizontal = 0
for x in changes:
    command, number = x.split(" ")
    number = int(number)
    if command == "forward":
        horizontal += number
    elif command == "down":
        depth = depth + number
    elif command == "up":
        depth = depth - number

print(depth * horizontal)

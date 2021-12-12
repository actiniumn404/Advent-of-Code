lines = open('inputs/day 10.txt').read().split("\n")
ref = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
score = 0
for line in lines:
    queue = []
    for char in line:
        if char in ["(", "[", "{", "<"]:
            queue.insert(0,ref[char])
        elif queue[0] == char:
            queue.pop(0)
        else:
            score += points[char]
            break

print(score)

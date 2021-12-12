from statistics import median


lines = open('inputs/day 10.txt').read().split("\n")
ref = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
scores = []
for line in list(lines):
    queue = []
    for char in line:
        if char in ["(", "[", "{", "<"]:
            queue.insert(0, ref[char])
        elif queue[0] == char:
            queue.pop(0)
        else:
            lines.remove(line)
            break
    else:
        if queue:
            subres = 0
            for bracket in queue:
                subres *= 5
                subres += points[bracket]
            scores.append(subres)

print(median(scores))

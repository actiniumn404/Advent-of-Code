data = list(map(int, open('inputs/day 6.txt').read().split(",")))
fish = {}
for x in data:
    fish[x] = fish.get(x, 0) + 1

for _ in range(256):
    copy = dict(fish)
    for x in sorted(list(fish.keys())):
        fish[x-1] = copy[x]
        fish.pop(x)
    if fish.get(-1):
        fish[6] = fish.get(6, 0) + fish[-1]
        fish[8] = fish[-1]
        fish.pop(-1)

print(sum(fish.values()))

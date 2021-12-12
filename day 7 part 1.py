data = list(map(int, open('inputs/day 7.txt').read().split(",")))
average = sum(data) // len(data)
left = 0
right = 0
for x in data:
    if x < average:
        left += 1
    elif x > average:
        right += 1

if max(left,right) == left:
    check = range(0, average+1)
else:
    check = range(average, 0)

result = float("inf")

for x in check:
    sub_result = 0
    for y in data:
        sub_result += abs(x-y)
    result = min(result, sub_result)

print(result)

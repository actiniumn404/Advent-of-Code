import requests
data = open("inputs/d1.txt", "r").read().split("\n")
counter = 1
for x in range(1, len(data)):
    if data[x-1] < data[x]:
        counter += 1
print(counter)

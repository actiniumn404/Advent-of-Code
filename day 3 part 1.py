binary = open('inputs/day 3.txt').read().splitlines()
gamma = []
epsilon = []
for i in range(len(binary[0])):
    subdata = [str(binary[j][i]) for j in range(len(binary))]
    gamma.append(max("1", "0", key=lambda k:subdata.count(k)))
    epsilon.append(min("1", "0", key=lambda k:subdata.count(k)))

gamma = int("".join(gamma), 2)
epsilon = int("".join(epsilon), 2)
print(gamma*epsilon)

binary = open('inputs/day 3.txt').read().splitlines()
oxygen = binary[:]
# Oxygen
found = False
for bit_num in range(len(oxygen[0])):
    if found:
        break
    bits = [oxygen[data_index][bit_num] for data_index in range(len(oxygen))]
    count_one = bits.count("1")
    count_zero = bits.count("0")
    if count_zero > count_one:
        most_common = "0"
    else:
        most_common = "1"
    pop_what = []
    for x in oxygen:
        if x[bit_num] != most_common:
            pop_what.append(x)
    for y in pop_what:
        if len(oxygen) == 1:
            found = True
            break
        oxygen.remove(y)

#Carbon Dixode
carbon = binary[:]
found = False
for bit_num in range(len(carbon[0])):
    if found:
        break
    bits = [carbon[data_index][bit_num] for data_index in range(len(carbon))]
    count_one = bits.count("1")
    count_zero = bits.count("0")
    if count_one > count_zero:
        most_common = "0"
    elif count_one < count_zero:
        most_common = "1"
    else:
        most_common = "0"
    pop_what = []
    for x in carbon:
        if x[bit_num] != most_common:
            pop_what.append(x)
    for y in pop_what:
        if len(carbon) == 1:
            found = True
            break
        carbon.remove(y)


print(int(carbon[0], 2)*int(oxygen[0], 2))

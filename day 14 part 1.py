data = open('inputs/day 14.txt').read()
poly = data.split("\n\n")[0]
templates = {k:v for k, v in [x.split(" -> ") for x in data.split("\n\n")[1].split("\n")]}

for _ in range(10):
    poly_edit = poly
    pair_i = 0
    changed = 0
    while pair_i < (len(poly) - 1):
        pair = poly[pair_i] + poly[pair_i+1]
        if templates.get(pair):
            poly_edit = list(poly_edit)
            poly_edit.insert(pair_i+1+changed, templates.get(pair))
            changed += 1
        pair_i += 1
    poly = "".join(poly_edit)

quantity = {}
for item in poly:
    quantity[item] = quantity.get(item, 0) + 1

print(max(list(quantity.values())) - min(list(quantity.values())))

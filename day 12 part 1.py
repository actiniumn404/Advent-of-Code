# A DFS problem finally

def dfs(visited, cave_name, path):
    if cave_name == "end":
        paths_done.add(",".join(path))
        return
    if cave_name in visited:
        return
    if cave_name.lower() == cave_name  or cave_name == "start":
        visited = visited + [cave_name]

    for cave in move[cave_name]:
        dfs(visited, cave, path+[cave_name])

data = open('inputs/day 12.txt').read().split("\n")
move = {}
paths_done = set()
for x in data:
    x = x.split("-")
    move[x[0]] = list(set(move.get(x[0], []) + [x[1]]))
    move[x[1]] = list(set(move.get(x[1], []) + [x[0]]))

dfs([], "start", [])
print(len(paths_done))

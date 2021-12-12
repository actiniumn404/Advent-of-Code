# A DFS problem finally
# It might be a little slow, but it works.
def dfs(visited: list, cave_name: str, path: list, double: str) -> None:
    if cave_name == "end":
        paths_done.add(",".join(path))
        return
    if cave_name in visited:
        return
    if cave_name.lower() == cave_name or cave_name == "start":
        if cave_name == double:
            double = ""
        else:
            visited = visited + [cave_name]
    for cave in move.get(cave_name, []):
        dfs(visited, cave, path+[cave_name], double)

data = open('inputs/day 12.txt').read().split("\n")
move = {}
paths_done = set()
for x in data:
    x = x.split("-")
    move[x[0]] = list(set(move.get(x[0], []) + [x[1]]))
    move[x[1]] = list(set(move.get(x[1], []) + [x[0]]))

for item in move:
    if item.lower() == item and item != "end" and item != "start":
        dfs([], "start", [], item)
print(len(paths_done))

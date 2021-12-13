data = open('inputs/day 13.txt').read()
points = set(data.split("\n\n")[0].split("\n"))
instructions = [x.replace("fold along ", "") for x in data.split("\n\n")[1].split("\n")]
#for instruct in instructions:
instruct = instructions[0]
if instruct[0] == "y":
    axis = int(instruct.split("=")[-1])
    for point in list(points):
        if int(point.split(",")[1]) > axis:
            # Mathy way of doing axis - (point_y - axis)
            new = 2*axis - int(point.split(",")[1])
            points.remove(point)
            points.add(point.split(",")[0]+","+str(new))
else:
    axis = int(instruct.split("=")[-1])
    for point in list(points):
        if int(point.split(",")[0]) > axis:
            # Mathy way of doing axis - (point_y - axis)
            new = 2*axis - int(point.split(",")[0])
            points.remove(point)
            points.add(str(new)+","+point.split(",")[1])


print(len(points))

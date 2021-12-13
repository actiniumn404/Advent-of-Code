data = open('inputs/day 13.txt').read()
points = set(data.split("\n\n")[0].split("\n"))
instructions = [x.replace("fold along ", "") for x in data.split("\n\n")[1].split("\n")]
for instruct in instructions:
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
for x in range(0, int(max(points, key=lambda i: int(i.split(",")[1])).split(",")[1] )+1):
    for y in range(0, int(max(points, key=lambda i: int(i.split(",")[0])).split(",")[0])+1):
        if str(y)+","+str(x) in points:
            print("#", end="")
        else:
            print(" ", end="")

    print("", end="\n")

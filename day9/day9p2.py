with open("input") as infile:
    input_list = infile.readlines()
    input_list = [line[:-1] for line in input_list]


rope_dict = {}

for i in range(10):
    rope_dict[i] = [0, 0]

print(rope_dict)


def movetail(first_knot,second_knot):
    new_knot = [0, 0]
    knot_distance = abs((first_knot[0] - second_knot[0])) + abs((first_knot[1] - second_knot[1]))
    if first_knot[0] in (second_knot[0]-1,second_knot[0],second_knot[0]+1) and \
            first_knot[1] in (second_knot[1]-1,second_knot[1],second_knot[1]+1):
        return second_knot  # Doesn't move
    elif knot_distance == 2:
        if first_knot[0] > second_knot[0]:
            new_knot = [second_knot[0]+1, second_knot[1]]
        if first_knot[0] < second_knot[0]:
            new_knot = [second_knot[0]-1, second_knot[1]]
        if first_knot[1] > second_knot[1]:
            new_knot = [second_knot[0], second_knot[1]+1]
        if first_knot[1] < second_knot[1]:
            new_knot = [second_knot[0], second_knot[1]-1]
        return new_knot
    else:
        if first_knot[0] > second_knot[0] and first_knot[1] > second_knot[1]:
            new_knot = [second_knot[0]+1, second_knot[1]+1]
        if first_knot[0] < second_knot[0] and first_knot[1] > second_knot[1]:
            new_knot = [second_knot[0]-1, second_knot[1]+1]
        if first_knot[0] > second_knot[0] and first_knot[1] < second_knot[1]:
            new_knot = [second_knot[0]+1, second_knot[1]-1]
        if first_knot[0] < second_knot[0] and first_knot[1] < second_knot[1]:
            new_knot = [second_knot[0]-1, second_knot[1]-1]
        return new_knot


visited_coords = [[0, 0]]
for line in input_list:
    line = line.split(sep=" ")
    direction = line[0]
    distance = int(line[1])
    print("Command:", line)
    for rpt in range(distance):

        print("Repeat:", rpt)
        head = rope_dict[0]
        match direction:
            case "U":
                head[1] += 1
            case "D":
                head[1] -= 1
            case "L":
                head[0] -= 1
            case "R":
                head[0] += 1
        print(rope_dict[0][0],",",rope_dict[0][1])
        for knot in range(1, 10):
            rope_dict[knot] = movetail(rope_dict[knot-1],rope_dict[knot])
            print(rope_dict[knot][0],",",rope_dict[knot][1])
        if rope_dict[9] not in visited_coords:
            visited_coords.append(rope_dict[9])


print(len(visited_coords))

"""
....H.
....T.
......
......
s.....
"""
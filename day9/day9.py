with open("input") as infile:
    input_list = infile.readlines()
    input_list = [line[:-1] for line in input_list]


head = [0, 0]
tail = [0, 0]


def movetail():
    if tail[0] in (head[0]-1,head[0],head[0]+1) and tail[1] in (head[1]-1,head[1],head[1]+1):
        print("tail doesn't move")
        return False
    else:
        print("tail moved")
        return True


visited_coords = []
for line in input_list:
    line = line.split(sep=" ")
    direction = line[0]
    distance = int(line[1])
    print(line)
    for rpt in range(distance):
        org_head = list(head)
        match direction:
            case "U":
                head[1] += 1
            case "D":
                head[1] -= 1
            case "L":
                head[0] -= 1
            case "R":
                head[0] += 1
        if movetail():
            tail = org_head
        if tail not in visited_coords:
            visited_coords.append(tail)
        print("head", head, "tail", tail, "org", org_head)
    print()

print(visited_coords)
print(len(visited_coords))

"""
....H.
....T.
......
......
s.....
"""
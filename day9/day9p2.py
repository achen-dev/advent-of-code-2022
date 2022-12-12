with open("testinput") as infile:
    input_list = infile.readlines()
    input_list = [line[:-1] for line in input_list]


rope_dict = {}

for i in range(10):
    rope_dict[i] = [0, 0]

print(rope_dict)

def movetail():
    if tail[0] in (head[0]-1,head[0],head[0]+1) and tail[1] in (head[1]-1,head[1],head[1]+1):
        return False
    else:
        return True


visited_coords = []
for line in input_list:
    line = line.split(sep=" ")
    direction = line[0]
    distance = int(line[1])
    for knot in range(9):
        head = rope_dict[knot]
        tail = rope_dict[knot+1]
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
            if rope_dict[9] not in visited_coords:
                visited_coords.append(rope_dict[9])
            print(head,tail)
        print(knot, head, tail)
print(len(visited_coords))

"""
....H.
....T.
......
......
s.....
"""
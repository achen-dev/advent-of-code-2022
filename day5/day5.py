"""
Initial State:
                    [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9


"""

# PART ONE
state_dict = {}

state_list = ["BQC", "RQWZ", "BMRLV", "CZHVTW", "DZHBNVG", "HNPCJFVQ", "DGTRWZS", "CGMNBWZP", "NJBMWQFP"]

for i in range(1, 10):
    state_dict[i] = [char for char in state_list[i-1]]

with open("input") as infile:
    input_list = infile.readlines()
    input_list = [line[:-1] for line in input_list]

for line in input_list:
    line_list = line.split(sep=" ")
    # print(line_list)
    box_num = int(line_list[1])
    source = int(line_list[3])
    destination = int(line_list[5])
    for repeat in range(box_num):
        state_dict[destination].append(state_dict[source].pop())
        # print(state_dict)


print([i[-1] for i in state_dict.values()])


# PART TWO
state_dict2 = {}

state_list2 = ["BQC", "RQWZ", "BMRLV", "CZHVTW", "DZHBNVG", "HNPCJFVQ", "DGTRWZS", "CGMNBWZP", "NJBMWQFP"]

for i in range(1, 10):
    state_dict2[i] = [char for char in state_list2[i-1]]

for line in input_list:
    line_list = line.split(sep=" ")
    # print(line_list)
    box_num = int(line_list[1])
    source = int(line_list[3])
    destination = int(line_list[5])
    chosen_boxes = state_dict2[source][0-box_num:]
    state_dict2[destination] += chosen_boxes
    # print(line,state_dict2[source], chosen_boxes,state_dict2[destination])
    state_dict2[source] = state_dict2[source][:0-box_num]
    # print(state_dict2[source])

print([i[-1] for i in state_dict2.values()])

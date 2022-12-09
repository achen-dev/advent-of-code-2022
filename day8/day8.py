with open("input") as infile:
    input_list = infile.readlines()
    input_list = [line[:-1] for line in input_list]

#print(input_list)

WIDTH = len(input_list[0])
HEIGHT = len(input_list)


print(WIDTH, HEIGHT)


def visible(height, coords):
    height = int(height)
    x = coords[0]
    y = coords[1]
    candidate_dir = ["U","D","L","R"]
    # If on the edge, already visible
    u_sum = 0
    d_sum = 0
    l_sum = 0
    r_sum = 0
    if x == 0 or x == WIDTH-1 or y == 0 or y == HEIGHT-1:
        candidate_dir.append("E")
    # Check left
    for other_tree in reversed(list(input_list[y][:x])):
        l_sum += 1
        if int(other_tree) >= height:
            candidate_dir.remove("L")
            break

    # Check right
    for other_tree in input_list[y][x+1:]:
        r_sum += 1
        if int(other_tree) >= height:
            candidate_dir.remove("R")
            break

    # Check up
    for line in reversed(list(input_list[:y])):
        u_sum += 1
        if int(line[x]) >= height:
            candidate_dir.remove("U")
            break
    # Check down
    for line in input_list[y+1:]:
        d_sum += 1
        if int(line[x]) >= height:
            candidate_dir.remove("D")
            break

    total_score = u_sum*d_sum*l_sum*r_sum
    print(height,[x,y],  "u", u_sum, "d", d_sum, "l", l_sum,"r", r_sum,"score",total_score)
    if candidate_dir:
        return True,total_score
    else:
        return False,total_score


visible_count = 0
x_cor = 0
y_cor = 0
highest_score = 0
while y_cor < HEIGHT:
    while x_cor < WIDTH:
        current_tree = input_list[y_cor][x_cor]
        results = visible(current_tree,[x_cor,y_cor])
        isvisible = results[0]
        current_score = results[1]
        if current_score > highest_score:
            highest_score = current_score
        if isvisible:
            visible_count += 1
        x_cor += 1
    x_cor = 0
    y_cor += 1

print(visible_count, highest_score)
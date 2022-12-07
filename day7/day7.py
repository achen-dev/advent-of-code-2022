with open("input") as infile:
    input_list = infile.readlines()
    input_list = [line[:-1] for line in input_list]


directory_dict = {}
current_path = []
current_directory = ""

i = 0
while i < len(input_list):
    line = input_list[i]
    print("currently on line", i+1)
    if line == "$ cd ..":
        current_path = current_path[:-1]
        print("move back to ", current_path)
    elif line[:4] == "$ cd":
        current_path.append(line[4:])
        current_directory = line[4:]
        print("move to ", current_path)
    elif line[:4] == "$ ls":
        current_dir_size = 0
        i += 1

        print("starting list")
        while i != len(input_list)-1:
            subline = input_list[i]
            if subline[0] == "d":
                pass
            elif subline[0] == "$":
                i -= 1
                break
            else:
                print("found file", subline)
                line_list = subline.split(sep=" ")
                current_dir_size += int(line_list[0])
            i += 1
        directory_dict["".join(current_path)] = current_dir_size
    i += 1

print(directory_dict.items())
dictionary_items = [list(x) for x in directory_dict.items()]
for parent in dictionary_items:
    for child in dictionary_items:
        if parent[0] == child[0]:
            pass
        elif parent[0] in child[0]:
            parent[1] += child[1]

print(sorted(dictionary_items, key = lambda x:x[1], reverse = True))
valid_items = [i for i in dictionary_items if i[1] <= 100000 and i[1] != 0]
print(valid_items)
print(sum([i[1] for i in valid_items]))
required_new_space = 30000000 - (70000000 - 45089714)
valid_to_del = [i for i in dictionary_items if i[1] >= required_new_space and i[1] != 0]
print(sorted(valid_to_del,reverse=True, key=lambda x:x[1]))
print(sorted(valid_to_del,key=lambda x:x[1]))
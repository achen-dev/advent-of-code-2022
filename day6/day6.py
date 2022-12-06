# Today's code is pretty hacky, wanted to prioritize speed :)

with open("input") as infile:
    input_line = infile.readline()

#print(type(input_line))
initial_list = input_line[:4]
print(initial_list, set([i for i in initial_list]))
for i in range(len(input_line))[4:]:
    initial_list = initial_list[1:]
    initial_list += input_line[i]
    print(initial_list, set([char for char in initial_list]), i)

    if len(set([char for char in initial_list])) == 4:
        print(initial_list, set([char for char in initial_list]))
        print("char i is", input_line[i])
        print(i)
        break

initial_list = input_line[:14]

for i in range(len(input_line))[14:]:
    initial_list = initial_list[1:]
    initial_list += input_line[i]
    print(initial_list, set([char for char in initial_list]), i)

    if len(set([char for char in initial_list])) == 14:
        print(initial_list, set([char for char in initial_list]))
        print("char i is", input_line[i])
        print(i)
        break

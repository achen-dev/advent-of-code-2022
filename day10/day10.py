with open("input") as infile:
    input_list = infile.readlines()
    input_list = [line[:-1] for line in input_list]

cycle = 0
X = 1
cycle_dict = {}
for line in input_list:
    cycle_dict[cycle] = X
    if line == "noop":
        cycle += 1
        cycle_dict[cycle] = X
    else:
        cycle += 1
        cycle_dict[cycle] = X
        cycle += 1
        cycle_dict[cycle] = X
        X += int(line.split()[1])

sum = 0
for i in (20,60,100,140,180,220):
    sum += i*cycle_dict[i]

print(sum)
output_string = ""
for i in cycle_dict:
    sprite_range = (cycle_dict[i]-1, cycle_dict[i], cycle_dict[i]+1)
    print(sprite_range,i)
    if i % 40 in sprite_range:
        output_string += "#"
        print("add #")
    else:
        output_string += "."
        print("add .")
    if (i+1) % 40 == 0:
        output_string += "\n"
print(output_string)

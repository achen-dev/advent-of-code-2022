value_dictionary = {}
alphabet_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = 1
for char in alphabet_string:
    value_dictionary[char] = i
    i += 1

with open("input") as infile:
    input_list = infile.readlines()
    input_list = [line[:-1] for line in input_list]

part1_total_priorities = 0
for item in input_list:
    part1 = item[:len(item)//2]
    part2 = item[len(item)//2:]
    crossover = [value for value in part1 if value in part2]
    part1_total_priorities += value_dictionary[crossover[0]]

print(part1_total_priorities)

part2_total_priorities = 0
group_list = []
i = 0
for item in input_list:
    group_list.append(item)
    i += 1
    if i == 3:
        item1 = group_list[0]
        item2 = group_list[1]
        item3 = group_list[2]
        crossover2 = [value for value in item1 if value in item2 and value in item3]
        part2_total_priorities += value_dictionary[crossover2[0]]
        # print(item1,item2,item3,crossover2)
        i = 0
        group_list = []


print(i,part2_total_priorities)

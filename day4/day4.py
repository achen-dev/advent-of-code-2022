with open("input") as infile:
    input_list = [line[:-1] for line in infile.readlines()]

print(input_list)

range_list = [line.split(sep=",")for line in input_list]
print(range_list[:4])

overlap_count = 0
contained_count = 0
for item in range_list:
    item_int = []
    for part in item:
        split_part = [int(i) for i in part.split(sep="-")]
        item_int.append(split_part)
    print(item_int)
    item_int.sort(key = lambda x: x[1]-x[0])
    print(item_int)
    part1 = item_int[0]
    part2 = item_int[1]
    if part1[0] >= part2[0] and part1[1] <= part2[1]:
        contained_count += 1
        print(item_int, "counted")
    part1_list = [i for i in range(part1[0], part1[1]+1)]
    part2_list = [i for i in range(part2[0], part2[1]+1)]
    overlap = [i for i in part1 if i in part2_list]
    if overlap:
        overlap_count += 1


print(contained_count, overlap_count)



#print(range_list[:4])
# 98-99 , 99-99
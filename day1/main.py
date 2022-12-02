class Elf:
    def __init__(self, name, carried_calories):
        self.name = name
        self.carried_calories = carried_calories




if __name__ == "__main__":
    elf_list = []
    with open("input") as infile:
        sum_cal = 0
        counter = 0
        for line in infile.readlines():
            if line == "\n":
                new_elf = Elf(counter, sum_cal)
                sum_cal = 0
                elf_list.append(new_elf)
                counter += 1
            else:
                sum_cal += int(line)
    max_cal = 0
    for elf in elf_list:
        if elf.carried_calories > max_cal:
            max_cal = elf.carried_calories

        print(elf.name,elf.carried_calories)
    print(max_cal)

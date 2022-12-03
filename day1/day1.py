FILEPATH = "input"

class Elf:
    def __init__(self, name, carried_calories):
        self.name = name
        self.carried_calories = carried_calories


def read_calories(filepath):
    """
    Reads calories from file and creates a list of elfs with carried calories
    :param filepath:
    :return:
    """
    elf_list = []
    with open(filepath) as infile:
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
    return elf_list


if __name__ == "__main__":
    elf_list = read_calories(FILEPATH)
    max_cal = 0
    for elf in elf_list:
        if elf.carried_calories > max_cal:
            max_cal = elf.carried_calories
    elf_list.sort(key = lambda x:x.carried_calories, reverse = True)
    print(sum([item.carried_calories for item in elf_list[:3]]))
    print(max_cal)

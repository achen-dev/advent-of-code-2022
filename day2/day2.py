"""
Part 1:
X, A = Rock 1
Y, B = Paper 2
Z, C = Scissors 3

Part 2:
X = Lose
Y = Draw
Z = Win
"""


def score_round_part1(me, elf):
    score = 0
    match me:
        case "X":
            score += 1
            match elf:
                case "A":
                    score += 3
                case "C":
                    score += 6
        case "Y":
            score += 2
            match elf:
                case "B":
                    score += 3
                case "A":
                    score += 6
        case "Z":
            score += 3
            match elf:
                case "C":
                    score += 3
                case "B":
                    score += 6
    return score


def score_round_part2(me, elf):
    score = 0
    match me:
        case "X":
            score += 0
            match elf:
                case "A":
                    score += 3
                case "B":
                    score += 1
                case "C":
                    score += 2
        case "Y":
            score += 3
            match elf:
                case "A":
                    score += 1
                case "B":
                    score += 2
                case "C":
                    score += 3
        case "Z":
            score += 6
            match elf:
                case "A":
                    score += 2
                case "B":
                    score += 3
                case "C":
                    score += 1
    return score


with open("input") as infile:
    input_list = infile.readlines()
    [line.rstrip('\n') for line in input_list]

total_score_p1 = 0

for item in input_list:
    my_hand = item[2]
    elf_hand = item[0]
    total_score_p1 += score_round_part1(my_hand,elf_hand)

total_score_p2 = 0

for item in input_list:
    my_hand = item[2]
    elf_hand = item[0]
    total_score_p2 += score_round_part2(my_hand,elf_hand)

print(total_score_p1)
print(total_score_p2)



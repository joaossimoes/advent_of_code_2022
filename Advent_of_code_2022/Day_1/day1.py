
def main():
    input = open("Day_1/input")

    calories_per_elf = AddEachElfCalories(input)
    part_1 = max(calories_per_elf)
    print("Part 1 answer is: ", part_1)
    
    GetTopThree(calories_per_elf)

def AddEachElfCalories(input):
    calories_sum = 0
    full_calories_list = []
    for line in input:
        if line.strip() == "":
            full_calories_list.append(calories_sum)
            calories_sum = 0
        else:
            calories_sum += int(line.strip())
    return full_calories_list

def GetTopThree(calories_per_elf):
    calories_per_elf = sorted(calories_per_elf, reverse = True)
    part_2 = calories_per_elf[0] + calories_per_elf[1] + calories_per_elf[2]
    print("Part 2 answer is: ", part_2)

if __name__ == "__main__":
    main()
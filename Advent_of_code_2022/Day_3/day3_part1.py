import string

def main():
    rawInput = open("Advent_of_code_2022/Day_3/input_sample", "r")
    points_dictionary = AtributtePointsToLetters()

    repeated_letters = CreateRepeatsList(rawInput)
    rawInput.close()
    total_points = AddPoints(repeated_letters, points_dictionary)
    print("Part 1 answer is: ", total_points)

    rawInput = open("Advent_of_code_2022/Day_3/input", "r")
    badges = BadgeFinder(rawInput)
    total_badges = AddPoints(badges, points_dictionary)
    print("Part 2 answer is: ", total_badges)

def BadgeFinder(input):
    elf_number = 1
    elf_group = []
    badges = []
    for line in input:
        rucksack = line.strip()
        elf_group.append(rucksack)
        elf_number += 1
        if elf_number == 4:
            for rucksack in elf_group:
                for item in rucksack:
                    if item in elf_group[1] and item in elf_group[2]:
                        badges.append(item)
                        break
                break
            elf_group = []
            elf_number = 1
    return badges

def CreateRepeatsList(input):
    repeated_letters = []
    for line in input:
        line = line.strip() 
        first_compartiment, second_compartiment = line[:len(line)//2], line[len(line)//2:]
        repeated_letters_compartiment = []
        #I need to account for repeated letters in both rucksacks, so I use a list for each rucksack and a list for the overall
        for letter in first_compartiment:
            if letter in second_compartiment:
                if letter not in repeated_letters_compartiment:
                    repeated_letters_compartiment.append(letter)
        for letter in repeated_letters_compartiment:
            repeated_letters.append(letter)
    return repeated_letters
    
def AddPoints(repeated_letters, points_dictionary):
    total_points = 0
    for letter in repeated_letters:
        if letter.isupper():
            points_worth = points_dictionary[letter.lower()] + 26
        else:
            points_worth = points_dictionary[letter]
        total_points += points_worth
    return total_points

def AtributtePointsToLetters():
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    return values




if __name__ == "__main__":
    main()
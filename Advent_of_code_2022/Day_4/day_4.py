
def main():
    rawInput = open("Advent_of_code_2022/Day_4/input", "r")
    sections_ones, sections_twos = GetSections(rawInput)
    containded_sections, partial_overlaps = FindContainedSections(sections_ones,sections_twos)
    print("Part1 answer is: ", containded_sections)
    print("Part2 answer is: ", partial_overlaps)

def GetSections(input):
    elf_ones = []
    elf_twos = []
    for line in input:
        line = line.strip()
        elf1_section, elf2_section = line.split(",")
        elf1_section = (elf1_section.split("-"))
        elf_ones.append(elf1_section)
        elf2_section = (elf2_section.split("-"))
        elf_twos.append(elf2_section)
    return elf_ones, elf_twos

def FindContainedSections(ones, twos):
    group_number = 0
    number_contained = 0
    partial_overlap = 0
    for section in ones:
        if int(section[0]) <= int(twos[group_number][0]) and int(section[1]) >= int(twos[group_number][1]):
            print(section[0])
            number_contained += 1 
        elif int(section[0]) >= int(twos[group_number][0]) and int(section[1]) <= int(twos[group_number][1]):
            number_contained += 1
        if int(section[1]) < int(twos[group_number][0]) or int(section[0]) > int(twos[group_number][1]):
            pass
        else:
            partial_overlap += 1
        group_number += 1
    return number_contained, partial_overlap

if __name__ == "__main__":
    main()
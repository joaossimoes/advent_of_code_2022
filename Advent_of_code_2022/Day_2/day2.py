def main():
    input = open("Day_2/input")
    points_dictionary = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}

    elfs_hands, my_hands = GetListsOfHands(input, points_dictionary)

    points = CalculatePoints(elfs_hands, my_hands)
    print("Part 1 answer is: ", points)

    my_real_hands = ConstructMyHands(elfs_hands, my_hands)
    points = CalculatePoints(elfs_hands, my_real_hands)
    print("Part 2 answer is: ", points)

    

def GetListsOfHands(input, points_dictionary):
    elfs_hands_list = []
    my_hands_list = []
    for line in input:
        line = line.strip()
        elfs_hand, my_hand = line.split(" ")
        #exchange letters by number of points that each represent, like this I can then compare int values when
        #calculating who wins
        elfs_hands_list.append(points_dictionary[elfs_hand])
        my_hands_list.append(points_dictionary[my_hand])
    return elfs_hands_list, my_hands_list

def CalculatePoints(elfs_hands, my_hands):
    index = 0
    win_bonus = 6
    draw_bonus = 3
    lose_bonus = 0
    total_points = 0
    for hand in elfs_hands:
        if hand == 1 and my_hands[index] != 1:
            if my_hands[index] == 2:
                points = int(my_hands[index]) + win_bonus
            else:
                points = int(my_hands[index]) + lose_bonus
        elif hand == 2 and my_hands[index] != 2:
            if my_hands[index] == 3:
                points = int(my_hands[index]) + win_bonus
            else:
                points = int(my_hands[index]) + lose_bonus
        elif hand == 3 and my_hands[index] != 3:
            if my_hands[index] == 1:
                points = int(my_hands[index]) + win_bonus
            else:
                points = int(my_hands[index]) + lose_bonus
        else:
            points = int(my_hands[index]) + draw_bonus
        index += 1
        total_points += points
    return total_points


def ConstructMyHands(elfs_hands, my_hands):
    index = 0
    my_hand = 0
    my_instructions = []
    for elf_hand in elfs_hands:
        #I need to lose
        if my_hands[index] == 1:
            my_hand = elf_hand - 1
            if my_hand == 0:
                my_hand = 3
        #I need to draw
        elif my_hands[index] == 2:
            my_hand = elf_hand
        #Here I need to win
        elif my_hands[index] == 3:
            my_hand = elf_hand + 1
            if my_hand == 4:
                my_hand = 1

       
        my_instructions.append(my_hand)
        index += 1
    print(my_instructions)
    return my_instructions





if __name__ == "__main__":
    main()
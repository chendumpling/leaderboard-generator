#!/usr/bin/env python3
import sys
import fileinput

def main():
    
    first_row = True
    all_lines = copy_file(fileinput.input())
    
    # Dictionary to store row and column formatting info.
    columns_init = {}
    columns_init[0] = len("Participant") + 3
    columns_init[1] = len("Overall") + 3 # could be written as "Avg"

    # score_data = {} # Dunno if I should make this a list or dict


    columns_init = update_participants_length(columns_init, all_lines)
    print("```py")

    # iterates the file line-by-line
    for i in range(len(all_lines)):

        if first_row == True:

            # Checks how many categories there are and updates them
            columns_init, category_list = update_categories(all_lines[i], columns_init)
            columns_init = print_header_row(all_lines[i], columns_init, category_list)
            first_row = False
            continue

    # result = make_leaderboard(columns_init, result) # this will order participants by Overall score

    # print_result(result)

    print("```")

def copy_file(input):
    """
    Copies input file to a list of lines for reusability
    """
    lines = []
    for this_line in fileinput.input():
        lines.append(this_line)

    return lines



def update_participants_length(columns_init, all_lines):
    """
    Check if all participant name length is longer than the "Participant" word itself + 1 character
    If so, make columns_init['Participant'] = new_participant_name_length + 3
    """
    all_participants = []
    first_row1 = True
    
    # iterates the file line-by-line
    for i in range(len(all_lines)):

        if first_row1 == True:
            first_row1 = False
            continue

        all_words_and_nums = all_lines[i].split()
        participant_name = ""

        for i in range(len(all_words_and_nums)):

            if all_words_and_nums[i].isdigit():
                break

            participant_name += all_words_and_nums[i] + " "

        all_participants.append(participant_name.rstrip())

    for i in range(len(all_participants)):

        # Checks if participant name is longer than "Participant"
        if len(all_participants[i]) > columns_init[0]:
            columns_init[0] = len(all_participants[i]) + 3

    return columns_init

def update_categories(line, columns_init):
    """
    Sets the categories of the leaderboard
    """
    category_list = line.split() 
    
    for i in range(2, len(category_list) + 2):
        columns_init[i] = {}
        columns_init[i][category_list[i-2]] = len(category_list[i-2]) + 3

    return columns_init, category_list


def print_header_row(line, columns_init, category_list):

    print(" " + ' '*2, end = "")
    print(' '*columns_init[0], end = "")
    print("Overall" + ' '*3, end = "")

    for i in range(2, len(columns_init)):

        print(category_list[i-2] + ' '*(columns_init[i][category_list[i-2]] - len(category_list[i-2])), end = "")

    print()
    return columns_init

"""
def make_leaderboard(columns_init, result):

    




    return result
    
"""

if __name__ == "__main__":
    main()
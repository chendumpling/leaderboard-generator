#!/usr/bin/env python3
import sys
import fileinput

def main():
    
    first_row = True
    all_lines = copy_file(fileinput.input())
    
    # Dictionary to store row and column formatting info.
    columns_init = {}
    columns_init['Participant'] = len("Participant") + 3
    columns_init['Score'] = len("Score") + 3

    columns_init = update_participants_length(columns_init, all_lines)
    
    # iterates the file line-by-line
    for i in range(len(all_lines)):

        # Prints the header row
        if first_row == True:

            # Checks how many categories there are and updates them
            columns_init = update_categories(all_lines[i], columns_init)
            columns_init = print_header_row(all_lines[i], columns_init)
            first_row = False
            continue

        # Prints the formatted rows
        # print_leaderboard(all_lines[i], columns_init)

    # newline at the end of the file
    # print() 
    
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

        if len(all_participants[i]) > columns_init['Participant']:
            columns_init['Participant'] = len(all_participants[i]) + 3

        print(all_participants[i])

    return columns_init

def update_categories(line, columns_init):
    """
    Sets the categories of the leaderboard
    """
    category_list = line.split() 
    
    for i in range(len(category_list)):
        columns_init[i] = {}
        columns_init[i][category_list[i]] = len(category_list[i]) + 3
        
        print(category_list[i] + " " + str(columns_init[i][category_list[i]]))

    return columns_init


def print_header_row(line, columns_init):

    for i in range(len(columns_init)):

        print(columns_init[i])


    return columns_init

"""
def print_leaderboard(line, columns_init):

    for i in range(len(columns_init)):
"""

if __name__ == "__main__":
    main()
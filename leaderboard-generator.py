#!/usr/bin/env python3
import sys
import fileinput

def main():
    
    first_row = True
    

    # Creates dictionary to store row and column formatting info.
    # Can be changed later by adding columns['NewColName'] = value
    columns_init = {}
    columns_init['Participant'] = len("Participant") + 3
    columns_init['Score'] = len("Score") + 3

    columns_init = update_participants_length(columns_init)
    
    
    # for each line in the file or stdin (this iterates by line)
    for this_line in fileinput.input():



        # Prints the header row
        if first_row == True:

            # Checks how many categories there are and updates them
            columns_init = update_categories(this_line, columns_init)
            # columns_init = print_header_row(this_line, columns_init)
            first_row = False
            continue

        # Prints the formatted rows
        # print_leaderboard(this_line, columns_init)

    # newline at the end of the file
    # print() 
    

def update_participants_length(columns_init):

    # Check if all participant name length is longer than the "Participant" word itself + 1 character
    # If so, make columns_init['Participant'] = new_participant_name_length + 3
    
    all_participants = []
    first_row = True
    
    for this_line in fileinput.input():

        if first_row == True:
            first_row = False
            continue

        all_words_and_nums = this_line.split()
        participant_name = ""

        for i in range(len(all_words_and_nums)):

            if all_words_and_nums[i].isdigit():
                break

            participant_name += all_words_and_nums[i] + " "

        all_participants.append(participant_name.rstrip())

    for i in range(len(all_participants)):

        if len(all_participants[i]) > columns_init['Participant']:
            columns_init['Participant'] = len(all_participants[i]) + 3

    return columns_init

def update_categories(line, columns_init):

    category_list = line.split() 

    for i in range(len(category_list)):
        columns_init[i] = {}
        columns_init[i][category_list[i]] = len(category_list[i] + 3)

    return columns_init

"""
def print_header_row(line, columns_init):

    for i in range(len(columns_init)):



    return columns_init

def print_leaderboard(line, columns_init):

    for i in range(len(columns_init)):
"""

if __name__ == "__main__":
    main()
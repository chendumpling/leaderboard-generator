#!/usr/bin/env python3
import sys
import fileinput

def main():
    
    first_row = True
    # for each line in the file or stdin (this iterates by line)
    for this_line in fileinput.input():

        # Creates dictionary to store row and column formatting info.
        # Can be changed later by adding columns['NewColName'] = value
        columns_init = {}
        columns_init['Participant'] = len("Participant") + 3
        columns_init['Score'] = len("Score") + 3

        # Check if all participant name length is longer than the "Participant" word itself + 1 character
        # If so, make columns_init['Participant'] = new_participant_name_length + 3


        # Prints the header row
        if first_row == True:
            columns_init, first_row = print_header_row(this_line, columns_init, first_row)

        # Prints the formatted lines and updates length
        columns_init = print_leaderboard(this_line, columns_init)

    # newline at the end of the file
    print() 

def print_header_row(line, columns_init, first_row):

    for i in range(len(columns_init)):


    # No longer at header row
    first_row = False

    return columns_init, first_row

def print_leaderboard(line, columns_init):

    for i in range(len(columns_init)):


    return columns_init

if __name__ == "__main__":
    main()

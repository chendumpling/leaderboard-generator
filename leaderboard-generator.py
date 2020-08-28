#!/usr/bin/env python3
import sys
import fileinput

spacing = 3

def main():
    
    first_row = True
    all_lines = copy_file(fileinput.input())
    results = []
    results_in_order = []
    
    # Dictionary to store row and column formatting info (acts like an array)
    columns_init = {}
    columns_init[0] = 0
    columns_init[1] = len("Overall") + spacing # could be written as "Avg"

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

        results = set_scores(all_lines[i], columns_init) # this will generate a list of all dictionaries of participants
        print(results)

    # results_in_order = make_leaderboard(columns_init, results) # this will order participants by Overall score

    # print_result(results_in_order)

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

        participant_name = get_participant_name(all_lines[i])
        all_participants.append(participant_name)

    for i in range(len(all_participants)):

        # Checks if participant name is longer than "Participant"
        if len(all_participants[i]) > columns_init[0]:
            columns_init[0] = len(all_participants[i]) + spacing

    return columns_init

def get_participant_name(line):

    all_words_and_nums = line.split()
    participant_name = ""

    for i in range(len(all_words_and_nums)):

        if all_words_and_nums[i].isdigit():
            break

        participant_name += all_words_and_nums[i] + " "

    return participant_name.rstrip()

def update_categories(line, columns_init):
    """
    Sets the categories of the leaderboard
    """
    category_list = line.split() 
    
    for i in range(2, len(category_list) + 2):
        columns_init[i] = {}
        columns_init[i][category_list[i-2]] = len(category_list[i-2]) + spacing

    return columns_init, category_list


def print_header_row(line, columns_init, category_list):

    print(' '*spacing, end = "")
    print(' '*columns_init[0], end = "")
    print("Overall" + ' '*spacing, end = "")

    for i in range(2, len(columns_init)):

        print(category_list[i-2] + ' '*(columns_init[i][category_list[i-2]] - len(category_list[i-2])), end = "")

    print()
    return columns_init

def get_participant_scores(line):

    all_words_and_nums = line.split()
    participant_scores = []

    for i in range(len(all_words_and_nums)):

        if all_words_and_nums[i].isdigit():
            participant_scores.append(all_words_and_nums[i])

    return participant_scores

def set_scores(line, columns_init):

    
    scores = get_participant_scores(line)

    # Checks if the scores are properly written
    if not len(scores) == (len(columns_init) - 3):
        print ("Scoring criteria missing")
        return

    scores_data = [0] * (len(scores)+2)

    # Gets participant name
    scores_data[0] = get_participant_name(line)

    # Puts all score data in score_data
    scores_average = 0 
    for i in range(len(scores)):
        scores_average += float(scores[i])
    scores_data[1] = float('{:.2f}'.format(scores_average/len(scores))) # Overall calculated score, can maybe remove float() for extra decimal places

    for i in range(len(scores)):
        scores_data[i+2] = int(scores[i])

    return scores_data

"""
def make_leaderboard(columns_init):

    result = []
    score_data = {}




    
    for i in range(len(result)):




    return result
"""


    


if __name__ == "__main__":
    main()
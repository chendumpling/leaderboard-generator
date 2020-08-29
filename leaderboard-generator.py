#!/usr/bin/env python3
import sys
import fileinput

# You can change these
spacing = 3 # positive integer
first_col = "Score"

def main():
    
    all_lines = copy_file(fileinput.input())
    scores = []
    results = []
    categories = []
    
    # array to store column info
    columns = [0]
    columns.append(len(first_col) + spacing) # could be written as "Avg"
    columns = update_participants_length(columns, all_lines)
    
    print("```py")

    # first line of file
    columns, categories = update_categories(all_lines[0], columns)
    columns = print_header_row(all_lines[0], columns, categories)

    # iterates the file line-by-line
    for i in range(1, len(all_lines)):
        scores.append(set_scores(all_lines[i], columns))

    sort_scores(scores)
    make_leaderboard(columns, scores, categories)

    print("```")

def copy_file(input):
    """
    Purpose: Copies input file to a list of lines for reusability.
    Example: "sample_input.txt" gets stored line-by-line in a list
    """
    lines = []
    for this_line in fileinput.input():
        lines.append(this_line)
    return lines

def update_participants_length(columns, all_lines):
    """
    Purpose: Records the length for the longest participant name.
    Example: The longest participant name is "A very very long name"
             so the length of it (21) is stored.
    """
    all_participants = []
    
    # iterates the file line-by-line
    for i in range(1, len(all_lines)):

        participant_name = get_participant_name(all_lines[i])
        all_participants.append(participant_name)

    # compares all names and stores the length of the longest
    for i in range(len(all_participants)):
        if (len(all_participants[i]) + spacing) > (columns[0]):
            columns[0] = len(all_participants[i]) + spacing

    return columns

def get_participant_name(line):
    """
    Purpose: Retrieves a participant's name from the line.
    Example: "Eric Simon 3 5 10" returns "Eric Simon"
    """
    all_words_and_nums = line.split()
    participant_name = ""
    for i in range(len(all_words_and_nums)):
        if all_words_and_nums[i].isdigit():
            break
        participant_name += all_words_and_nums[i] + " "
    return participant_name.rstrip()

def update_categories(line, columns):
    """
    Purpose: Sets the categories of the leaderboard. The values of these
             will be averaged to calculate the overall score.
    Example: "Performance Difficulty Accuracy" will return
             [Performance, Difficulty, Accuracy]
    """
    categories = line.split() 
    for i in range(2, len(categories) + 2):
        columns.append(len(categories[i-2]) + spacing)
    return columns, categories

def print_header_row(line, columns, categories):
    """
    Purpose: Takes category data and prints the header row of the leaderboard.
    Example: With "Performance Difficulty Accuracy" 
             being the first row of the input file, the output would be 
             "                            Score  Performance  Difficulty  Accuracy"
             Note: the blank space is intended.
    """
    print(' '*5, end = "") # spacing for "[1]  "
    print(' '*columns[0], end = "") # spacing for participant name
    
    # prints spacing for columns
    print(first_col + ' '*spacing, end = "")
    for i in range(2, len(columns) - 1):
        print(categories[i-2] + ' '*(columns[i] 
        - len(categories[i-2])), end = "")

    # doesn't print spacing for the last column, and adds a new line
    print(categories[len(columns) - 3])

    return columns

def set_scores(line, columns):
    """ 
    Purpose: Retrieves a participant's info from the line, calculates 
             average score and stores it in a list.
    Example: "Eric Simon 3 5 10" returns ['Eric Simon', 3.67, 3, 5, 3]
    """
    scores = get_participant_scores(line)

    # checks if scores are properly written
    if not len(scores) == (len(columns) - 2):
        print ("Scoring criteria missing")
        return

    scores_data = [0] * (len(scores)+2)
    scores_average = 0

    # participant name (ie 'Eric Simon')
    scores_data[0] = get_participant_name(line)

    # average of all category scores (ie 3.67)
    for i in range(len(scores)):
        scores_average += float(scores[i])
    scores_data[1] = '{:.2f}'.format(scores_average/len(scores))

    # individual category scores (ie [3, 5, 3])
    for i in range(len(scores)):
        scores_data[i+2] = int(scores[i])

    return scores_data

def get_participant_scores(line):
    """
    Purpose: Retrieves a participants score from the line.
    Example: "Eric Simon 3 5 10" returns [3, 5, 3]
    """
    all_words_and_nums = line.split()
    participant_scores = []

    for i in range(len(all_words_and_nums)):

        # store all scores in the list
        if all_words_and_nums[i].isdigit():
            participant_scores.append(int(all_words_and_nums[i]))

    return participant_scores

def sort_scores(scores):
    """
    Purpose: Sorts the score's list based on the participant's overall score.
    Example: [['Eric Simon', '4.00', 4, 5, 3], 
              ['Robert Chen', '9.00', 10, 9, 8], 
              ['GiantUnicorn', '2.00', 1, 2, 3]] 
             becomes 
             [['Robert Chen', '9.00', 10, 9, 8], 
              ['Eric Simon', '4.00', 4, 5, 3], 
              ['GiantUnicorn', '2.00', 1, 2, 3]] 
    """
    scores.sort(key = lambda x: x[1], reverse = True) 
    return scores

def make_leaderboard(columns, scores, categorie):
    """
    Purpose: Formats all the information into a leaderboard that can be copied
             into Discord as a markdown.
    Example: See "sample_output.txt"
    """
    for i in range(len(scores)):

        # prints the placement number and accounts for spacing
        print('[' + str(i+1) + ']' + ' '*(3 - len(str(i+1))), end = "")

        # prints spacing for columns
        for j in range(len(scores[i]) - 1):

            print(str(scores[i][j]) + ' '*(columns[j]
            - len(str(scores[i][j]))), end = "")

        # doesn't print spacing for the last column, and adds a new line
        print(str(scores[i][j]))

    return

if __name__ == "__main__":
    main()
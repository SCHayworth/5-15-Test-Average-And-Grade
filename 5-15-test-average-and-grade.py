# 5-15 Test Average and Grade
# Shaun Hayworth
# CIS 2
# 11-16-2019
# Source code and revision history are available at
# https://github.com/SCHayworth/5-15-Test-Average-And-Grade

# Program gets 5 test scores from the user, determines the letter grade for
# each one, and then determines the letter grade for the average of all 5.

# Import the Python math module.
import math

# Create a constant for the table header
TABLE_HEAD = """
score        numeric grade    letter grade
----------------------------------------------------"""


def main():
    '''Mainline program logic
    '''
    # Get a list of 5 test scores from the user
    score_counter = 0
    test_scores = []
    while score_counter < 5:
        new_score = int(input(f'Enter test score {len(test_scores) + 1}: '))
        test_scores.append(new_score)
        score_counter += 1

    # Find the average of all the test scores.
    average_score = calc_average(test_scores)

    # Print the teable header, and print the scores and grades beneath it.
    print(TABLE_HEAD)
    for score in test_scores:
        print(f'Score {(len(test_scores) - score_counter) + 1}:          {score}             {determine_grade(score)}')
        score_counter -= 1
    print('----------------------------------------------------')

    # Print the average test score and its letter grade.
    print(f'Average score:      {average_score}        {determine_grade(average_score)}')


def calc_average(score_list):
    '''Calculates the average of a list of test scores and returns the result.
    '''
    average = math.fsum(score_list) / len(score_list)
    return average


def determine_grade(score):
    '''Returns a letter grade for a test score passed into the function.
    '''
    if score >= 90:
        return 'A'
    elif score >= 80 and score <= 89:
        return 'B'
    elif score >= 70 and score <= 79:
        return 'C'
    elif score >= 60 and score <= 69:
        return 'D'
    else:
        return 'F'

# Call the main() function to execute the program.
main()

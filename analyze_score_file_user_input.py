import pandas as pd
import sys
import argparse


def parse_score_file(filename):

    """This function splits the score file into headers and the decoy
    score data. It returns two variables: a list of headers and a list
    of scores for each decoy. For each decoy, the individual score
    terms are returned as a list inside the list. The score terms are
    still strings and are NOT converted to float or other appropriate
    data types.
    This is a helper function that you may treat as a black box.
    """

    score_file = open(filename).readlines()
    headers = score_file[1].split()[1:]  # isolate the column headers
    # now make a list of lists where all subsequent entries are split up
    score_data = [line.split()[1:] for line in score_file[2:]]

    # a quick check to make sure there are no problematic entries
    for scores in score_data:
        if len(scores) != len(headers):
            sys.exit('Error in input file at decoy ' + scores[-1] + '.')

    return headers, score_data


def main():

    """Insert code here to analyze score file with user input

    Till now we have hardcoded file names and metrics to display. In
    this script we will accept the file name and the analysis metric
    from the user through the command line. To do so, we will parse
    arguments using the argparse module.

    Start by asking the user for the path to the score file and then
    follow the same instructions as the previous question till before
    printing out mean and median values of Fnat, i.e select by
    CAPRI_rank = 3, sort by I_sc and filter relevant columns.

    Now, offer the user a choice of selecting the metric for analysis.
    Valid choices are Fnat, rms, Irms, and total_score. The default
    should be Fnat. Also, ask how many of the top and bottom scoring
    rows they want the metric for. Ensure that the input is an integer.
    The default value should be 3. Later, you will need to ensure that
    this integer is not larger than the total number of available rows.
    If it is, use sys.exit() and throw a relevant error message.

    For example, 1) the command line

    python3 analyze_score_file_user_input.py --src fixed_docking_score.sc
    --metric Irms --nrows 5

    should produce a valid output.

    2) The command line

    python3 analyze_score_file_user_input.py --src docking_score.sc
    --metric Irms --nrows 5

    should exit in the above written helper function.

    3) The command line

    python3 analyze_score_file_user_input.py --s fixed_docking_score.sc
    -n 5 -m Irms

    should do the same thing as case 1.
    """


main()

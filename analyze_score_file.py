import pandas as pd
import sys


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

    headers, score_data = parse_score_file('docking_score.sc')
    print(headers, score_data)

    """Insert code here to analyze score file

    We will now use the fixed score file to do further analysis using 
    pandas data frames. The helper function above splits the score file
    into the header columns and a list of decoy score terms. (You might
    want to print out the variables, headers and score_data to better
    understand the organization of these variables.)
    
    Hint: while making the data frame use dtype=float to convert all
    relevant score terms to float. To verify the data types of each
    column, use <dataframe_name>.dtypes. Only the description column 
    should be a non-float object.
    
    The score file has three evaluation metrics that we'll use:
    1)  CAPRI_rank. 3 = High-quality model, 2 = Medium-quality model,
        1 = Acceptable model, 0 = Incorrect model
    2)  Fnat = Fraction of native contacts recovered. 1 = all contacts
        recovered and 0 = no contacts recovered.
    3)  I_sc = interface score (proxy for binding energy). We use this
        to predict which models are docked better.
        
    To only look at high-quality models, select rows with CAPRI_rank=3.0.
    Then sort these rows by interface score and filter the display to
    show only the relevant metrics and the description. For the three 
    rows with the best interface scores and the three with the worst 
    ones, print the mean and median of the fraction of native contacts.  
    """


main()

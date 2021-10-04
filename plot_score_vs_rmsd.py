import matplotlib.pyplot as plt
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
            sys.exit("Error in input file at decoy {}.".format(scores[-1]))

    return headers, score_data


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--score_file', help='Path to score file',
                        required=True)
    args = parser.parse_args()
    score_file = args.score_file

    # separating the score file into headers and values
    headers, score_data = parse_score_file(score_file)

    # converting the parsed data into a pandas data frame
    df = pd.DataFrame(score_data, columns=headers, dtype=float)

    """Insert code to plot score versus RMSD
    
    Attached is a score file of symmetric docking simulations called
    3m1z_SymDock_score. Using the pandas data frames, make a scatter
    plot of interface scores (y-axis) versus interface RMSD (x-axis),
    i.e. df['I_sc'] vs df['Irms']. Reduce the marker point size to 10
    and change it to a color of your choice. Limit the left of the
    x-axis to 0 Angstroms and the top of the y-axis to 0 energy units.
    Draw a dashed vertical line at interface RMSD = 1 Ang to highlight
    sub-Angstrom points. Assign appropriate x- and y-axis labels and
    a plot title.
    
    Finally save the plot and attach it with your code submission.
    """
    # Extracting columns of the df as the x and y axis
    x = df.Irms
    y = df.I_sc
    print(x)
    print(y)

    # Creating a scatterplot with size 10 red dots
    plt.scatter(x, y, marker='.', s=10, color='red')

    # Adding in a dashed line at 1 Ang for reference
    plt.axvline(x=1, linestyle='dashed')

    # Limiting the x and y axis and labelling both axes
    plt.xlabel('Interface RMSD')
    plt.xlim(0)
    plt.ylabel('Interface Scores')
    plt.ylim(-125, 0)

    # Adding name to plot
    plt.title('Irms vs. I_sc')

    # Show and save the plot
    plt.show()
    plt.savefig('HW4_graph.png')

main()

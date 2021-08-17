import re

def listToString(s):
    str1 = " "
    return str1.join(s)

def main():

    score_file = open('docking_score.sc').readlines()

    """Insert code here to search for decoy scores

    Attached is a real score file (docking_score.sc) generated using a
    buggy job distribution system. In this exercise, we are only
    interested in the values of models (aka decoys) with serial numbers
    50-59. To print only those lines, we will use the help of regular
    expressions (aka regex) through the re module. The variable 
    score_file is a list of the lines in the ancillary score file. 
    
    Search for lines which start with 'SCORE:' and end with
    '3v4f_b_INPUT_0050\n' through '3v4f_b_INPUT_0059\n' and print them.
    Do you notice anything odd in the number of such lines?
    
    Search for lines which just end in '3v4f_b_INPUT_0050\n' through
    '3v4f_b_INPUT_0059\n' and print them. Is it odder?
    
    Now print the same lines using the re module and replacing 
    '3v4f_b_INPUT_' with 'regex_' in every line.

    You could do this entire assignment through basic string
    manipulations, but this way is more versatile going forward.
    """

    for x in range(50, 60):
        num = x
        for l in score_file:
            line = l.split()
            if line[0] == "SCORE:" and line[26] == "3v4f_b_INPUT_00" + str(num):
                rn = listToString(line)
                regex = re.compile(r'3v4f_b_INPUT_')
                print(regex.sub("regex_", rn))




main()

import re
import hashlib

def listToString(s):
    str1 = " "
    return str1.join(s)

def main():

    """Insert code here to fix a score file

    Attached is a real score file (docking_score.sc) generated using a
    buggy job distribution system. Your job is to write a fixed score
    file called fixed_docking_score.sc which takes care of the following
    problems:

    1)  docking_score.sc has multiple occurrences of the same decoy.
        For example, the decoy name 3v4f_b_INPUT_0049 appears multiple
        times. In the fixed file, write only the LAST instance of each
        decoy and discard all duplicate lines,
        e.g. only retain line 66 for 3v4f_b_INPUT_0049.

    2)  The lines are, at times, truncated.
        Delete all such lines in the fixed score file.

    3)  The decoy names may need to be changed to make them descriptive.
        In the fixed file, change the decoy names from 3v4f_b_INPUT_0049
        to file_handling_string_manipulation_test_0049 and so on.
        (Let's assume we also did this for the corresponding decoy pdb
        files.)

    No other detail in the lines should change. The two header lines
    should be printed as is. The order of the lines that are not
    discarded should be the same. At the end of your script, print out
    the number of lines in your decoy file and the number of lines you
    discarded.
    """
    score_file = open("docking_score.sc").readlines()[2:]

    # lines_seen = set()  # holds lines already seen
    # outfile = open("newDocking_score.txt", "w")
    # for line in open(infilename, "r"):
    #     if line not in lines_seen:  # not a duplicate
    #         outfile.write(line)
    #         lines_seen.add(line)
    # outfile.close()

    #1. Lets convert each line into a part of a list
    #2. Rearrange the list by their respective numbering
    #3. Take out the repeats and save the last instance

    line = listToString(score_file)
    #line = line.split()

    #print(line)
    #if line[0] == "SCORE:" and line[26] == "3v4f_b_INPUT_0091":
        #print(line)

    num = 0
    fullfile = []
    justnums = []


    for l in score_file:
        line = l.split()
        if line[0] == "SCORE:":
            rn = listToString(line)
            regex = re.compile(r'3v4f_b_INPUT_')
            #print(regex.sub("file_handling_string_manipulation_test_", rn))
            fullfile.append(rn)

    for i in range(len(fullfile)):
        current = fullfile[i]
        #print(current)
        num = current[-3:]
        justnums.append(num)

    #print(justnums)
    # print(fullfile)
    for i in range(len(justnums)-1, 0, -1):
        for j in range(i):
            if justnums[j] > justnums[j + 1]:
                temp = justnums[j]
                ltemp = fullfile[j]

                justnums[j] = justnums[j + 1] #so I listed everything in order, then how do I only grab in the last instance?
                fullfile[j] = fullfile[j + 1]

                justnums[j + 1] = temp
                fullfile[j + 1] = ltemp

    print(justnums)

    for i in range(len(justnums) - 1):
        print(justnums[i])
        if justnums[i] == justnums[i + 1]:
            justnums.remove(justnums[i])
            i -= 1


    # counter = 1
    # for i in justnums:
    #     if i == justnums[counter]:
    #         justnums.remove(i)
    #         #fullfile.remove(fullfile[counter - 1])
    #         counter -= 1
    #     counter += 1


    print(justnums)
    #print(fullfile)

    # for entry in fullfile:
    #     print(entry)

    # counter = 1
    # for i in justnums:
    #     if i == justnums[counter]:
    #         justnums.remove(i)
    #     counter += 1
    #
    # print(justnums)

    # for j in range(i):
    #     if
main()

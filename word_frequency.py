def parse_file(input_filename):

    # """This function reads from an input file and returns all the
    # words in a list. This is a helper function; treat as black box.
    # """
    word_list = []

    # to save each line as a string in a list
    input_file = open(input_filename).readlines()

    for line in input_file:
        line = line.strip()  # strip whitespace
        line = line.strip(",")
        line = line.strip("!")
        line = line.strip("'")
        line = line.strip(".")
        if not line or line.startswith("#"):
            continue  # skip empty lines and comments

        for word in line.split():  # splits the string by spaces
            word_list.append(word.lower())  # to eliminate case inconsistency

    return word_list


def main():

    word_list = parse_file("output.txt")  # can change Macbeth to any word file

    print(word_list)
    dictionary = []
    counter = 0
    roster = []
    Top10 = 0
    for i in word_list:
        if len(i) >= 4:
            if i not in dictionary:
                dictionary.append(i)

    for w in dictionary:
        current = w
        for l in word_list:
            if current == l:
                counter += 1

        roster.append(counter)
        roster.append(w)
        counter = 0

    # for c in roster:


    #print(dictionary)

    # """Insert code here to read word frequencies
    #
    # In this folder is a helper file where we have the entire Macbeth
    # copied from http://shakespeare.mit.edu/macbeth/full.html. Make sure
    # it stays in the same folder as this file.
    #
    # The file is read by a pre-defined helper function tha returns all
    # the words as a list. Use dictionaries to find out how frequently
    # every word occurs. Then sort the dictionary by the word frequency.
    # One way would be using:
    # sorted_word_count = sorted(word_count.items(), key=lambda kv: kv[1],
    #                            reverse=True)
    # (where word_count is the name of the dictionary and
    # sorted_word_count is list of tuples sorted by word frequency)
    #
    # You could also check out defaultdict for a better dictionary using:
    # from collections import defaultdict
    #
    # Print the 10 most commonly used 4+ letter words as follows:
    # <word 1> occurs <n1> times.
    # <word 2> occurs <n2> times.
    # and so on.
    #
    # You could also just sort the list and count the frequencies, but
    # where's the fun in that!
    # """

main()

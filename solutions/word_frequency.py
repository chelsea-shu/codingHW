def parse_file(input_filename):

    """This function reads from an input file and returns all the
    words in a list. This is a helper function; treat as black box.
    """
    word_list = []

    # to save each line as a string in a list
    input_file = open(input_filename).readlines()

    for line in input_file:
        for word in line.split():  # splits the string by spaces
            word_list.append(word.lower())  # to eliminate case inconsistency

    return word_list


def main():

    word_list = parse_file("Macbeth")  # can change Macbeth to any word file

    """Insert code here to read word frequencies

    In this folder is a helper file where we have the entire Macbeth
    copied from http://shakespeare.mit.edu/macbeth/full.html. Make sure
    it stays in the same folder as this file.

    The file is read by a pre-defined helper function tha returns all
    the words as a list. Use dictionaries to find out how frequently
    every word occurs. Then sort the dictionary by the word frequency.
    One way would be using:
    sorted_word_count = sorted(word_count.items(), key=lambda kv: kv[1],
                               reverse=True)
    (where word_count is the name of the dictionary and
    sorted_word_count is list of tuples sorted by word frequency)

    Print the 10 most commonly used 4+ letter words as follows:
    <word 1> occurs <n1> times.
    <word 2> occurs <n2> times.
    and so on.

    You could also just sort the list and count the frequencies, but
    where's the fun in that!
    """

    # counting which word occurs how many times
    word_count = {}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count.update({word: 1})

    sorted_word_count = sorted(word_count.items(), key=lambda kv: kv[1],
                               reverse=True)

    # printing the 10 most common 4+ letter words
    accepted_word_count = 0

    for counts in sorted_word_count:
        if len(counts[0]) >= 4:
            print(str(counts[0]) + " occurs " + str(counts[1]) + " times.")
            accepted_word_count += 1

        if accepted_word_count >= 10:
            break


main()

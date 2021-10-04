import argparse

# Creates a dictionary from the given file
def make_dict(fileName):
    dict = {}
    with open(fileName) as f: # Open and read file line by line
        while True:
            line = f.readline()
            if not line: # If there are no more lines, break
                break
            key = line.split()[0] # Convert key and values into the dictionary
            value = line.split()[1]
            dict[key] = value

    return dict

# Uses command line to change values in the dictionary
def main():
    dict = make_dict('ref2015_wts')
    parser = argparse.ArgumentParser(description='Changing the weight of things')
    parser.add_argument('-t', '--terms', nargs='*', help='What is the name of the term you are changing')
    parser.add_argument('-w', '--weights', nargs='*', type=float, help='What is the weight you want to enter')
    args = parser.parse_args()

    # Store arguments as variables/lists
    keys_to_change = args.terms
    values_to_change = args.weights

    # Locate values based on the keys and change the value
    count = 0
    for ii in keys_to_change:
        dict[str(ii)] = values_to_change[count]
        print(str(ii) + 'was changed to ' + str(values_to_change[count]))
        count += 1

    print(dict)

    """Write a function to alter score weights

    Attached is a file called ref2015_wts which has the weights of the
    various score terms. Using argparse and file parsing methods, read
    the file and make a dictionary like:
    score_weights = {'fa_atr': 1, 'fa_rep': 0.55, ...}

    Now, write a function to change the default weights of selected
    score terms and display which terms were changes. Since you have no
    prior way of determining how many terms need to be changed, the
    function should accept the dictionary of weights and a variable
    number of keyword arguments (look up **kwargs).


    For example,
    A)
    If command line is:
    python alter_weights.py --terms fa_atr --weights 0.8

    the output should be:
    fa_atr was changed to 0.8
    {'fa_atr': 0.8, 'fa_rep': 0.55, ...}

    B)
    If command line is:
    python float_increment.py -t fa_atr fa_rep -w 0.8 0.9

    the output should be:
    fa_atr was changed to 0.8
    fa_rep was changed to 0.9
    {'fa_atr': 0.8, 'fa_rep': 0.55, ...}

    Please follow PEP8 conventions.
    """


main()

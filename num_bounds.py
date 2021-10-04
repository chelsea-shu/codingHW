import argparse

def within_bounds(value, low, high):

    """This function returns True if value is less than high and more
    than low. Replace this function with a lambda function.
    """

    return high > value > low


def main():
    parser = argparse.ArgumentParser(description='Entering a series of numbers and comparing values')
    parser.add_argument('-hi', '--high', type=float, help='What is the high parameter?')
    parser.add_argument('-l', '--low', type=float, help='What is the low parameter?')
    parser.add_argument('-v', '--value', nargs='*', type=float, help='What is your value?')
    args = parser.parse_args()

    # Stores the different arguments and creates a list of entered values
    high = args.high
    low = args.low
    value_list = args.value

    # Defining the lambda function that will return a True or False when comparing values
    x = lambda a, b, c : a > b > c # Lambda values can only store 1 argument! It's just nice and compact

    # Iterizes the list of entered values and returns whether or not the current value is within bounds
    for current in value_list:
        print(x(high, current, low))

    """Insert code here to input a series of numbers and of bounds and
    print out a series of True/False if the numbers are within the
    bounds.

    Use argument parsing to accept the three arguments. To input a
    number series you may use the nargs parameter. Then substitute the
    function written above with a lambda function, which does the
    exact same thing. Finally print out True or False in the same order.

    Please follow PEP8 conventions.
    """


main()

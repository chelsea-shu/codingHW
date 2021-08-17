from math import sqrt


def main():

    number1 = input("Enter first integer: ")
    number2 = input("Enter second integer: ")

    """Insert code here print common factors of two numbers

    Similar to the previous homework, loop up to the square root of the
    two numbers, identify all the factors and store them in two lists,
    one for each number. Then compare the contents of the list to
    identify unique common factors (including 1) and print them in 
    ascending order.
    
    One way to compare is to loop through the contents of the sets and 
    find common factors. (A more efficient way is to convert the lists 
    into sets and find the intersection, if you want to try that.)

    Check that the inputs are positive integers.
    
    If you are comfortable using functions, feel free to define one to
    identify factors. If not, it's okay to duplicate the code for this
    homework. We'll re-do this exercise later for an arbitrarily large
    number of integers, and then we'll use functions.
    """

    if not (isinstance(number1, int) and isinstance(number2, int)):

        print("Inputs should be integers.")

    elif not (number1 > 0 and number2 > 0):

        print("Inputs should be positive.")

    else:

        number1_factors = []
        number2_factors = []
        common_factors = []

        # identifying factors of number1
        for i in range(1, int(sqrt(number1)) + 1):
            if number1 % i == 0:
                number1_factors.append(i)
                if i != number1/i:
                    number1_factors.append(number1/i)

        # identifying factors of number1
        for i in range(1, int(sqrt(number2)) + 1):
            if number2 % i == 0:
                number2_factors.append(i)
                if i != number2/i:
                    number2_factors.append(number2/i)

        # identifying common factors
        for i in number1_factors:
            if i in number2_factors:
                common_factors.append(i)

        if len(common_factors) == 0:
            print(str(number1) + " and " + str(number2) +
                  " have no common factors.")
        else:
            print("The common factors of " + str(number1) + " and " +
                  str(number2) + " are : " +
                  ", ".join(str(factor) for factor in sorted(common_factors)))


main()

from math import sqrt, ceil


def main():

    number1 = int(input("Enter first integer: "))
    number2 = int(input("Enter second integer: "))

    # Account for negatives

    num1list = []
    num2list = []
    common = []

    for i in range(ceil(sqrt(number1))):
        if number1 % (i+1) == 0:
            num1list.append(i+1)
            num1list.append(int(number1 / (i+1)))

    for i in range(ceil(sqrt(number2))):
        if number2 % (i+1) == 0:
            num2list.append(i+1)
            num2list.append(int(number2 / (i+1)))

    num1list = sorted(set(num1list))
    num2list = sorted(set(num2list))
    for r in num1list:
        for r2 in num2list:
            if r == r2:
                common.append(r)

    print(common)

    # What if they have no common factors?

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


main()

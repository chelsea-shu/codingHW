from math import sqrt


def main():

    number = input("Enter an integer: ")

    """Insert code here check if a number is prime
    
    One (inefficient) way to do this is to loop from 2 to the square
    root (sqrt(number)) of this number and test the divisibility by 
    these numbers by using the modulo (%) operator.

    If the number the user enters is composite, the loop should break
    at the very first instance of a non-trivial factor.
    
    For example, if the user enters 36, the output should be:
    36 = 2 * 18
    
    if the user enters 29, the output should be:
    29 is a prime number.
    
    To check for integer input, you can use isinstance(number, int).
    Also, check that the integer is positive and provide a suitable error
    message.
    """

    if not isinstance(number, int):

        print("Input should be an integer.")

    elif number > 0:

        is_prime = True

        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                print(str(number) + " = " + str(i) + " * " + str(number / i))
                is_prime = False
                break  # factor detected; stop further calculations

        if is_prime:
            print(str(number) + " is a prime number.")

    else:

        print("Input should be positive.")


main()

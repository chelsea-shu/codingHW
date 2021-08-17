from math import sqrt


def main():

    number = int(input("Enter an integer: "))

    factors = []
    if number < 0:
        print("The number given is negative")

    else:
        for i in range(number):
            if number % (i + 1) == 0:
                factors.append(i + 1)
        if factors == [1, number]:
            print("This is a prime number")
        print(factors)


main()


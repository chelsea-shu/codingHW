from math import sqrt
import math

# Getting input from the user
def get_input():
    nums = []

    length = int(input("How many numbers are you entering? "))

    for ii in range(length):
        nums.append(int(input("Enter number: ")))

    return nums


# Identifying all divisible factors? What do you mean unique common factors?
def get_factors(nums):
    overall_list = []

    for num in nums:
        num_factors = []
        for ii in range(1, math.ceil(sqrt(num))):
            if num % ii == 0:
                num_factors.append(ii)
                num_factors.append(int(num/ii))

        overall_list.append(num_factors)

    return overall_list


# Find the intersection of all factors created
def find_intersection(all_factors):
    for ii in range(len(all_factors) - 1):
        set1 = set(all_factors[ii])
        set2 = set(all_factors[ii+1])
        print(set1.intersection(set2))

def main():
    numbers = get_input()
    factors = get_factors(numbers)
    print(factors)
    find_intersection(factors)




    """Insert code here print common factors

    Ask to user to input a set of integers. Similar to the problems in
    HW set 1, loop up to the square root of all numbers, identify all
    the factors and store them in individual lists. Then compare the
    contents of the list to identify unique common factors (including
    1) and print them in ascending order.

    Write a function to identify the factors and store them in a list.
    You can then use set intersections.

    Follow PEP 8 conventions
    """


main()

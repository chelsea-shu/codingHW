def main():

    height = int(input("Enter the height of the triangle: "))

    if height % 2 != 0:
        top = int(height / 2)
        total_stars = height
    else:
        top = int((height - 1)/2)
        total_stars = height - 1

    temp = top
    stars = 1

    for x in range(top):
        for s in range(temp):
            print(" ", end="")
        for st in range(stars):
            print("*", end="")
        print()
        temp -= 1
        stars += 2

    if height % 2 != 0:
        for mid in range(total_stars):
            print("*", end="")
        print()
    else:
        for r in range(2):
            for mid in range(total_stars):
                print("*", end="")
            print()

    stars = stars - 2
    temp = 1
    for x in range(top):
        for s in range(temp):
            print(" ", end="")
        for st in range(stars):
            print("*", end="")
        print()
        temp += 1
        stars -= 2



    """Insert code here to print a diamond

    Using an integer input, draw a diamond of that height.

    For example, if the user inputs 5, the output should be:
      *
     ***
    *****
     ***
      *

    if the user inputs 6, the output should be:
      *
     ***
    *****
    *****
     ***
      *

    Extra: Feel free to add code to verify the input etc.
    """


main()

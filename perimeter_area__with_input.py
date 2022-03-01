#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created March 2022
# This program calculates the perimeter and area
# of a rectangle with user input.


def main():
    # this function calculates the perimeter and area
    # input
    length = int(input("Enter the length of the rectangle (cm): "))
    width = int(input("Enter the Width of the rectangle (cm): "))
    # process
    perimeter = 2 * (length + width)
    area = length * width
    # output
    print("")
    print("Perimeter is {0} cm.".format(perimeter))
    print("Area of {0} cm².".format(area))
    print("\nDone.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: October 2021
# This is the percentage marker program in python
# this function uses return values


def calculate_percentage_mark(level):
    # calculate mark as percentage
    if level == "4+":
        percentage = 97
    elif level == "4":
        percentage = 90
    elif level == "4-":
        percentage = 83
    elif level == "3+":
        percentage = 78
    elif level == "3":
        percentage = 74
    elif level == "3-":
        percentage = 71
    elif level == "2+":
        percentage = 68
    elif level == "2":
        percentage = 64
    elif level == "2-":
        percentage = 61
    elif level == "1+":
        percentage = 58
    elif level == "1":
        percentage = 54
    elif level == "1-":
        percentage = 51
    elif level == "R":
        percentage = 24
    else:
        percentage = -1

    return percentage


def main():
    # this function gets the level

    # input
    level_from_user = input("Enter the level you want converted to a percentage: ")

    # call functions
    # output

    some_variable = calculate_percentage_mark(level_from_user)

    if some_variable == -1:
        print("{0} is an invalid input.".format(level_from_user))
    else:
        print(
            "Level {0} has a middle percentage of {1}%.".format(
                level_from_user, some_variable
            )
        )
    print("\nDone.")


if __name__ == "__main__":
    main()

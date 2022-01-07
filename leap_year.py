#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Dec. 16, 2021
# This program allows a user to determine
# if a certain year is a leap year

import time


def main():
    # Asks questions and gets user input
    print("This program determines if a chosen year is a leap year.")
    print(" ")
    time.sleep(1)
    user_year = (input("Enter your year: "))
    print(" ")
    time.sleep(1)

    try:
        # Make sure user input is an integer
        user_year_int = int(user_year)

        # Calculate if year is a leap year
        if user_year_int <= 0:
            print("Please enter a positive integer")
        else:
            if user_year_int % 4 == 0:
                if user_year_int % 100 == 0:
                    if user_year_int % 400 == 0:
                        print("{} is a leap year".format(user_year_int))
                    else:
                        print("{} is not a leap year".format(user_year_int))
                else:
                    print("{} is a leap year".format(user_year_int))
            else:
                print("Not a leap year")

    except Exception:
        # Prevent crash by displaying error messsage
        print("'{}' is not a number".format(user_year))


if __name__ == "__main__":
    main()

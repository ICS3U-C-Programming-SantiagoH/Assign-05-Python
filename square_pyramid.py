#!/usr/bin/env python3

# Created by: Santiago Hewett
# Created on: Dec 11, 2023
# This program takes user input for the base edge
# and height of a square-based pyramid, then calculates
# the surface area, and allows the user to do the process again.

import math


def calc_surface_area(base_edge, height):
    # Calculate the surface area of a square pyramid
    surface_area = base_edge**2 + base_edge * 2 * math.sqrt(
        base_edge**2 / 4 + height**2
    )
    return surface_area


def get_positive_float(prompt):
    # Get a positive float input from the user
    while True:
        user_input_str = input(prompt)
        try:
            user_input_float = float(user_input_str)
            if user_input_float > 0:
                return user_input_float
            else:
                print(f"{user_input_float} must be greater than 0.")
        except ValueError:
            print(f"{user_input_str} is not a valid positive number.")


def main():
    # Main function for the square pyramid surface area calculator
    while True:
        # Get valid input for base edge and height but also alow for decimals
        user_base_edge = get_positive_float(
            "Enter the base edge of the square pyramid: "
        )
        user_height = get_positive_float("Enter the height of the square pyramid: ")

        # Calculate and display the surface area
        surface_area = calc_surface_area(user_base_edge, user_height)
        print(f"\nThe surface area of the square pyramid is: {surface_area:.2f}")

        # Ask if the user wants to run it again
        user_decision = input(
            "\nDo you want to calculate for another square-based pyramid? (y/n): "
        )

        # Check if the user wants to stop
        if user_decision.lower() != "y":
            break


if __name__ == "__main__":
    main()

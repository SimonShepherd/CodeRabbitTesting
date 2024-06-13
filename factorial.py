#!/usr/bin/env python3

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the number n.

    Raises:
    ValueError: If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    """
    Main function to test the factorial function.
    """
    try:
        number = int(input("Enter a non-negative integer: "))
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
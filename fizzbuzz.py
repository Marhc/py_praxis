"""Solving the classic FizzBuzz challenge.

This example implements FizzBuzz as a function. 

Features included in this module:
    - Console Output;
    - Function Definition;
    - Type Definition ('Type Hints');
    - String Interpolation ('fstrings');
    - Docstrings ('Google Python Style Guide');
    - Single line and Multiline comments;
    - Conditional Statements;
    - For..in loop;
    - Ranges;
    - Modulus / remainder operator ('%');
    - Special, 'dunder' or 'magic' variables;
"""


def fizzbuzz(num: int) -> str:
    """For the given number, returns the correct answer in the Fizzbuzz game.

    Args:
        num: An integer number > 0

    Returns:
        A string corresponding to the game answer.  
    """

    if num % 3 == 0 and num % 5 == 0:
        return f"{ num } - FizzBuzz"
    elif num % 3 == 0:
        return f"{ num } - Fizz"
    elif num % 5 == 0:
        return f"{ num } - Buzz"
    else:
        return f"{ num }"


if __name__ == "__main__":
    # Skips execution when importing the module,
    # but allows it when calling the script.

    for item in range(1, 101):
        print(fizzbuzz(item))

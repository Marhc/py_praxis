"""
    Solving the classic FizzBuzz challenge.

    This example implements FizzBuzz as a function. 

    Features included in this module:
        - Console Output;
        - Function Definition;
        - Type Definition ('Type Hints');
        - String Interpolation ('fstrings');
        - Docstrings;
        - Single line and Multiline comments;
        - Conditional Statements;
        - For..in loop;
        - Ranges;
        - Modulus / remainder operator ('%');
        - Special, 'dunder' or 'magic' variables;
"""


def fizzbuzz(num: int) -> str:
    """Returns the appropriate answer for the given number."""
    if num % 15 == 0:
        return f"{ num } - FizzBuzz"
    elif num % 3 == 0:
        return f"{ num } - Fizz"
    elif num % 5 == 0:
        return f"{ num } - Buzz"
    else:
        return f"{ num }"


if __name__ == "__main__":
    # Bypass execution when module importing,
    # but allows execution when calling the script.

    for item in range(1, 101):
        print(fizzbuzz(item))

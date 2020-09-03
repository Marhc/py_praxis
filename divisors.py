"""This is a playground with a **'proper divisors'** function.

Features included in this module:
    - Console Input / Output;
    - Function Definition;
    - Type Definition (**'Type Hints'**);
    - Module Import;
    - String Interpolation (**'fstrings'**);
    - String Padding;
    - String Join;
    - Map function;
    - Type Conversion;
    - Lambda expressions;
    - **'For..in'** loop;
    - Modulus / remainder operator (**'%'**);
    - Ranges;
    - Conditional Statements;
    - Literal notation for Lists (**'List literal values'**);
    - List Comprehension;
    - Single line and Multiline comments;
    - Docstrings (**'Google Python Style Guide'**);
    - Comment-Docstrings;
    - Special, **'dunder'** or **'magic'** variables;
"""

from typing import List


def divisors(num: int) -> List[int]:  # (PEP 484 - Type Hints)
    """Gets the list of the proper divisors.
    
    Args:
        num: An integer number > 0

    Returns:
        A List of integers corresponding to the list of divisors.
    """

    factors = [1]
    for factor in range(2, num + 1):
        if num % factor == 0:
            factors.append(factor)

    return factors


# Anti-pattern according to PEP8 style guide: 'Always use a def statement...'.
divisors_from_lambda = lambda num: [factor for factor in range(1, num + 1) if num % factor == 0]
   

if __name__ == '__main__':
    # Bypass execution when module importing,
    # but allows execution when calling the script.

    input_number = int(input("Type a integer number > 0: "))
    print(f"{ 'Divisors from Function'.ljust(22) } = {{ { ', '.join(map(str, divisors(input_number))) } }}")
    print(f"{ 'Divisors from Lambda'.ljust(22) } = {{ { ', '.join(map(str, divisors_from_lambda(input_number))) } }}")

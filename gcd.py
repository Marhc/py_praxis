"""Playing around with 'gcd function' implementations.

Features included in this module:
    - Console Input / Output;
    - Function Definition;
    - Type Definition ('Type Hints');
    - Module Import;
    - Tuple literal values;
    - Dictionary literal values;
    - 'Spread'/'Unpack'/'Splat' Operator ('*');
    - Interpolation / Substitution of strings;
    - String Padding;
    - Type Conversion;
    - Destructuring Assignment;
    - Set Intersection Operator ('&');
    - Max built-in function;
    - Built-in Math Library;
    - While loop;
    - Modulus / remainder operator ('%');
    - Docstrings ('Google Python Style Guide');
"""

from math import gcd
from divisors import divisors


def gcd_by_factors(num1: int, num2: int) -> int:
    """Calcs the gcd using the list of dividers

    Args:
        num1: An integer number > 0
        num2: An integer number > 0

    Returns:
        The result of gcd.
    """

    first_divisors = divisors(num1)
    second_divisors = divisors(num2)

    return max(set(first_divisors) & set(second_divisors))


def gcd_by_euclid(num1: int, num2: int) -> int:
    """Calcs the gcd by Euclidian Algorithm

    Args:
        num1: An integer number > 0
        num2: An integer number > 0

    Returns:
        The result of gcd.  
    """

    while num2:
        num1, num2 = num2, num1 % num2
    return num1


first_number = int(input("Type the first number: "))
second_number = int(input("Type the second number: "))

factors_gcd = {
    'label': 'GCD by factors',
    'value': gcd_by_factors(first_number, second_number)
}

euclidian_gcd = ('GCD by Euclid', gcd_by_euclid(first_number, second_number))
math_gcd = ('GCD by Math Lib', gcd(first_number, second_number))

# Latest Style with f-strings
print(f"\n{factors_gcd['label']:15}: {factors_gcd['value']}")

# New Style with format function
print("{:15}: {}".format(*euclidian_gcd))

# Old / Classic Style with '%' operator
print('%-15s: %d' % math_gcd)

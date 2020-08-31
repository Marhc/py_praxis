"""
    Playing around with 'gcd function' implementations.

    Features included in this module:
        - Console Input / Output;
        - Function Definition;
        - Type Definition ('Type Hints');
        - Module Import;
        - String Interpolation ('fstrings');
        - String Padding;
        - Type Conversion;
        - Destructuring Assignment;
        - Set Intersection Operator ('&');
        - Max built-in function;
        - Built-in Math Library;
        - While loop;
        - Modulus / remainder operator ('%');
        - Docstrings;
"""

from math import gcd
from divisors import divisors


def gcd_by_factors(num1: int, num2: int) -> int:
    """Calcs the gcd getting the list of divisors"""
    first_divisors = divisors(num1)
    second_divisors = divisors(num2)

    return max(set(first_divisors) & set(second_divisors))


def gcd_by_euclid(num1: int, num2: int) -> int:
    """Calcs the gcd by Euclidian Algorithm"""
    while num2:
        num1, num2 = num2, num1 % num2

    return num1


first_number = int(input("Type the first number: "))
second_number = int(input("Type the second number: "))

print(f"\n{ 'GCD by factors:'.ljust(16) }  { gcd_by_factors(first_number, second_number) }")
print(f"{ 'GCD by Euclid:'.ljust(16) }  { gcd_by_euclid(first_number, second_number) }")
print(f"{ 'GCD by Math Lib:'.ljust(16) }  { gcd(first_number, second_number) }")

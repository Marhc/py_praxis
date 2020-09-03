"""A simple **"Hello Function"** for educational purposes.

This module explores basic features of the Python programming language.

Features included in this module:
    - Console Input / Output;
    - Function Definition;
    - Module Import;
    - Default Parameter Values;
    - String Interpolation (**'fstrings'**);
    - Single line and Multiline comments;
    - Docstrings (**'Google Python Style Guide'**);
    - 'Falsy' coalescing operator (**'or'**);
    - Conditional Statements;
    - Custom main entry point and exit point;
    - Private function naming convention;
    - Special, **'dunder'** or **'magic'** variables;
    - Command line arguments handling;
"""

import sys


def hello_user(name=""):
    """Returns a greeting message with the user name.

    This is an example of a parameterized function with a default value.
    If no name is provided the function returns **"Hello Everyone!"** by default.

    Args:
        name (str): The user name typed in the Console. 

    Returns:
        str: The greeting message.
    """

    return f"Hello { name or 'Everyone' }!"


def _custom_main(argv):  # Python has no a default main entry point.
    """Example of a custom main function with command line arguments handling."""

    user_name = input("Type your name: ")
    print(hello_user(user_name))


if __name__ == '__main__':
    # Skips execution when importing the module,
    # but allows it when calling the script.

    sys.exit(_custom_main(sys.argv))

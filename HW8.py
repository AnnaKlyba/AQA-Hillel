"""
Homework 8. Multiplication table.

Given 0 < number (integer) <= 11
You need to print multiplication table based on this number.
# Example: num=5
# Output:
#  1   2   3   4   5
#  2   4   6   8  10
#  3   6   9  12  15
#  4   8  12  16  20
#  5  10  15  20  25
"""


def multi_table(el):
    """Print multiplication table. Input parameters: el - integer."""
    for x in range(1, el + 1):
        for y in range(1, el + 1):
            print(x * y, end='\t')
        print()


multi_table(5)

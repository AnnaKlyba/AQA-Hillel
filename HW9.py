"""
Homework 9. Lambda function.

Given: list of integers/floats with lambda function
as one of the element inside list
Write function that will produce new list by applying
lambda to all integers and floats
Input: [lambda a: a + 2, 9, 3, 1, 0]
Output: [11, 5, 3, 2]

Input: [9, 2, 3, lambda a: a / 2.0, 1, 0]
Output: [4.5, 1, 1.5, 0.5, 0.0].
"""

l1 = [lambda a: a + 2, 9, 3, 1, 0]
l2 = [9, 2, 3, lambda a: a / 2.0, 1, 0]


def write_function(in_list):
    """Search for the lambda by its type and apply it to all elements."""
    lamb = 0
    for el in in_list:
        if isinstance(el, type(lambda: 0)):
            del in_list[lamb]
            lamb = el
            break
        else:
            lamb += 1
    out_list = [lamb(el) for el in in_list]
    return out_list


print(write_function(l1))
print(write_function(l2))

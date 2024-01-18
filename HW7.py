"""
Homework 7. If-elif-else.

Given values w,x,y,z
write if-elif-else statement that will search minimum value
and print smth aka "'y' is minimum value'
where 'y' is variable name (not value)
advice use python debugger and different values to check your algorithm
optionally you can check your algorithm somehow with assert statements
"""

w, x, y, z = -1, -1, -1, 0

template = "'{}' is minimum value"

if (w <= x) and (w <= y) and (w <= z):
    print(template.format('w'))
elif (x <= w) and (x <= y) and (x <= z):
    print(template.format('x'))
elif (y <= w) and (y <= x) and (y <= z):
    print(template.format('y'))
else:
    print(template.format('z'))

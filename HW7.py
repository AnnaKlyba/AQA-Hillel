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

if (w <= x) and (w <= y) and (w <= z):
    print("'w' is minimum value")
elif (x <= w) and (x <= y) and (x <= z):
    print("'х' is minimum value")
elif (y <= w) and (y <= x) and (y <= z):
    print("'y' is minimum value")
else:
    print("'z' is minimum value")

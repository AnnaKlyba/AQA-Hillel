"""
Homework 5.
Given list of tuples (people list -> name, surname, age, profession,
City location)
1 - Add your new record with similar random data to the beginning
of the given list
2 - In modified list swap elements with indexes 1 and 5  (1<->5)
and print result
3 - check condition that all people in modified list with records
indexes 6, 10, 13 have age >=30 and print result.
"""

AGE = 30

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix'),
]

p_rec = people_records.copy()
p_rec.insert(0, ('Antony', 'Poveck', 25, 'QA', 'Taxes'))
p_rec[1], p_rec[5] = p_rec[5], p_rec[1]
print(p_rec)

"""Print check for every case."""

print(p_rec[6][2] >= AGE)
print(p_rec[10][2] >= AGE)
print(p_rec[13][2] >= AGE)

"""Print check for logical AND."""

print(p_rec[6][2] >= AGE and p_rec[10][2] >= AGE and p_rec[13][2] >= AGE)

"""Print check for logical ALL."""

log_all = all((p_rec[6][2] >= AGE, p_rec[10][2] >= AGE, p_rec[13][2] >= AGE))
print(log_all)

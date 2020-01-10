from com.abc.lib.student_ops import get_details, get_grade

# procedural programming (C)

name = input('Enter name: ')
roll = int(input('Enter roll: '))
gender = input('Enter gender: ')
marks = float(input('Enter marks: '))

print(get_details(name, roll, gender, marks))
print(get_grade(marks))


# Object oriented programming (OOP)
# Real world equate Software
# 1. Real world actors - Memory that data occupies in the RAM: Object.
# Every data (object) in the RAM has data type: str, int, float, bool.
# "class" gives a data type to an object and it is used to create 1 to n objects
# str, int, float, bool,... are all built in classes in python
'''
2. Real world actor characteristics - Attributes of the object
3. Real world actor actions - Function calls on the object
'''
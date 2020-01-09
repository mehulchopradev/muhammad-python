from com.abc.lib.student_ops import get_details, get_grade

# procedural programming (C)

name = input('Enter name: ')
roll = int(input('Enter roll: '))
gender = input('Enter gender: ')
marks = float(input('Enter marks: '))

print(get_details(name, roll, gender, marks))
print(get_grade(marks))


# Object oriented programming (OOP)
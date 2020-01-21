from com.abc.college.student import Student
from com.abc.college.professor import Professor

s1 = Student(name='mehul', gender='m', roll=10, marks=90)
# Internally
# 1. 5006
# 2. Student.__init__(5006, name='mehul', gender='m', roll=10, marks=90)

p1 = Professor(name='jane', gender='f', subjects=['Physics', 'Chemistry'])
# Internally
# 1. 5004
# 2. Professor.__init__(5004, name='jane', gender='f', subjects=['Physics', 'Chemistry'])

i = 45

print(i)
# Internally
# print(i.__str__())
# print(int.__str__(i))

print(s1)
# Internally
# print(s1.__str__())
# print(Student.__str__(s1))

print(p1)
# Internally
# print(p1.__str__())
# print(Professor.__str__(p1))

# print(s1.get_details())
# Internally
# print(Student.get_details(s1))

# print(p1.get_details())
# Internally
# print(Professor.get_details(p1))

# print(p1.get_subjects()) # Physics|Chemistry
from com.abc.college.student import Student
# Person Y

# objects (instances)
# s1 = Student()
# Internally
'''
1. Memory (4005) will be reserved in the RAM for this new object
2. Student.__init__(4005)
'''

s1 = Student('mehul', 'm', 10, 90) # RAM (4005)
# Internally
'''
1. Memory (4005) will be reserved in the RAM for this new object
2. Student.__init__(4005, 'mehul', 'm', 10, 90)
'''


s2 = Student('jane', 'f', 12, 34) # RAM (4003)

# print(s1)
# print(s2)

# create attributes in an object
''' s1.name = 'mehul'
s1.gender = 'm'
s1.roll = 10
s1.marks = 90

s2.name = 'jane'
s2.gender = 'f'
s2.roll = 12
s2.marks = 34 '''

# get attributes from an object (access them)
''' print(s1.name)
print(s1.roll)
print(s2.name)
print(s2.roll) '''

# print(s1.mobile) # this will give attribute not found error

print(s1.get_details())
# Internally
# print(Student.get_details(s1))

print(s2.get_details())
# Internally
# print(Student.get_details(s2))

print(s1.get_grade())
# Internally
# print(Student.get_grade(s1))

print(s2.get_grade())
# Internally
# print(Student.get_grade(s2))

'''
s3 = Student()
s3.student_name = 'muhammad'
s3.gen = 'm'
s3.r = 13
s3.marks = 23
Is also a violation of object oriented principles
Objects of the same data type (class), must have the same set of attributes
'''

# print(s3.get_details()) # will not work
# Internally
# print(Student.get_details(s3))

s3 = Student('muhammad', 'm', 13, 23)
print(s3.get_details())
print(s3.get_grade())



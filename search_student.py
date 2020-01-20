from com.abc.college.student_old import Student

# ordered data structure
''' slist = [
    Student(name='mehul', gender='m', roll=10, marks=90),
    Student(name='muhammad', gender='m', roll=5, marks=56),
    Student(name='jane', gender='f', roll=12, marks=88),
    Student(name='jill', gender='f', roll=4, marks=99)
] '''

sdict = {
    10: Student(name='mehul', gender='m', roll=10, marks=90),
    5: Student(name='muhammad', gender='m', roll=5, marks=56),
    12: Student(name='jane', gender='f', roll=12, marks=88),
    4: Student(name='jill', gender='f', roll=4, marks=99)
}

roll = int(input('Enter roll to search: '))

''' for student in slist:
    if student.roll == roll:
        print(student.get_details())
        break
else:
    # will execute if the corresponding for block is completely exhausted
    # no break has been encountered in the corresponding for block
    print('Student not found') '''

if roll in sdict:
    student = sdict[roll]
    print(student.get_details())
else:
    print('Student not found')

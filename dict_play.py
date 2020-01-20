from com.abc.college.student_old import Student

sdict = {
    10: Student(name='mehul', gender='m', roll=10, marks=90),
    5: Student(name='muhammad', gender='m', roll=5, marks=56),
    12: Student(name='jane', gender='f', roll=12, marks=88),
    4: Student(name='jill', gender='f', roll=4, marks=99)
}

# get a new dict of items (rollno: name) from sdict
''' result = {}
items = sdict.items()
for item in items:
    result[item[0]] = item[1].name

print(result) '''

results = {roll: student.name for roll, student in sdict.items()}
print(results)

# get a new dict of items (rollno: (name, gender)) from sdict for only those students whose marks scored is > 88
ans = {roll: (student.name, student.gender) for roll, student in sdict.items() if student.marks > 88}
print(ans)

# get a new dict of items (rollno: [name, marks]) from sdict for only those students who have the gender 'm'
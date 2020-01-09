def get_details(name, roll, gender, marks):
    return 'Name: ' + name + '\nRoll: ' + str(roll) + '\nGender: ' + gender \
        + '\nMarks: ' + str(marks)

def get_grade(marks):
    if marks > 100 or marks < 0:
        grade = 'I'
    elif marks >= 70:
        grade = 'A'
    elif marks >= 60:
        grade = 'B'
    elif marks >= 40:
        grade = 'C'
    else:
        grade = 'F'
    return grade
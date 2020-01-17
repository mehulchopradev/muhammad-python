'''
As convention all user defined classes must start with capital letter
'''
# Person X
class Student:

    def __init__(self, name, gender, roll, marks):
        # constructor
        # self - the current object
        # create attributes in the object
        self.name = name
        self.gender = gender
        self.roll = roll
        self.marks = marks

        # by default
        # return self

    def get_details(self):
        # self - current object for which this function is being called
        ''' return 'Name: ' + self.name + '\nRoll: ' + str(self.roll) + '\nGender: ' + self.gender \
        + '\nMarks: ' + str(self.marks) '''
        # return 'Name: {0}\nRoll: {1}\nGender: {2}\nMarks: {3}'.format(self.name, self.roll, self.gender, self.marks)
        return 'Name: {name}\nRoll: {roll}\nGender: {gender}\nMarks: {marks}'\
            .format(roll=self.roll, name=self.name, gender=self.gender, marks=self.marks)

    def get_grade(self):
        marks = self.marks
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

    def get_name_roll(self):
        return (self.name, self.roll)
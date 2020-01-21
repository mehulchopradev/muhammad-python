# Student IS-A CollegeUser
# Student (child class) -> CollegeUser (parent class)
# Inheritance
# sub class -> super class
# child class -> parent class
from .college_user import CollegeUser

# Student -> CollegeUser -> object : Multilevel inheritance
class Student(CollegeUser):
    def __init__(self, name, gender, roll, marks):
        super().__init__(name, gender)
        # Internally
        # CollegeUser.__init__(self, name, gender)

        self.roll = roll
        self.marks = marks

    # overrides the inherited method in its own class
    def get_details(self):
        # self - Student object
        part1 = super().get_details()
        # Internally
        # CollegeUser.get_details(self)

        part2 = '\nRoll: {0}'.format(self.roll)
        return part1 + part2

    def __str__(self):
        # self - Student object
        part1 = super().get_details()
        part2 = '\nRoll: {0}\nMarks: {1}'.format(self.roll, self.marks)
        return part1 + part2

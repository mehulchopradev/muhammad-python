# Student IS-A CollegeUser
# Student (child class) -> CollegeUser (parent class)
# Inheritance
# sub class -> super class
# child class -> parent class
from .college_user import CollegeUser
class Student(CollegeUser):
    def __init__(self, name, gender, roll, marks):
        super().__init__(name, gender)
        # Internally
        # CollegeUser.__init__(self, name, gender)

        self.roll = roll
        self.marks = marks
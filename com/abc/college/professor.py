# Professor IS-A CollegeUser
# Professor (child class) -> CollegeUser (parent class)
from .college_user import CollegeUser
class Professor(CollegeUser):
    def __init__(self, name, gender, subjects):
        super().__init__(name, gender)
        # Internally
        # CollegeUser.__init__(self, name, gender)

        self.subjects = subjects

    # along with inherited methods can have its own set of methods too
    def get_subjects(self):
        return '|'.join(self.subjects)
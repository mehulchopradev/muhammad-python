# generalize code in this parent class

# super class
# parent class
# CollegeUser -> object : Single Inheritance
class CollegeUser(object): # every class in python implicitly inherits from the object class
    def __init__(self, name, gender):
        # self - (5006 Student object)
        # self - (5004 Professor object)
        # self - any child class object of CollegeUser

        # common set of attributes
        self.name = name
        self.gender = gender

    # method is inherited in its child classes
    def get_details(self):
        # self - (5006 Student object)
        # self - (5004 Professor object)
        # self - any child class object of CollegeUser
        return 'Name: {0}\nGender: {1}'.format(self.name, self.gender)

    def __str__(self):
        return self.get_details()
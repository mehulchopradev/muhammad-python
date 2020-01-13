'''
For every class in python (built in class or user defined class), a single object
per class is created in the RAM.
This object represents the class definition.
This is called as the class object
'''
class Book:
    # class object attribute
    count = 0
    def __init__(self, title, price, pages, no_of_copies):
        # Book object attributes
        self.title = title
        self.price = price
        self.pages = pages
        self.no_of_copies = no_of_copies

        # Class object attributes are accessed using the class name directly
        Book.count += 1

    # object functions
    def get_details(self):
        return 'Name: ' + self.title + '\nPrice: ' + str(self.price) \
        + '\nPages: ' + str(self.pages) + '\nNo Of Copies : ' + str(self.no_of_copies)

    def is_expensive(self):
        return True if self.price > 500 else False

    # class object functions
    # class object functions do not have self
    def get_count():
        return Book.count

    ''' def clone(source):
        return Book(title=source.title, price=source.price, pages=source.pages, no_of_copies=source.no_of_copies) '''
    
    def clone(self):
        return Book(title=self.title, price=self.price, pages=self.pages, no_of_copies=self.no_of_copies)

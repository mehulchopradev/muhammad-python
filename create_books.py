from com.abc.college.book import Book
# print(Book.count) # 0

# class object functions are directly called on the class
print(Book.get_count()) # class object functions
# Person Y

b1 = Book(title='Book 1', price=900, pages=879, no_of_copies=4)
b1.price=890 # mutable objects
print(Book.count) # 1

b2 = Book(title='Book 2', price=450, pages=600, no_of_copies=2)

print(b1.get_details()) # object functions
# Internally
# print(Book.get_details(b1))

print(b2.get_details())
# print(Book.get_details(b2))

print('Expensive') if b1.is_expensive() else print('Not expensive') # a book whose price is greater than 500
# print('Expensive') if Book.is_expensive(b1) else print('Not expensive')

print('Expensive') if b2.is_expensive() else print('Not expensive')

print(Book.count) # 2

b3 = Book(title='Book 3', price=340, pages=560, no_of_copies=2)
print(Book.count) # 3
print(b3.get_details())

# b3clone = Book.clone(b3)
b3clone = b3.clone()
# Book.clone(b3)
print(b3clone.get_details())
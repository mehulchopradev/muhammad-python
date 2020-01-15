# from com.abc.college.book import Book

# create a list of 4 Book objects

''' blist = [
    Book(title='Book 1', price=900, pages=450, no_of_copies=3),
    Book(title='Book 2', price=800, pages=340, no_of_copies=1),
    Book(title='Book 3', price=230, pages=900, no_of_copies=0),
    Book(title='Book 4', price=900, pages=1000, no_of_copies=2)
]

# get a new list of all the Books that have price greater than or equal 800 and then print the details of those books
price_more_thaneq_800_list = [book for book in blist if book.price >= 800]
for book in price_more_thaneq_800_list:
    print(book.get_details()) '''

blist = [
    ('Book 1', 900, 450, 3),
    ('Book 2', 800, 340, 1),
    ('Book 3', 230, 900, 0),
    ('Book 4', 900, 1000, 2),
]

# get a new list of all the Books that have price greater than or equal to 800 and then print the details
price_more_thaneq_800_list = [bt for bt in blist if bt[1] >= 800]
for book in price_more_thaneq_800_list:
    print('Name: ' + book[0] + '\nPrice: ' + str(book[1]) \
        + '\nPages: ' + str(book[2]) + '\nNo Of Copies : ' + str(book[3]))

# print(price_more_thaneq_800_list)
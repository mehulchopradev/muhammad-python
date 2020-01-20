pointers = [4, 5, 10, 6, 8, 9, 1, 3, 7, 10]

# get a new list of only the odd elements from the pointers list (filtering)
# without for comprehensions / for loop
# functional programming
# iterable = filter(function, iterable)

''' def odds(element):
    return element % 2
odd_elements = list(filter(odds, pointers)) '''
odd_elements = list(filter(lambda element: element % 2, pointers))
print(odd_elements)

# get a new list of only the even elements greater than 5 from the pointers list (filtering)
''' def evens_more_than_5(element):
    return not element % 2 and element > 5
evenss = list(filter(evens_more_than_5, pointers)) '''
evenss = list(filter(lambda element: not element % 2 and element > 5, pointers))
print(evenss)

# get a new list of pointer marks deducted by 1 from the pointers list (mapping)
# iterable = map(function, iterable)
''' def deducted_mark(element):
    return element - 1
deducted_marks = list(map(deducted_mark, pointers)) '''
deducted_marks = list(map(lambda element: element - 1, pointers))
print(deducted_marks)

# Lambda functions
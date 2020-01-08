# Module
# name -> evenodd

n = int(input('Enter n: '))

# remainder = n % 2

# if remainder is non zero then print Odd
# else print even
# 2 branches
# if - else
'''
if <<condition that gives either True or False>>:
    I1
    I2
    I3
else:
    I4
    I5
'''

''' if remainder:
   print('Odd')
else:
    print('Even') '''

''' if n % 2:
    print('Odd')
else:
    print('Even') '''

# if comprehensions syntax
# Pre requisite - both the branches (2) must have only one statement to execute in their blocks
print('Odd') if n % 2 else print('Even')
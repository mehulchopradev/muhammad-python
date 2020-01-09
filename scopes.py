# scope - areas in the code where you will be able to use the variable

a = 6 # scope is going to be entire module
c = 11 # scope is going to be entire module
d = 23 # scope is going to be entire module

def abc():
    b = 9 # scope is going to be abc()
    print(b) # 9
    print(a) # 6

    c = 15 # scope is going to be abc()
    print(c) # 15

    # d = d + 45 # this is an error
    # print(d)

# print(b) # this will not work as scope of b is only abc()
print(a) # 6
abc()
print(c) # 11
print(d)

'''
scope of a variable in python is either
1. The entire module
2. The function
'''
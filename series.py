# Module
# name -> series
'''
This module will have all the functions that help in generating a mathematical series
'''

# print(__name__) # pre built variable that every python module gets
# when run directly, the value is __main__
# when imported in sme other module, the value is series

def get_fibo_series(n):
    # n - 8
    # 0 1 1 2 3 5 8 13
    result = ''
    a, b = 0, 1
    result += str(a) + ' ' + str(b) + ' '
    for _ in range(1, n - 2 + 1): # _ means any variable. Prevents warning from coming when the loop
        # variable is not used in the loop
        c = a + b
        result += str(c) + ' '
        a, b = b, c

    return result

def get_odd_series(n):
    # n - 9
    # 1 3 5 7 9
    result = ''
    for v in range(1, n + 1, 2):
        result += str(v) + ' '
    return result

# below block of code should run only when the series module is run directly
# below block of code must not run when the series module is imported in some other module
if __name__ == '__main__':
    i = 10
    print(get_fibo_series(i))
    print(get_odd_series(i))
from traceback import print_exc

print('Program starts..')

n = input('Enter n: ')

# handled the error
# exception handling
try:
    i = int(n) # always look out for having only the statement that can raise an error, in the try block
except ValueError:
    print('Please enter integer value only')
    print_exc()
else:
    # will execute when there is no error in the corresponding try block
    print('Odd') if i % 2 else print('Even')

print('Program ends..')
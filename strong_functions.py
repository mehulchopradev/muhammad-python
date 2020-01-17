# can take 0 to n arguments
# variable number of arguments
def myadd(*args):
    # print(args) # tuple
    # print(type(args))
    sum = 0
    for element in args:
        sum += element
    return sum

# positional arguments packing
print(myadd()) # 0
print(myadd(5)) # 5
print(myadd(6, 5, 4, 3, 6)) # 24
print(myadd(6, 7, 2, 4, 6, 7, 8, 3, 4)) # 47


def area_rectangle(length, breadth):
    return length * breadth

# a list (tuple) where the elements in the list are in the same order as the positional arguments needed in the
# area_rectangle function
stats = [6, 3]
print(area_rectangle(stats[0], stats[-1]))

# positional arguments unpacking
print(area_rectangle(*stats))

def perimeter_rectangle(**stats):
    # print(stats) # dictionary
    # key in the dict - keyword argument name
    # value in the dict - keyword argument value
    '''
        This function expects keyword arguments 'length' and 'breadth'
    '''
    return 2 * (stats['length'] + stats['breadth'])

# print(perimeter_rectangle(4.3, 4.1))  # postional arguments. This will not work

# keyword arguments packing
print(perimeter_rectangle(length=4.3, breadth=4.1)) # keyword arguments
print(perimeter_rectangle(breadth=4.1, length=4.3))
# print(perimeter_rectangle(l=5, b=4)) # this will not work

smap = {'length': 5, 'breadth': 4}
# keys in the dictionary match the name of the  arguments in the function

print(area_rectangle(smap['length'], smap['breadth']))
print(area_rectangle(**smap))
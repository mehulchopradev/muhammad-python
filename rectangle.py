# user defined functions
def area_rectangle(length, breadth):
    a = length * breadth
    return a

def perimeter_rectangle(length, breadth):
    p = 2 * (length + breadth)
    return p

l = float(input('Enter length: '))
b = float(input('Enter breadth: '))

area = area_rectangle(l, b)
perimeter = perimeter_rectangle(l, b)

# built in functions
'''
built in functions are already defined, 
you just need to call them
'''
print(area)
print(perimeter)
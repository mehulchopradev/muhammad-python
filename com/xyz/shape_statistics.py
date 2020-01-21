from .shape import Shape
def compute_stats(s):
    # in such a way that whatever object is passed to this method, it has methods area() and perimeter()
    if isinstance(s, Shape):
        print('Area is {0}'.format(s.area()))
        print('Perimeter is {0}'.format(s.perimeter()))
    else:
        print('Cannot compute. Please inherit from Shape')
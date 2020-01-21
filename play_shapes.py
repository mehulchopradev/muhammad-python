# Manager

from com.abc.geometry.square import Square
from com.abc.geometry.rectangle import Rectangle
from com.abc.geometry.circle import Circle
from com.xyz.shape_statistics import compute_stats

s1 = Square(side=5)
''' print(s1.area())
print(s1.perimeter()) '''
compute_stats(s1)

s2 = Square(side=7)
compute_stats(s2)

r1 = Rectangle(length=5, breadth=2)
compute_stats(r1)

c = Circle(5)
compute_stats(c)

# abstract class and abstract methods
# 1. Make the class as abstract class
# 2. For whichever methods we need to enforce a compulsory override in the sub classes, make the method also abstract

from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
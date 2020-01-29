# multiple inheritance
# one child class having more than 1 parent class

# vendor x
class Abc:
    def fun(self):
        print('Fun of Abc')

    def hello(self):
        print('Different implementation of hello from abc')

# vendor y
class Xyz:
    def show(self):
        print('Show of xyz')

    def hello(self):
        print('Hello of xyz')

# me (my company)
class Mno(Xyz, Abc):
    pass

R u able to hear me ???
I cannot hear U

m = Mno()
m.fun()
m.show()
m.hello()
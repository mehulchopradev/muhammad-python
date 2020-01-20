# abc (entire module) -> function object
def abc():
    # i (abc) -> int (6)
    i = 6

    # j (abc) -> int (10)
    j = 10

    # k (abc) -> int (20)
    k = 20

    # xyz (abc) -> function object
    # in python a function can be defined inside another function
    def xyz():
        print('Xyz')

        # inner scope can access the outer scope variables
        # inner function can access the outer function variables
        print(j) # 10

        # k (xyz) -> int (50)
        k = 50
        print(k) # 50
    
    print(i) # 6
    xyz()
    print(k) # 20

abc()

# mno (module) -> function object (4001)
def mno():
    # t (mno) -> int (9)
    t = 9

    # rty (mno) -> function object (4003)
    def rty(x):
        print(x ** t)

    print(t) # 9

    # in python a function can return another function
    return rty

er = mno()
# our assumption
# above when the function returns, the variable t will be destroyed


# er (module) -> function object (4003)
er(5) # 25
# still contrary to the assumption, the line er(5) works! and it gets the value of t
# our assumption is wrong in case of inner functions
# closures
# an inner function remembers all the variables from the enclosing scope even after the enclosing scope has returned

# pqr (module) -> function object (4001)
def pqr(fn):
    # fn (pqr) -> 4005
    i = 9
    j = fn(i)
    return j ** 2

# gtr (module) -> function object (4005)
def gtr(a):
    return a - 1

# a function as an argument to another function
# callback function
b = pqr(gtr)
print(b)
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
        print(x ** 2)

    print(t) # 9

    # in python a function can return another function
    return rty

er = mno()
# er (module) -> function object (4003)
er(5) # 25
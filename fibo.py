# Module
# name -> fibo
n = int(input('Enter n: '))

'''
    n = 8

    0 a
	1 b           a
	1 c = a + b   b           a
	2             c = a + b   b
	3                         c = a + b
	5
	8
	13
'''

# assuming user will enter n > 2
a, b = 0, 1 # creating multiple variables in a single line
print(a)
print(b)

# 1 - 6 : 1 - (n-2)
for v in range(1, n - 2 + 1):
    c = a + b
    print(c)
    a, b = b, c
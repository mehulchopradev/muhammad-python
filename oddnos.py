n = int(input('Enter n: '))

# looping statements
# while loop
'''
while <<condition True or False>>:
    I1
    I2
    I3
'''

''' i = 0
while i <= n:
    if i % 2:
        print(i)
    i = i + 1 '''

# for loop (Perferred in python)
'''
for v in <<sequence of elements>>:
    I1
    I2
    I3

Sequence of elements
3 - for loop will move 3 times
10 - for loop will move 10 times
'''

# 0 - n
# 0 - 20
# 0 - 30
# range(0, n + 1)
''' for v in range(0, n + 1):
    if v % 2:
        print(v) '''

for v in range(1, n + 1, 2): # n = 9: (range(1, 10, 2) -> (1, 3, 5, 7, 9))
    print(v)

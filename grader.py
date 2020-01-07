marks = float(input('Enter marks: '))

'''
>= 70 - A
>= 60 - B
>= 40 - C
< 40 - F
> 100 or < 0 - I
'''
# more than 2 branches
# if - elif - elif - **** - else
'''
if <<condition True or False>>:
    I1
    I2
    I3
elif <<condition True or False>>:
    I4
    I5
elif <<condition True or False>>:
    I6
else:
    I7
    I8
'''
if marks > 100 or marks < 0:
    print('I')
elif marks >= 70:
    print('A')
elif marks >= 60:
    print('B')
elif marks >= 40:
    print('C')
else:
    print('F')


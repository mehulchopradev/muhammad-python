# import a module in another module
import series

# import the functions directly from the module, rather than importing the module
# PYTHONPATH

# conflict between the user defined module and built in module
# organize modules into packages

# from com.abc.lib.math import even_or_odd
import com.abc.lib.math as mymath
from math import factorial as fact

while True:
    # print('1. Fibo series\n2. Odd series\n3. Even or odd\n4. Factorial\n5. Exit')
    print('1. Fibo series', '2. Odd series', '3. Even or odd', '4. Factorial', '5. Exit', sep='\n')
    choice = int(input('Please enter ur choice: '))

    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        n = int(input('Enter n: '))

    if choice == 1:
        print(series.get_fibo_series(n))
        # pass # ask python to ignore the empty block and not raise a syntax error
    elif choice == 2:
        print(series.get_odd_series(n))
    elif choice == 3:
        print(mymath.even_or_odd(n))
    elif choice == 4:
        print(fact(n))
    else:
        # exit
        break # breaks from the surrounding loop


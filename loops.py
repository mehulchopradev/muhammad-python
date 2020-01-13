for v in range(0, 30):
    if v % 2:
        continue # will not execute the rest of the statements of the loop and
        # directly jumps to the next element in the range
    print(v ** 3)
    print(v / 2)
pointers = [4, 5, 10, 6, 8, 9, 1, 3, 7, 10]

# generate a new list of only the odd elements from the pointers list (filtering)
''' odds = []
for pointer in pointers:
    if pointer % 2:
        odds.append(pointer)

print(odds) '''

# Pre requisite
# We should be generating a new list
# For comprehensions
odds = [pointer for pointer in pointers if pointer % 2]
print(odds)

''' evens = []
for pointer in pointers:
    if not pointer % 2 and pointer > 5:
        evens.append(pointer) '''

# generate a new list of even elements greater than 5 from the pointers list (filtering)
evens = [pointer for pointer in pointers if not pointer % 2 and pointer > 5]
print(evens)

# generate a new list of marks deducted by 1 from the pointers list (mapping)
''' deducted_marks = []
for pointer in pointers:
    deducted_marks.append(pointer - 1)
print(deducted_marks) '''

deducted_marks = [pointer - 1 for pointer in pointers]
print(deducted_marks)
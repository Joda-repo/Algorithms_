"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
max = MIN_ITEM
min = MAX_ITEM

print(array)
for i in array:
    if i > max:
        max = i
        pos_max = array.index(i)
    elif i < min:
        min = i
        pos_min = array.index(i)

array.pop(pos_max)
array.insert(pos_max, min)
array.pop(pos_min)
array.insert(pos_min, max)
print(array)

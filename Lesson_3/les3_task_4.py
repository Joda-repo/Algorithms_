"""
Определить, какое число в массиве встречается чаще всего
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 4

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
max_f = 1
f = 0

for i in array:
    f = 0
    for k in array:
        if i == k:
            f = f + 1
    if max_f < f:
        max_f = f
        element = i

print(f"Число {element} количество повторений - {max_f}")

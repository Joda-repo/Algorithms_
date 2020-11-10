"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к
задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
"""

import random

SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
max_min = MIN_ITEM
for i in array:
    if i < 0:
        if max_min < i:
            max_min = i

print(max_min)
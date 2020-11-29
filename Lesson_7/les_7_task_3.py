"""Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима)."""

import random

MIN_ITEM = -100
MAX_ITEM = 99
SIZE = 10
n = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * n + 1)]
i = 0


def median(arr):
    global i
    flag = False
    if arr == 0:
        return f"0 медианы нет"

    less = []
    more = []
    median_num = arr[i]

    for item in arr:
        if item == median_num:
            pass
        elif item > median_num:
            more.append(item)
        elif item < median_num:
            less.append(item)

    if len(less) == (len(arr) // 2) and len(more) == (len(arr) // 2):
        less.append(median_num)
        print(f"{array}\nМедиана: {median_num}")
        flag = True
    if not flag:
        i += 1
        median(arr)
    return None


median(array)

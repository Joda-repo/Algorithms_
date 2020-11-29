"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
 [0; 50). Выведите на экран исходный и отсортированный массивы."""
import random

MIN_ITEM = 0
MAX_ITEM = 49.99
SIZE = 10

array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_cut = [round(_, 2) for _ in array]  # не могу видеть больше 2-4 чисел после запятой
print(array_cut)


def merge_sort(data):
    count = len(data)
    if count > 2:
        part_1 = merge_sort(data[:count // 2])
        part_2 = merge_sort(data[count // 2:])
        data = part_1 + part_2
        last_index = len(data) - 1

        for i in range(last_index):
            min_value = data[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > data[j]:
                    min_value = data[j]
                    min_index = j

            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]

    elif len(data) > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    return data


print(merge_sort(array_cut))

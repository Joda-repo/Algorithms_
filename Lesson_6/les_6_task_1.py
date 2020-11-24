"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

Данные моего интерпретатора: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32

task_1 занимает меньше всего места так не используются дополнительные переменные из-за "трюка" array[imax], array[imin]
 = array[imin], array[imax]
"""

import random
import sys

total = 0


def task_0(SIZE, MIN_ITEM, MAX_ITEM):  # первый вариант исходный.
    print(f"\n {'-' * 100}")
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
    print(f"\n{'-' * 100}\n")
    return locals()


"""
type(x)=<class 'dict'>, sys.getsizeof(x)=196, x={'SIZE': 10, 'array': [7, 17, 94, 30, 44, 73, 22, 94, 26, 71],
 'max': 94, 'min': 17, 'i': 71, 'pos_max': 1, 'pos_min': 7, 'MAX_ITEM': 100, 'MIN_ITEM': 0}
Переменная : SIZE, размер:  14
Переменная : array, размер:  92
Переменная : max, размер:  14
Переменная : min, размер:  14
Переменная : i, размер:  14
Переменная : pos_max, размер:  14
Переменная : pos_min, размер:  14
Переменная : MAX_ITEM, размер:  14
Переменная : MIN_ITEM, размер:  12
Размер всех переменных в функции : 202"""


def task_1(SIZE, MIN_ITEM, MAX_ITEM):  # второй вариант, с использованием ранее запрещеной функции max & min и подмены
    # значений без переменных
    print(f"\n {'-' * 100} \n")
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(array)
    imax = array.index(max(array))
    imin = array.index(min(array))
    array[imax], array[imin] = array[imin], array[imax]
    print(array)
    print(f"\n{'-' * 100}\n")
    return locals()


"""type(x)=<class 'dict'>, sys.getsizeof(x)=196, x={'SIZE': 10, 'array': [100, 27, 1, 38, 32, 33, 2, 61, 44, 43],
 'imax': 2, 'imin': 0, 'MAX_ITEM': 100, 'MIN_ITEM': 0}
Переменная : SIZE, размер:  14
Переменная : array, размер:  92
Переменная : imax, размер:  14
Переменная : imin, размер:  12
Переменная : MAX_ITEM, размер:  14
Переменная : MIN_ITEM, размер:  12
Размер всех переменных в функции : 158"""


def task_2(SIZE, MIN_ITEM, MAX_ITEM):  # третий вариант, проверить размер
    print(f"\n {'-' * 100} \n")
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(array)
    imax = array.index(max(array))
    imin = array.index(min(array))
    array[imax], array[imin] = array[imin], array[imax]
    final_tup = tuple(array)
    print(final_tup)
    print(f"\n{'-' * 100}\n")
    return locals()


""""
type(x)=<class 'dict'>, sys.getsizeof(x)=196, x={'SIZE': 10, 'array': [11, 42, 4, 88, 26, 43, 72, 53, 90, 5],
 'imax': 2, 'imin': 8, 'final_tup': (11, 42, 4, 88, 26, 43, 72, 53, 90, 5), 'MAX_ITEM': 100, 'MIN_ITEM': 0}
Переменная : SIZE, размер:  14
Переменная : array, размер:  92
Переменная : imax, размер:  14
Переменная : imin, размер:  14
Переменная : final_tup, размер:  60
Переменная : MAX_ITEM, размер:  14
Переменная : MIN_ITEM, размер:  12
Размер всех переменных в функции : 220"""


def show(x):
    global total
    total = 0
    print(f'{type(x)=}, {sys.getsizeof(x)=}, {x=}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                print(f'Переменная : {key}, размер:  {sys.getsizeof(value)}')
                total += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)
    return f'Размер всех переменных в функции : {total}'


print(show(task_0(10, 0, 100)))
print(show(task_1(10, 0, 100)))
print(show(task_2(10, 0, 100)))

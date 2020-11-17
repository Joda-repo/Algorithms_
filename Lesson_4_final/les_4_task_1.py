"""
 Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
Выбранная задача: Определить, какое число в массиве встречается чаще всего les3_task_4.py
"""

"""
Вывод: 
при сравнени main_1 и main_2 зависимость с указаными значениями линейная. При это в функции main() линейная зависимость
превращается в гиперболическую с увеличением количества данных. (Вот что занчит если функцию пишет студент или "доку")
Сравнивая main_1 и main_2 то конечно main_1 лучше так как в main_2 добавлен словарь, однако в случае со словарем у тебя 
есть количество всех значений, а даже при масиве в тысячу значений разница 0.15993429999999997(main_1) vs  0.18107679999999998 (main_2)
График тут: https://drive.google.com/file/d/1lX5-ijLXGEwVkGkNxO5D8kiGp8J2oM_F/view?usp=sharing
P.S. Решил написать вывод вначале убив тем самым интригу, но съэкономив время на листание кода
"""

import cProfile
import random
import timeit


def calc(f):
    return calc(f) + 1


def main(SIZE, MIN_ITEM, MAX_ITEM): # Решение без использования max()
    #   SIZE = 10
    #   MIN_ITEM = 0
    #   MAX_ITEM = 4
    global element

    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

    # print(array)
    max_f = 1

    for i in array:
        f = 0
        for k in array:
            if i == k:
                f = f + 1
        if max_f < f:
            max_f = f
            element = i

    return f"Число {element} количество повторений - {max_f}"


cProfile.run('main(10, 0, 20)')
"""
    58 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:14(main)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:20(<listcomp>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
cProfile.run('main(20, 0, 20)')
"""
 113 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:14(main)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:20(<listcomp>)
       20    0.000    0.000    0.000    0.000 random.py:200(randrange)
       20    0.000    0.000    0.000    0.000 random.py:244(randint)
       20    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       28    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
cProfile.run('main(30, 0, 20)')
"""
172 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:14(main)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:20(<listcomp>)
       30    0.000    0.000    0.000    0.000 random.py:200(randrange)
       30    0.000    0.000    0.000    0.000 random.py:244(randint)
       30    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       30    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       47    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

print(timeit.timeit('main(10, 0, 20)', number=100, globals=globals()))  # 0.002423399999999999
print(timeit.timeit('main(20, 0, 20)', number=100, globals=globals()))  # 0.005364800000000003
print(timeit.timeit('main(30, 0, 20)', number=100, globals=globals()))  # 0.009171699999999991
print(timeit.timeit('main(40, 0, 20)', number=100, globals=globals()))  # 0.013585
print(timeit.timeit('main(50, 0, 20)', number=100, globals=globals()))  # 0.01902100000000001


def main_1(SIZE, MIN_ITEM, MAX_ITEM):   # Решение с использованием max()
    #   SIZE = 10
    #   MIN_ITEM = 0
    #   MAX_ITEM = 4

    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return max(array)


cProfile.run('main_1(10, 0, 20)')
"""
60 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:50(main_1)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:55(<listcomp>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       14    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
cProfile.run('main_1(20, 0, 20)')
"""
  119 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:50(main_1)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:55(<listcomp>)
       20    0.000    0.000    0.000    0.000 random.py:200(randrange)
       20    0.000    0.000    0.000    0.000 random.py:244(randint)
       20    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       33    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
cProfile.run('main_1(30, 0, 20)')
"""
 171 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:50(main_1)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:55(<listcomp>)
       30    0.000    0.000    0.000    0.000 random.py:200(randrange)
       30    0.000    0.000    0.000    0.000 random.py:244(randint)
       30    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       30    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       45    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

print(timeit.timeit('main_1(10, 0, 20)', number=100, globals=globals()))    # 0.0017710000000000087
print(timeit.timeit('main_1(20, 0, 20)', number=100, globals=globals()))    # 0.003381099999999998
print(timeit.timeit('main_1(30, 0, 20)', number=100, globals=globals()))    # 0.004932099999999995
print(timeit.timeit('main_1(40, 0, 20)', number=100, globals=globals()))    # 0.0064992999999999995
print(timeit.timeit('main_1(50, 0, 20)', number=100, globals=globals()))    # 0.00793199999999998


def main_2(SIZE, MIN_ITEM, MAX_ITEM):   # Решение через словарь с использованием max()
    #   SIZE = 10
    #   MIN_ITEM = 0
    #   MAX_ITEM = 4

    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    my_dict = dict((_, 0) for _ in array)

    for i in array:
        my_dict[i] = my_dict[i] + 1
    inverse = [(value, key) for key, value in my_dict.items()]
    return max(inverse)[1]

cProfile.run('main_2(10, 0, 20)')
"""
 74 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:70(main_2)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:75(<listcomp>)
       11    0.000    0.000    0.000    0.000 les_4_task_1.py:76(<genexpr>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:80(<listcomp>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       15    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
"""
cProfile.run('main_2(20, 0, 20)')
"""
 141 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:70(main_2)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:75(<listcomp>)
       21    0.000    0.000    0.000    0.000 les_4_task_1.py:76(<genexpr>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:80(<listcomp>)
       20    0.000    0.000    0.000    0.000 random.py:200(randrange)
       20    0.000    0.000    0.000    0.000 random.py:244(randint)
       20    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       32    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}"""
cProfile.run('main_2(30, 0, 20)')
"""
207 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:70(main_2)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:75(<listcomp>)
       31    0.000    0.000    0.000    0.000 les_4_task_1.py:76(<genexpr>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:80(<listcomp>)
       30    0.000    0.000    0.000    0.000 random.py:200(randrange)
       30    0.000    0.000    0.000    0.000 random.py:244(randint)
       30    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       30    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       48    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}"""


print(timeit.timeit('main_2(10, 0, 20)', number=100, globals=globals()))    # 0.002347999999999989
print(timeit.timeit('main_2(20, 0, 20)', number=100, globals=globals()))    # 0.004297699999999988
print(timeit.timeit('main_2(30, 0, 20)', number=100, globals=globals()))    # 0.006145700000000004
print(timeit.timeit('main_2(40, 0, 20)', number=100, globals=globals()))    # 0.007850999999999997
print(timeit.timeit('main_2(50, 0, 20)', number=100, globals=globals()))    # 0.009717299999999984
"""
 Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.

"""
"""
Вывод: реализация функции prime() показала наибольшую успешность так как в функции sieve границы массива выбраны приблизительно
"""

import cProfile
import timeit


def sieve(n):
    q = n ** 2 + 2
    sieve = [i for i in range(q)]  # списки list только для алгоритма решето Эратосфена, а не для ПЗ к уроку 2

    sieve[1] = 0
    for i in range(2, q):
        if sieve[i] != 0:
            j = i + i
            while j < q:
                sieve[j] = 0
                j += i

    for k in range(0, sieve.count(0)):
        sieve.remove(0)

    return sieve[n - 1]


cProfile.run('sieve(40)')
"""
1357 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.001    0.001    0.004    0.004 les_4_task_2.py:5(sieve)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:7(<listcomp>)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1351    0.003    0.000    0.003    0.000 {method 'remove' of 'list' objects}
"""
cProfile.run('sieve(50)')
"""
 2142 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.001    0.001    0.009    0.009 les_4_task_2.py:5(sieve)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:7(<listcomp>)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2136    0.007    0.000    0.007    0.000 {method 'remove' of 'list' objects}
"""
cProfile.run('sieve(60)')
"""
 3106 function calls in 0.016 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.016    0.016 <string>:1(<module>)
        1    0.002    0.002    0.016    0.016 les_4_task_2.py:5(sieve)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:7(<listcomp>)
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     3100    0.014    0.000    0.014    0.000 {method 'remove' of 'list' objects}"""

print(timeit.timeit('sieve(40)', number=100, globals=globals()))    # 0.3795044
print(timeit.timeit('sieve(50)', number=100, globals=globals()))    # 0.8153091000000001
print(timeit.timeit('sieve(60)', number=100, globals=globals()))    # 1.5358761999999997
print(timeit.timeit('sieve(70)', number=100, globals=globals()))    # 2.6876775000000004
print(timeit.timeit('sieve(80)', number=100, globals=globals()))    # 4.3687826


def prime(p):
    prime = []
    i = 0
    while True:
        i = i + 1
        if len(prime) == p:
            return prime[p - 1]
        if i % 2 != 0:
            prime.append(i)


cProfile.run('prime(40)')
"""
  124 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:34(prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       80    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       40    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
cProfile.run('prime(50)')
"""
54 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:34(prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      100    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
cProfile.run('prime(60)')
"""
  184 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:34(prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      120    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       60    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print(timeit.timeit('prime(40)', number=100, globals=globals()))    # 0.001931799999999484
print(timeit.timeit('prime(50)', number=100, globals=globals()))    # 0.002415000000000944
print(timeit.timeit('prime(60)', number=100, globals=globals()))    # 0.002901200000000159
print(timeit.timeit('prime(70)', number=100, globals=globals()))    # 0.0033741000000002686
print(timeit.timeit('prime(80)', number=100, globals=globals()))    # 0.00388389999999994

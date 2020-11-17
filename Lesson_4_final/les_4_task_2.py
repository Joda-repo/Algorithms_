"""
 Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
 вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».

Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.

"""
"""
Вывод: Метод эратосфера показал себя на порядок лучше чем сделанный студентом. Плюс после определенного значения растет
экспоненциально.
"""
import cProfile
import timeit


def sieve(n):
    q = n ** 2 + 2
    sieve_final = [i for i in range(q)]  # списки list только для алгоритма решето Эратосфена, а не для ПЗ к уроку 2

    sieve_final[1] = 0
    for i in range(2, q):
        if sieve_final[i] != 0:
            j = i + i
            while j < q:
                sieve_final[j] = 0
                j += i

    for k in range(0, sieve_final.count(0)):
        sieve_final.remove(0)

    return sieve_final[n - 1]


cProfile.run('sieve(10)')
"""
    82 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:21(sieve)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:23(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       76    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}      
"""
cProfile.run('sieve(15)')
"""
  185 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:21(sieve)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:23(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      179    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
"""
cProfile.run('sieve(20)')
"""
   329 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 les_4_task_2.py:21(sieve)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:23(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      323    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}"""

print(timeit.timeit('sieve(10)', number=100, globals=globals()))  # 0.005970900000000001
print(timeit.timeit('sieve(15)', number=100, globals=globals()))  # 0.016969899999999996
print(timeit.timeit('sieve(20)', number=100, globals=globals()))  # 0.0424007
print(timeit.timeit('sieve(25)', number=100, globals=globals()))  # 0.0858707
print(timeit.timeit('sieve(30)', number=100, globals=globals()))  # 0.15131319999999998


def prime(n):
    prime_res = list()
    for num in range(1, n ** 2 + 3):
        check = True
        for i in range(2, num):
            if (num % i == 0):
                check = False
        if check:
            prime_res.append(num)
    prime_res.remove(1)
    return prime_res[n - 1]


cProfile.run('prime(10)')
"""
  32 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:87(prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       27    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

"""
cProfile.run('prime(15)')
"""
    55 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.002    0.002    0.002    0.002 les_4_task_2.py:85(prime)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
       50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

"""
cProfile.run('prime(20)')
"""
  85 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
        1    0.005    0.005    0.005    0.005 les_4_task_2.py:85(prime)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
       80    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
"""

print(timeit.timeit('prime(10)', number=100, globals=globals()))  # 0.033434500000000034
print(timeit.timeit('prime(15)', number=100, globals=globals()))  # 0.15870109999999998
print(timeit.timeit('prime(20)', number=100, globals=globals()))  # 0.5126138000000001
print(timeit.timeit('prime(25)', number=100, globals=globals()))  # 1.3010229
print(timeit.timeit('prime(30)', number=100, globals=globals()))  # 2.8742813

"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
 [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
сортировки, например, расчёской, шейкерная и другие в зачёт не идут."""
import random

MIN_ITEM = -100
MAX_ITEM = 99
SIZE = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def smart_buble(arr):
    for i in range(0, len(arr) - 1):
        flag = True
        print(arr)
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            return arr
    return arr


print(smart_buble(array))

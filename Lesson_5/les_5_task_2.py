from collections import deque

"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


def sum_hex(x, y):
    hex_sum_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                    'C': 12, 'D': 13, 'E': 14, 'F': 15,
                    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    check = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)

    while x:

        if y:
            res = hex_sum_dict[x.pop()] + hex_sum_dict[y.pop()] + check

        else:
            res = hex_sum_dict[x.pop()] + check

        check = 0

        if res < 16:
            result.appendleft(hex_sum_dict[res])

        else:
            result.appendleft(hex_sum_dict[res - 16])
            check = 1

    if check:
        result.appendleft('1')

    return list(result)


def mult_hex(x, y):
    hex_multi_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                      'C': 12, 'D': 13, 'E': 14, 'F': 15,
                      0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                      12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    check = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = hex_multi_dict[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            check[i].appendleft(m * hex_multi_dict[x[j]])

        for _ in range(i):
            check[i].append(0)

    transfer = 0

    for _ in range(len(check[-1])):
        res = transfer

        for i in range(len(check)):
            if check[i]:
                res += check[i].pop()

        if res < 16:
            result.appendleft(hex_multi_dict[res])

        else:
            result.appendleft(hex_multi_dict[res % 16])
            transfer = res // 16

    if transfer:
        result.appendleft(hex_multi_dict[transfer])

    return list(result)


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())


print(*a, '+', *b, '=', *sum_hex(a, b))

print(*a, '*', *b, '=', *mult_hex(a, b))

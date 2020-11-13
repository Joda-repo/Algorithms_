"""В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""
result = [0] * 8

for x in range(1, 100):
    for y in range(2, 10):
        if x % y == 0:
            result[y - 2] += 1

for i in range(2, 10):
    print(f"Количество чисел кратных {i} равно : {result[i - 2]}")


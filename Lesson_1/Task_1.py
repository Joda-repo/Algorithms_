# https://app.diagrams.net/#G14JSzgxB8LDDaGxumIbRW_rozgviJzYUX
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = input("Введите трёхзначное число: ")

# решение через дополнительные переменные
n = int(num)
a = n // 100
b = n % 100 // 10
c = n % 10
summary = a + b + c
print(f"Сумма = {summary}")
print(f"Произведение = {a * b * c}")

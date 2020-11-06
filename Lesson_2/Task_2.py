chet = 0
nechet = 0
n = str(input("Введите число, которое будет разобрано на состовляющие : "))
for i in n:
    if int(i) % 2 == 0:
        chet += 1
    else:
        nechet += 1
print(f"Количество четных : {chet}\nКоличество нечетных : {nechet}")

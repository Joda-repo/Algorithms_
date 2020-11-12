#https://drive.google.com/file/d/1AnfJ74rVbU7Oamcn6EpBB1NJ6LuZlN42/view?usp=sharing
#Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
# цифры (4, 6 и 0) и 2 нечетные (3 и 5).

chet = 0
nechet = 0
n = str(input("Введите число, которое будет разобрано на состовляющие : "))
for i in n:
    if int(i) % 2 == 0:
        chet += 1
    else:
        nechet += 1
print(f"Количество четных : {chet}\nКоличество нечетных : {nechet}")

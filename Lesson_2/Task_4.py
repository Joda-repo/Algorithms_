n=int(input("Введите число : "))
s = 0
i = 1
while i != n+1:
    if i % 2 == 0:
        s =s + (1 / (i ** 2)) * (-1)
        i +=1
    else:
        s = s + 1 / (i ** 2)
        i += 1

print(s)
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

first = ord(input('1-я буква: '))
second = ord(input(' 2-я буква (1-я буква не равна 2-я буква): '))
first = first - ord('a') + 1
second = second - ord('a') + 1
print(f"Порядковый номер 1-й буквы = {first}, 2-й = {second}")
print(f"Число букв между введенными: {abs(first - second) - 1}")

import string

a = string.ascii_lowercase

print(a)

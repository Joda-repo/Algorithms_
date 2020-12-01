import hashlib
import random

alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя123456789'
lenght = int(input("Введите длинну строки : "))
array = ''.join(random.choices(alphabet, k=lenght))
result = set()


def sub(arr):
    for i in range(len(arr)):
        for j in range(len(arr), i, -1):
            hash_str = hashlib.sha256(arr[i:j].encode('utf-8')).hexdigest()
            result.add(hash_str)
    return f'{len(result) - 1} различных подстрок в строке {arr}'


print(sub('abcd'))
print(sub(array))

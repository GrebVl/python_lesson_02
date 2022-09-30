# Задание 5 Реализуйте алгоритм перемешивания списка.
import random

N = int(input('Введите число N '))

list_ = []

for i in range(-N, N+1):
    list_.append(i)

for j in range(-N, N+1):
    list_[j] = random.randrange(-N, N + 1)

print(list_)
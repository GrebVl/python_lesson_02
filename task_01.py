# Задание 1 Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#
# Пример:
#
# 6782 -> 23
# 0,56 -> 11

num_ = str(input('Введите чесло: '))
if num_.isdigit() == False:
    num_ = num_.replace(":", "0")
    num_ = num_.replace(" ", "0")
    num_ = num_.replace(";", "0")
    num_ = num_.replace(".", "0")
    num_ = num_.replace(",", "0")

print(num_)
summ_ = 0
for i in range(len(num_)):
    summ_ += int(num_[i])
print(summ_)


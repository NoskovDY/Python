﻿# Урок 6. Задание 3.
# Вводятся целые числа A и B. Гарантируется, что A ≤ B.
# Выведите все четные числа на заданном отрезке через пробел.

# Решение

# Помещаем введенные по запросу числа в переменные
print('Введите целые числа A и B, A должно быть меньше B')
A = int(input('A = '))
B = int(input('B = '))
# цикл для перебора чисел в диапазоне и проверки их на четность
for i in range (A, B+1):
    if i%2==0:
        print(i, end=' ') # выводим числа в одну строку с пробелами
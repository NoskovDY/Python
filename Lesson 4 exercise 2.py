﻿# Урок 4. Задание 2.
# Дано пятизначное целое число. Напишите алгоритм, который возведёт количество десятков в степень количества единиц.
# Затем умножит это число на количество сотен. И делит получившееся число на разность количества десятков тысяч
# и количества тысяч Например, есть число 46275 Необходимо возвести 7 (десятки) в степень 5 (единицы),
# умножить получившееся число на 2 (сотни), и разделить на разность между 4 (десятки тысяч) и 6 (тысячи) то есть (4-6)
# В результате необходимо получить вещественное число. В нашем примере это будет: -16807.0

# Решение

# Помещаем введенное по запросу число в переменную
a= int(input('Пожалуйста введите пятизночное целое число : '))

# Вычисляем значения разрядов этого числа
d1=(a//10000%10)
d2=(a//1000%10)
d3=(a//100%10)
d4=(a//10%10)
d5=(a%10)

# Последовательно выводим текст с объяснением наших действий, выполняем операцию и выводим текст операции и результат
print()
print ('Возведем количество десятков ',d4,' в степень количества единиц ',d5," :")
res1=d4**d5
print (d4,'**',d5,'=',res1)
print()
print ('умножим это число на количество сотен ',d3," :")
res2=res1*d3
print (res1,'*',d3,'=',res2)
print()
print ('и разделим получившееся число на разность количества десятков тысяч ',d1,' и количества тысяч ',d2," :")
res3=d1-d2
resfin=float(res2/res3)
print (res2,'/(',d1,'-',d2,')=',res2,'/',res3,'=',resfin)
print()
# Проверем результат вычислением в одном выражении
print('Проверим вычислением в одном выражении :' )
resfin2=float(d4**d5*d3/(d1-d2))
print(d4,'**',d5,'*',d3,'/(',d1,'-',d2,')=',resfin2)
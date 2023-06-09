﻿# Урок 3. Задание 2.
# А теперь мы с тобой напишем форму ввода ответа на тест по биологии 
# для студентов. Он должен запрашивать по порядку этапы развития человека 
# (проверим твое умение гуглить, что тоже очень важно для программиста.)
# и в конце вывести все стадии, разделенные знаком =>, что будет означать 
# постепенный переход от одного к другому. В следующих уроках мы дополним эту 
# форму до полноценного теста, который будет проверять правильность ответов, 
# а пока -начнем с малого. Напоминаем, что разделить эти данные тебе поможет 
# команда sepвнутри команды print, например, чтобы разделить переменные
# знаком +нужно ввести: print(a1, a2, a3, sep='+')Подсказка: последняя
# стадия развития -Homo sapiens sapiens.

# Решение
# Помещаем в переменные правильные значения, что возможно понадобиться 
# в следующих заданиях
stage1 = "Australopithecus"
stage2 = "Homo habilis"
stage3 = "Homo erectus"
stage4 = "Homo neanderthalensis"
stage5 = "Homo sapiens sapiens"

# Выводим текст теста
print ('Выделяют 5 основных этапов эволюции человека. Укажите их по порядку.')
# Помещаем в дугие переменные ответы 
test_stage1 = input("Первый этап :  ")
test_stage2 = input("Второй этап :  ")
test_stage3 = input("Третий этап :  ")
test_stage4 = input("Четвертый этап :  ")
test_stage5 = input("Пятый этап :  ")


print ("Вы указали этапы в следующем порядке:")
# Выводим переменные с ответами с разделением =>
print (test_stage1, test_stage2, test_stage3, test_stage4, test_stage5, sep=" => ")

# Так же выводим правильный ответ
print ("Пожалуйста сравните с правильным ответом:")
print (stage1, stage2, stage3, stage4, stage5, sep=" => ")


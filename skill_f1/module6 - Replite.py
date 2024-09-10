# numbers = int(input("Введите число: "))
# number = 1
# while number <= numbers:
#     summ = number ** 3
#     print(f"{number} ** 3 = {summ}")
#     number += 1
import random

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# name = input('Введите имя должника ')
# summ = int(input('Введите сумму долга '))
# print(f'{name}, ваша задолженность составляет {summ} рублей ')
# summ2 = int(input(f'Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
# while summ2 < summ:
#     summ2 = int(input(f'Маловато, {name}. Давайте еще раз '))
# else:
#     print(f'Отлично, {name}! Вы погасили долг. Спасибо!')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
# i = 0
# numbers = int(input('Введите число: '))
# if numbers == 0:
#     numbers += 1
# while numbers > 0:
#     numbers = numbers // 10
#     i += 1
# print(f'Ответ: {i}')
# #
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# positive = 0
# negative = 0
# numbers = True
# # numbers = int(input('Поставте оценку, от -100 до 100: '))
# while numbers != 0:
#     numbers = int(input('Поставте оценку, от -100 до 100: '))
#     if numbers > 0:
#         positive += 1
#         # numbers = int(input('Введите число: '))
#     elif numbers < 0:
#         negative += 1
#         # numbers = int(input('Введите число: '))
# print(f'Кол-во положительных чисел: {positive}\nКол-во отрицательных чисел: {negative}')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# hour = 0
# task2 = 0
# call2 = False
# print('Начался 8-часовой рабочий день')
# while hour < 8:
#     hour += 1
#     task = int(input(f'{hour} час\nСколько задач решит Максим '))
#     task2 += task
#     call = int(input('Звонит жена. Взять трубку? (1-да, 0-нет) '))
#     call2 += call
#     if call > 0:
#         call2 = True
# print(f'Рабочий день закончился. Всего выполнено задач: {task2}')
# if call2:
#     print('Нужно зайти в магазин')

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# x = float(input('Введите сумму вклада '))
# p = float(input('Введите процент по вкладу '))
# y = int(input('Введите ожидаемую сумму '))
# procent = (x / 100) * p
# year = int(y / procent)
# print(year)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# import random
#
# numbers = random.randint(1, 10)
# number = True
# score = 0
# while number != numbers:
#     number = int(input('Ведите число '))
#     score += 1
#     if number > numbers:
#         print('Число больше, чем нужно. Попробуйте еще раз!')
#     elif number < numbers:
#         print('Число меньше, чем нужно. Попробуйте ещё раз!')
# print(f'Вы угадали! Число попыток: {score}')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

#
# number_min = 0
# number_max = 100
# N = (100 + 1) // 2
# N1 = 0
# N2 = 0
# while True:
#     print(f'твое число равно, больше или меньше числа, {N}?')
#     answer = int(input('1 - равно, 2 - больше, 3 - меньше: '))
#     if answer == 1:
#         print('Я угадал!')
#         break
#     elif answer == 2:
#         number_min = N
#         N = (N + number_max) // 2
#         print(number_min, number_max)
#     elif answer == 3:
#         number_max = N
#         N = (N + number_min) // 2
#         print(number_min, number_max)

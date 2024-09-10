# number = 0
# score = 0
# for numbers in range(1, 11):
#     score += 1
#     numbers = int(input(f'введите {score} число: '))
#     if numbers > 0 and numbers % 2 == 0:
#         number += 1
# print(f'чётных и положительных чисел: {number}')

# ////////////////////////////////////////////////////////////////////////////////////////////////////////
# summ = 0
# score = 0
# for numbers in range(1, 13):
#     score += 1
#     numbers = int(input(f'Введите зарплату за {score} месяц '))
#     summ += numbers
# print('средняя зарплата за год составляет: ', summ / 12)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# N = int(input('Введите число '))
# factorial = N
# for i in range(1, N):
#     factorial *= i
# print(factorial)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////
# three = 0
# four = 0
# five = 0
# scholar = int(input('Введите количество учеников: '))
# for rating in range(1, scholar + 1):
#     rating = int(input('Введите оценку по информатике: '))
#     if rating == 3:
#         three += 1
#     elif rating == 4:
#         four += 1
#     elif rating == 5:
#         five += 1
# if three > four and three > five:
#     print('Сегодня троечников больше')
# elif four > three and four > five:
#     print('Сегодня хорошистов больше')
# elif five > three and five > four:
#     print('Сегодня отличник больше')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
# summ = 0
# score = 0
# number_a = int(input('Введите первое число '))
# number_b = int(input('Введите вророе число '))
# for numbers in range(number_a, number_b + 1):
#     if numbers % 3 == 0:
#         score += 1
#         summ += numbers
# arithmetic = summ / score
# print(f'Средне арифметическое число: {arithmetic}')

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# for i in range(10, 100):
#     ten = i // 10
#     unit = i % 10
#     if ten * unit * 3 == i:
#         print(f'число {i} равно оригиналу')

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

# summ = 0
# summ2 = 0
# N = int(input('введите колличество карточек: '))
# for numbers_1 in range(1, N):
#     numbers_1 = int(input('Введите номера оставшейся карточки: '))
#     summ += numbers_1
# for numbers_2 in range(1, N + 1):
#     summ2 += numbers_2
# print('Номер пропавшей карточки:',summ2 - summ)

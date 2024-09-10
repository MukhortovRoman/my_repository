# month = 0
# for meal in range(100, -4, -4):
#     print('Через', month, 'месяцев у вас осталось',meal,'килограммов гречки')
#     month += 1

# //////////////////////////////////////////////////////////////////////////////////////////////////////////
# credit_total = 0
# people_total = int(input('Введите количество должников: '))
# for people in range(0, people_total, 5):
#     print('должник с номером', people)
#     credit = int(input('Сколько должны? '))
#     credit_total += credit
# print('Общая сумма долга:', credit_total)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////

# time = int(input('Введите время разогрева: '))
# hot = False
# for reverse_timer in range(time, 0, -1):
#     print('Осталось', reverse_timer, 'минут')
#     hot = int(input('Остановить таймер? 0 - нет. 1 - да '))
#     if hot == True:
#         print('Ваша еда готова, можете забрать, осталось', reverse_timer, 'сек.')
#         break
# else:
#     print('Ваша еда готова, осторожно горячo!')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# numbers = 0
# score = 0
# number_a = int(input('Введите число "A": '))
# number_b = int(input('Введите число "B": '))
# number_c = int(input('Введите число "C": '))
# for i in range(number_a, number_b + 1):
#     if i % number_c == 0:
#         numbers += i
#         score += 1
# print(numbers // score)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////


# start = int(input('Введите начало отрезка: '))
# stop = int(input('Введите конец отрезка: '))
# step = int(input('Введите шаг: '))
# if start < stop:
#     start, stop = stop, start
# if step > 0:
#     step *= -1
# for x in range(start, stop - 1, step):
#     y = x ** 3 + 2 * x ** 2 - 4 * x + 1
#     print('В точке', start, 'функция равна', y)
#     start += step

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
# money_full = 0
# educational_grant = int(input('Введите стипендию: '))
# expenses = int(input('Введите расходы на проживание: '))
# print()
# while expenses < educational_grant:
#     expenses = int(input('Введите все расходы на проживание: '))
# for month in range(1, 11):
#     money = expenses - educational_grant
#     money_full += money
#     money_full = round(money_full, 1)
#     print(f'{month}. месяц траты {expenses} не хватает {money_full}')
#     money_total = (expenses / 100) * 3
#     expenses += money_total
#     expenses = round(expenses, 1)
# print()
# print('Нужно спросить у родителей', money_full, 'рублей')

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

# summ = 0
# N = int(input('Введите N: '))
# for number in range(0, N):
#     elem = (-1) ** number * 1 / (2 ** number)
#     summ += elem
# print('Ответ:',summ)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

# boys = int(input('Введите кол-во мальчиков: '))
# girls = int(input('Введите кол-во девочек: '))
# answer = ''
# if (boys > 2 * girls) or (girls > 2 * boys):
#     print('Нет решения.')
# elif boys >= girls:
#     k = boys - girls
#     for bgb in range(k):
#         answer += 'BGB'
#     for bg in range(girls - k):
#         answer += 'BG'
# else:
#     k = girls - boys
#     for gbg in range(k):
#         answer += 'GBG'
#     for gb in range(boys - k):
#         answer += 'GB'
# print(answer)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////



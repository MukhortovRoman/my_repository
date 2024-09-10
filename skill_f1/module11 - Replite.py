# euro = float(input('Введите стоимоть покупки в евро: '))
#
# dollar = euro * float(1.25)
# ruble = dollar * float(60.87)
#
# print(f'Стоимость покупки {round(ruble, 2)} рублей')

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import math
#
# score = 0
# numbers = int(input('Введите кол-во чисел: '))
#
# while score < numbers:
#     number = float(input(f'Введите число {score + 1}: '))
#     score += 1
#
#     if number > 0:
#         num = math.ceil(number)
#         x = math.log(num)
#
#         print(f'x = {num}  log(x) = {x}')
#         print()
#     else:
#         num = math.floor(number)
#         x = math.exp(num)
#
#         print(f'x = {num}  log(x) = {x}')
#         print()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import math
#
# percent = 0
# size2 = 0
# score = 0
# size = float(input('Введите размер файла: '))
# speed = float(input('введите скорость интернет соединения: '))
# print()
#
# if size < 0 or speed < 0:
#     print('Не корректный ввод')
# else:
#     i = size / speed
# while score <= i:
#     score += 1
#     size2 += size / i
#     percent = size2 * 100 / size
#     if percent >= 100:
#         size2 = size
#         percent = 100
#
#     print(f'Прошло {score} сек. Скачано {int(size2)} из {int(size)} Мб ({math.ceil(percent)}%)')

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# x = float(input('Введите положительное действительное число: '))
#
# print(int((x - int(x)) * 10))
#
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
# import math
#
# planet = float(input('Введите радиус случайной планеты: '))
# earth = round((4 / 3) * (math.pi * float(6378.1)) ** 3, 1)
#
# planet_volume = round((4 / 3) * (math.pi * planet) ** 3, 1)
# i = earth / planet_volume
# if earth > planet_volume:
#     print('Объем планеты земля больше в', round(i, 3), 'раз', end='')
# else:
#     difference = earth / planet_volume
#     difference_1 = planet_volume / earth
#
#     print(f'Объём планеты Земля меньше в (1/{round(difference, 3)}) = {round(difference_1, 3)} раз')

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# print('Введите месторасположения коня:')
# x = float(input('По горизонтали: '))
# y = float(input('По вертикали: '))
# x = int(x * 10)
# y = int(y * 10)
#
# print('Введите местоположение точки на доске: ')
# x1 = float(input('По горизонтали: '))
# y1 = float(input('По вертикали: '))
# x1 = int(x1 * 10)
# y1 = int(y1 * 10)
#
# if x < 0 or y > 8 or x < 0 or y > 8:
#     print('Клетки с такой координатой не существует')
# else:
#     print(f'Конь в клетке ({x}, {y}). Точка в клетки ({x1}, {y1})')
# if abs(x - x1) * abs(y - y1) == 2:
#     print('Да, конь может ходить в эту точку.')
# else:
#     print('Конь не может ходить в эту точку.')
#

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

# num1 = int(input('Введите первое число: '))
# num2 = int(input('введите второе число: '))
#
# num_max = ((num1 + num2) + abs(num1 - num2)) / 2
#
# print(f'Наибольшее число: {int(num_max)}')

# bet = int(input('Скролько ставим? '))
# coefficient = float(input('Какой коэффициент? '))
#
# win = round(bet * coefficient, 2)
#
# print('Потенциальный выигрыш: ', win)
# print(win)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# height = float(input('Ваш рост: '))
# weight = float(input('Ваш вес: '))
#
# bmi = round(weight / height ** 2, 2)
# print('Ваш индекс массы тела: ', bmi)
# if bmi < 18.5:
#     print('недобор')
# elif bmi < 25:
#     print('нормальный')
# elif bmi < 30:
#     print('избыток')
# else:
#     print('ожирение')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////


# age = int(input('Введите возраст: '))
# temperature = float(input('Введите температуру тела: '))
#
# print('Плдарить', round(age * temperature, 2), 'рублей')

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# numbers = int(input('Сколько чатлов? '))
# CR = numbers / 2200
# print('Это', CR, 'CR \nМожно купить кораблей:', int(CR * 2))
#
#

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# horizontal = float(input('По горизонтали: '))
# vertical = float(input('По вертикали: '))
#
# if horizontal < 0 or horizontal > 0.800 or vertical <0 or vertical > 0.800:
#     print('Клетки с такой координатой не существует')
# else:
#
#     print(f'Фигура находится в клеткм: {int(horizontal * 10)}, {int(vertical * 10)}')

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# horizontal = float(input('По горизонтали: '))
# vertical = float(input('По вертикали: '))
#
#
# if horizontal < 0 or horizontal > 0.800 or vertical <0 or vertical > 0.800:
#     print('Клетки с такой координатой не существует')
# else:
#
#     print(f'Фигура находится в клеткм ({int(horizontal * 10)}, {int(vertical * 10)})')
#
# x = int(horizontal * 10) + 0.5
# y = int(vertical * 10) + 0.5
# x = float(x / 10)
# y = float(y / 10)
# m = round(x - horizontal, 3)
# n = round(y - vertical, 3)
#
# print(f'Поправте положение фигуры на ({m}, {n})')


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import math
#
# a = float(input('Введите сторону a треугольника: '))
# b = float(input('Введите сторону b треугольника: '))
# c = float(input('Введите сторону c треугольника: '))
#
# s = math.sqrt((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c))
#
# print(s)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import math
#
# distance = float(input('Введите пройденное расстояние: '))
# corner = math.radians(float(input('Введите угол движения: ')))
#
# x = distance * math.cos(corner)
# y = distance * math.sin(corner)
#
# print(x, y)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import math
#
# number = float(input('Введите число: '))
#
# print(math.floor(number))
# print(math.ceil(number))
# print(math.fabs(number))
# print(math.sqrt(number))
# print(math.exp(number))
# print(math.log(number))
# print(math.log2(number))
# print(math.log10(number))
# print(math.sin(number), math.cos(number))
# if number >= 0:
#     print(math.factorial(int(number)))

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////


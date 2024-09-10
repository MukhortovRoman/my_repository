# def greeting():
#     print('Привет!')
#     print('Добро пожаловать!')
#
# while True:
#     a = input('Зайдёте? Да/Нет: ')
#     if a == 'Да':
#         greeting()
#
#     print('Следующий.\n')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def meal():
#     a = int(input())
#     b = int(input())
#     print("Всего", a+b, "шт.")
#
# print("Сколько мешков рыбы и мяса? ")
# meal()
#
# print("\nСколько буханок белого и чёрного хлеба? ")
# meal()
#
# print("\nСколько вёдер воды и молока? ")
# meal()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def mail(name):
#     print(f'\nФамилия: Иванов\nИмя: {name}\nДом: 32')
# mail('Василий')
# mail('Игорь')
# mail('Алена')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def about_water(price):
#     print('\nНазвание: КлирВотер')
#     print('Производитель: ВодЗавод')
#     print(f'Цена: {price}')
#
# about_water(25)
# about_water(30)
# about_water(40)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import math
# def square(R):
#     print('Пдощадь: ', (4 * math.pi) * R ** 2)
# def volume(R):
#     print('Объем: ', 4 / 3 * math.pi * R ** 3)
#
# R = float(input('Введите радиус планеты: '))
# square(R)
# volume(R)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def is_prime(number_total):
#     n = 0
#     number = 0
#     k = 2
#
#
#     while n < numbers_total:
#         numbers = int(input('введите число: '))
#         num = numbers // 2
#         n += 1
#         while k <= num:
#             if numbers % k == 0:
#                 break
#             k += 1
#         else:
#             number += 1
#
#     print('Количество простых чисел в последовательности: ', number)
#
# numbers_total = int(input('Введите количество чисел: '))
# is_prime(numbers_total)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def arif(a, b):
#     m = (a + b) / 2
#     print(m)
#
#
# a = int(input('Введите левую границу: '))
# b = int(input('Введите правую границу: '))
# if a < b:
#     arif(a, b)
# else:
#     print('Не верный ввод')

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def mail(surname, name, land, city, street, house, flat):
#     print('\nФамилия', surname)
#     print('Имя', name)
#     print('Страна', land)
#     print('Горрод', city)
#     print('Улица', street)
#     print('Дом', house)
#     print('Квартира', flat)
#
# for _ in range(3):
#     a = input('Фамилия: ')
#     b = input('Имя: ')
#     c = input('Страна: ')
#     d = input('Город: ')
#     n = input('Улица: ')
#     m = int(input('Номер дома: '))
#     f = int(input('Номер квартиры: '))
#     mail(a, b, c, d, n, m, f)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# import math
#
#
# def distance(x, y):
#     dist = math.sqrt(x ** 2 + y ** 2)
#     print(round(dist, 2))
#
#
# def distance2(x, y, x1, y1):
#     dist = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
#     print(round(dist, 2))
#
#
# number = int(input('1 - расстояние до точки, 2 - растояние между точками\n'))
#
# if number == 1:
#     x = float(input('Введите первую точку: '))
#     y = float(input('Введите вторую точку: '))
#     distance(x, y)
# elif number == 2:
#     x = float(input('Введите икс первой точки: '))
#     y = float(input('Введите игрек первой точки: '))
#     x1 = float(input('Введите иксвторой точки: '))
#     y1 = float(input('Введите игрек второй точки: '))
#     distance2(x, y, x1, y1)
# else:
#     print('Не верный ввод')

# //////////////////////////////////////////////////////////////////////////////////////////////////////////

# num = int(input('Введите число'))
#
# num_min = num % 10
# while num:
#     m = num % 10
#     if num_min > m:
#         num_min = m
#     num //= 10
# print(num_min)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# не верное решение!!!!!!!!!!!!!!!

# def revers(n):
#     while n:
#         num = n % 10
#         print(num, end='')
#         n //= 10
#
#
# numders = int(input('Введите число: '))
# if numders == 0:
#     print('Программа завершена!')
#
# revers(numders)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////


# def rev(number):
#     num = 0
#     while number:
#         digit = number % 10
#         number //= 10
#         num *= 10
#         num += digit
#     print(num)
#
# number = int(input('Введите число: '))
# rev(number)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def count_letters(text, digit, letter):
#     count_letter = 0
#     count_number = 0
#     for liter in text:
#         if liter == digit:
#             count_number += 1
#         elif liter == letter:
#             count_letter += 1
#     print(f'\nКоличество цифр {digit}: {count_number}')
#     print(f'Количество букы {letter}: {count_letter}')
#
#
# text = input('\nВведите текст: ')
# digit = input('Какую цифру ищем? ')
# letter = input('Какую букву ищем? ')
# count_letters(text.lower(), digit, letter.lower())

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# import random
#
# print('\n*** Игра камень, ножницы, бумага ***')
# game = int(input('\nВведите: 1 - "Камень", 2 - "Ножницы", 3 - "Бумага"  '))
#
# pc = random.randint(1, 3)
#
# if game == 1 and pc == 2:
#     print('Выиграл! камень бьет ножницы')
# elif game == 2 and pc == 3:
#     print('Выиграл! ножницы режут бумагу')
# elif game == 3 and pc == 1:
#     print('Выиграл! бумага кроет камень')
# elif game == pc:
#     print('Ничья')
# else:
#     print('Проиграл')

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def rock_paper_scissors():
#     import random
#
#     print('\n*** Игра камень, ножницы, бумага ***')
#     game = int(input('\nВведите: 1 - "Камень", 2 - "Ножницы", 3 - "Бумага"  '))
#
#     pc = random.randint(1, 3)
#
#     if game == 1 and pc == 2:
#         print('Выиграл! камень бьет ножницы')
#     elif game == 2 and pc == 3:
#         print('Выиграл! ножницы режут бумагу')
#     elif game == 3 and pc == 1:
#         print('Выиграл! бумага кроет камень')
#     elif game == pc:
#         print('Ничья')
#     else:
#         print('Проиграл')
#         main_menu()
#

def guess_the_number():
    import random

    print('\n*** Игра "Угадай число ***')

    score = 1
    score2 = 1

    numbers = int(input("\nВведите число: "))
    while True:
        num = random.randint(1, 10)
        if numbers == num:

            print("Угадали!!!")
            print(score2, "совпадение", "из", score)
            score2 += 1
            break
        else:
            score += 1
            print("Не угадали, правильный ответ", num)
            numbers = int(input("\nВведите следующее число: "))
            main_menu()


def main_menu():
    game = int(input('\nВыберите игру: 1 - камень, ножницы, бумага. 2 - угадай число '))
    if game == 1:
        rock_paper_scissors()
    elif game == 2:
        guess_the_number()


main_menu()

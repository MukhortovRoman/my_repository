# def summa_n(n):
#     num = 0
#     for _ in range(1, n + 1):
#         num += _
#     print(f'Я знаю, что сумма чисел от 1 до {numbers} равна {num}')
#
#
# numbers = int(input('Введите число: '))
# summa_n(numbers)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# def positive():
#     print('Положительное')
#
#
# def negative():
#     print('Отрицательное')
#
#
# def test():
#     number = int(input('Введите целое число: '))
#     if number >= 0:
#         positive()
#     else:
#         negative()
#
#
# test()

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# def summ(num):
#     total_num = 0
#     while num:
#         m = num % 10
#         total_num += m
#         num //= 10
#
#     print(f'\nСумма цифр равна: {total_num}')


# def maximum(num):
#     num_max = 0
#     while num:
#         m = num % 10
#         if num_max < m:
#             num_max = m
#         num //= 10
#
#     print(f'\nМаксимальная цифра {num_max}')
#
#
# def minimum(num):
#     num_min = num % 10
#     while num:
#         m = num % 10
#         if num_min > m:
#             num_min = m
#         num //= 10
#
#     print(f'\nМинимальная цифра {num_min}')
#
#
# while True:
#     numbers = int(input('\nВведите число: '))
#     print('\nВыберите действие: ')
#     operation = int(input('1 - вывести сумму цифр, 2 - максимальная цифра, 3 - минимальная цифра: '))
#
#     if operation == 1:
#         summ(numbers)
#     elif operation == 2:
#         maximum(numbers)
#     elif operation == 3:
#         minimum(numbers)
#     else:
#         print('Не верный ввод')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////


# def rev(number):
#     num = 0
#     while number:
#         digit = number % 10
#         number //= 10
#         num *= 10
#         num += digit
#     print(f'Число наоборот: {num}')
#
#
# number = int(input('\nВведите число: '))
# rev(number)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

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
# import math
#
#
# def divider(num_1, num_2):
#     divider = math.gcd(num_1, num_2)
#     print(f'\nНаибольший делитель равен: {divider}')
#
#
# num_1 = int(input('\nВведите первое число: '))
# num_2 = int(input('Введите второе число: '))
# divider(num_1, num_2)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////



def rock_paper_scissors():
    import random

    print('\n*** Игра камень, ножницы, бумага ***')
    game = int(input('\nВведите: 1 - "Камень", 2 - "Ножницы", 3 - "Бумага"  '))

    pc = random.randint(1, 3)

    if game == 1 and pc == 2:
        print('Выиграл! камень бьет ножницы')
    elif game == 2 and pc == 3:
        print('Выиграл! ножницы режут бумагу')
    elif game == 3 and pc == 1:
        print('Выиграл! бумага кроет камень')
    elif game == pc:
        print('Ничья')
    else:
        print('Проиграл')
        main_menu()


# def guess_the_number():
#     import random
#
#     print('\n*** Игра "Угадай число ***')
#
#     score = 1
#     score2 = 1
#
#     numbers = int(input("\nВведите число: "))
#     while True:
#         num = random.randint(1, 10)
#         if numbers == num:
#
#             print("Угадали!!!")
#             print(score2, "совпадение", "из", score)
#             score2 += 1
#             break
#         else:
#             score += 1
#             print("Не угадали, правильный ответ", num)
#             numbers = int(input("\nВведите следующее число: "))
#             main_menu()
#
#
# def main_menu():
#     game = int(input('\nВыберите игру: 1 - камень, ножницы, бумага. 2 - угадай число '))
#     if game == 1:
#         rock_paper_scissors()
#     elif game == 2:
#         guess_the_number()
#
#
# main_menu()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# def summ(number):
#     total = 0
#     for i in range(1, number + 1):
#         total += i
#     print(f'Сумма от 1 до {number} = {total}')
#     return total
#
#
# number = int(input('Введите число: '))
# summ2 = summ(number)
# summ(summ2)
#
# # //////////////////////////////////////////////////////////////////////////////////////////////////////////

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

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def number_count(number):
#     if number < 0:
#         print('Число отрицательное')
#         return 0
#     count = 0
#     while number > 0:
#         number //= 10
#         count += 1
#     return count
#
#
# def number_1():
#     num30 = 0
#     max_ = 0
#     m = 0
#     task = int(input('ВВедите кол-во задач: '))
#     i = 0
#     max_count = 0
#     while task > i:
#         i += 1
#         number = int(input(f'Введите {i} число: '))
#         num10 = number_count(number)
#         if m < num10:
#             m = num10
#             max_ = m
#             num30 = number
#     print('Первая задача на обработку: ', num30)
#

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# x = 1
# count = 0
# while x != 0:
#     x /= 2
#     count += 1
#     print(x)
# print('Кол-во делений:', count)

# ////////////////////////////////////////////////////////////////////////////////////////

# start_number = float(input("Введите число: "))
# count = 0
# while start_number > 10:
#     count += 1
#     start_number /= 10
#
# print(f"Формат плавающей точки: x = {start_number} * 10 ** {count}")

# ///////////////////////////////////////////////////////////////////////////////////////


# a = 1e-3
# x = 1
# count = 0
# while x < 2:
#     x += a
#     count += 1
# print('Кол-во прибавлений:',count)

# ///////////////////////////////////////////////////////////////////////////////////////

# num = 92345
# count = 0
# while num > 10:
#     num /= 10
#     count += 1
# print('Формат плавающей точки:', num, '* 10 **', count)

# ///////////////////////////////////////////////////////////////////////////////////

# import math
#
#
# def check_exponent_change(tax, new_tax):
#     total = tax + new_tax
#     degree_e_tax = math.floor(math.log10(tax))
#     degree_e_total = math.floor(math.log10(total))
#     if degree_e_tax != degree_e_total:
#         return True
#     else:
#         return False
#
#
# country_budget = float(input('Введите бюджет страны: '))
# budget_receipts = float(input('Введите новые поступления (налог): '))
# is_increase = check_exponent_change(country_budget, budget_receipts)
#
# if is_increase:
#     print('Бюджет увеличится')
# else:
#     print('Бюджет не изменится')

# /////////////////////////////////////////////////////////////////////////////////////

# def eqv(num_1, num_2, num_3):
#     return abs((num_1 + num_2) - num_3) <= 1e-15
#
#
# num_1 = float(input('Введите первое число: '))
# num_2 = float(input('Введите второе число: '))
# num_3 = float(input('Введите третье число: '))
#
# print(eqv(num_1, num_2, num_3))

# ////////////////////////////////////////////////////////////////////////////////////

# import math
#
# precision = float(input('Точность: '))
#
# result = 0
# i = 0
# add_Member = 1
#
# while add_Member > precision:
#     add_Member = 1 / math.factorial(i)
#     result += add_Member
#     i += 1
#
# print('Результат: ', result)
# print('Константа', math.e)

# ////////////////////////////////////////////////////////////////////////
# from decimal import Decimal
#
#
# print(Decimal(1.1) + Decimal(1.1) + Decimal(1.1) +d Decimal(3.3))

# ///////////////////////////////////////////////////////////////////////////

first_n = int(input("Введите первое число: "))

first_num_count = 0
temp = first_n

while temp > 0:
    first_num_count += 1
    temp = temp // 10
if first_num_count < 3:
 print("В первом числе меньше трёх цифр.")
else:
 last_digit = first_n % 10
 first_digit = first_n // 10 ** (first_num_count - 1)
 between_digits = first_n % 10 ** (first_num_count - 1) // 10
 first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
 print('Изменённое первое число:', first_n)

 second_n = int(input("\nВведите второе число: "))

 second_num_count = 0
 temp = second_n
 while temp > 0:
   second_num_count += 1
   temp = temp // 10

 if second_num_count < 4:
   print("Во втором числе меньше четырёх цифр.")
 else:
   last_digit = second_n % 10
   first_digit = second_n // 10 ** (second_num_count - 1)
   between_digits = second_n % 10 ** (second_num_count - 1) // 10
   second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit

   print('Изменённое второе число:', second_n)

   print('\nСумма чисел:', first_n + second_n)
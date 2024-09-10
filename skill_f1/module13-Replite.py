# def point(numbers):
#     count = 0
#     while numbers < 1:
#         numbers *= 10
#         count += 1
#     print('Формат плавающей точки: x =', round(numbers, 1), '* 10 **', count * -1)
#
#
# def point_1(numbers):
#     count = 0
#     while numbers > 10:
#         numbers /= 10
#         count += 1
#     print('Формат плавающей точки: x =', numbers, '* 10 **', count * 1)
#
#
# def point_2(numbers):
#     count = 0
#     while 1 <= numbers < 10:
#         numbers /= 10
#         count += 1
#     print('Формат плавающей точки: x =', numbers, '* 10 **', count * 1)
#
#
# def main():
#     numbers = float(input('Введите число: '))
#     if 0 < numbers < 1:
#         point(numbers)
#     elif numbers >= 10:
#         point_1(numbers)
#     elif 1 <= numbers < 10:
#         point_2(numbers)
#     else:
#         print('Введите число больше нуля')
#
#
# if __name__ == '__main__':
#     main()
#

# /////////////////////////////////////////////////////////////////////////////////
# def maximum_of_two(num_1, num_2):
#     return max(num_1, num_2)
#
#
# def maximum_of_three(x, num_3):
#     print(max(x, num_3))
#
#
# def main():
#     num_1 = int(input('Введите первое число: '))
#     num_2 = int(input('Введите второе число: '))
#     num_3 = int(input('Введите третье число: '))
#
#     x = maximum_of_two(num_1, num_2)
#     maximum_of_three(x, num_3)
#
#
# if __name__ == '__main__':
#     main()

# ///////////////////////////////////////////////////////////////////////////////////
# def rev(num_1, num_2):
#     num_1 = num_1[::-1]
#     num_2 = num_2[::-1]
#     summ = int(num_1) + int(num_2)
#     print(f'\nПервое число наоборот: {num_1}')
#     print(f'Второе число наоборот: {num_2}')
#     print('Сумма:', summ)
#     x = str(summ)
#     x = x[::-1]
#     print('\nСумма наоборот:', x)
#
#
# def main():
#     num_1 = input('Введите первое число: ')
#     num_2 = input('Введите второе число: ')
#     rev(num_1, num_2)
#
#
# if __name__ == '__main__':
#     main()

# ///////////////////////////////////////////////////////////////////////////////////////

# def first_num_count(first):
#     first_num_count = 0
#     temp = first
#     while temp > 0:
#         first_num_count += 1
#         temp = temp // 10
#
#     return first_num_count
#
#
# def change_number(num, digit):
#     num_1 = first_num_count(num)
#     last_digit = num % 10
#     first_digit = num // 10 ** (num_1 - 1)
#     between_digits = num % 10 ** (num_1 - 1) // 10
#     first_s = last_digit * 10 ** (num_1 - 1) + between_digits * 10 + first_digit
#
#     return first_s
#
#
# def main():
#     first_n = int(input("\nВведите первое число: "))
#     while first_n < 100:
#         print('В первом числе меньше трех цифр.')
#         first_n = int(input("Введите первое число: "))
#     change_number(first_n, 'первое')
#     print('Изменное число:', change_number(first_n, ''))
#
#     first_m = int(input("\nВведите второе число: "))
#     while first_m < 1000:
#         print('В втором числе меньше четырех цифр')
#         first_m = int(input("Введите второе число: "))
#     change_number(first_m, 'второе')
#     print('Изменное число:', change_number(first_m, ''))
#
#     print('\nСумма чисел:', change_number(first_n, '') + change_number(first_m, ''))
#
#
# if __name__ == '__main__':
#     main()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def calculate_vibrations(initial_amplitude, stop_amplitude):
#     vibrations = 0
#     amplitude = initial_amplitude
#     while amplitude > stop_amplitude:
#         amplitude *= 0.916
#         vibrations += 1
#     return vibrations
#
# def main():
#     initial_amplitude = float(input("Введите начальную амплитуду: "))
#     stop_amplitude = float(input("Введите амплитуду остановки: "))
#     vibrations = calculate_vibrations(initial_amplitude, stop_amplitude)
#     print(f"Маятник считается остановившимся через {vibrations} колебаний")
#
# main()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def D(x):
#     return x ** 3 - 3 * x ** 2 - 12 * x + 10
#
#
# d = float(input('Введите максимально допустимый уровень опасности: '))
# while d < 0:
#     print('Введите положительное число: ')
#     d = float(input())
#
# l = 0
# r = 4
# d_min = d
# x_min = 4
# while True:
#     x = (l + r) / 2
#     if D(x) < -d:
#         r = x
#     elif D(x) > d:
#         l = x
#     elif r - l < 0.00000001:
#         break
#     else:
#         l = x
#         if abs(D(x)) < abs(d_min):
#             x_min = x
#             d_min = D(x)
#
# print('Приблизительная глубина безопасной кладки ', x_min, 'м')




# //////////////////////////////////////////////////////////////////////////////////////////////////////////

max_of_two(max_of_two(a, b), c)
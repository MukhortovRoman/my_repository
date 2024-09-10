# for i in range(6):
#     for j in range(12):
#         if j % 2 == 0:
#             print(j + i, end='\t')
#     print()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////

# num = int(input('Введите лестницы: '))
# for i in range(num + 1):
#     for j in range(num + 1):
#         if i > j:
#             print(i, end=' ')
#     print()


# //////////////////////////////////////////////////////////////////////////////////////////////////////////

# size = int(input('Введите высоту рамки: '))
# size2 = int(input('введите ширину рамки: '))
#
# for i in range(size):
#     for j in range(size):
#         if i == 0:
#             print('-', end='')
#         elif j < 1:
#             print('|', end='')
#         elif j == size - 1:
#             print('|', end='')
#         elif i > size:
#             print('-', end='')
#         else:
#             print(' ', end='')
#
#     print()
# print('-' * size2, end='')

# /////////////////////////////////////////////////////////////////////////////////////////////////////////


# n = 0
# number = 0
# k = 2
# numbers_total = int(input('Введите количество чисел: '))
#
# while n < numbers_total:
#     numbers = int(input('введите число: '))
#     num = numbers // 2
#     n += 1
#     while k <= num:
#         if numbers % k == 0:
#             break
#         k += 1
#     else:
#         number += 1
#
# print('Количество простых чисел в последовательности: ', number)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# number = 0
# summ = 0
# summ_total = 0
# big_numbers = 0
# m = 0
# numbers_total = int(input('Введите кол-во чисел: '))
#
# while m < numbers_total:
#     N = int(input('Введите натуральное число: '))
#     number = N
#     m += 1
#
#     while N != 0:
#         summ += N % 10
#         N = N // 10
#
#     if summ > summ_total:
#         summ_total = summ
#
#         big_number = number
#     summ = 0
#
# print('Число', big_number, 'имеет максимальную сумму: ', summ_total)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////

# size = int(input('Введите высоту пирамиды: '))
#
# for row in range(size, 0, -1):
#     for col in range(size + 2):
#         if row < col:
#             print('#', end=' ')
#         else:
#             print('', end=' ')
#     print()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# size = int(input('Введите высоту пирамиды: '))
# score = size
#
# for row in range(size + 1):
#     for col in range(size + 1):
#         if row == col:
#             print(' ' * score, '#' * (row * 2 - 1))
#             score -= 1

# правильный код
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Разобраться!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# n = int(input('Введите высоту пирамиды: '))
# number = 1
# for row in range(1, n + 1):
#     print('\t' * (n - row), end='')
#     for coi in range(row):
#         print(number, end='')
#         number += 2
#         print('\t' * 2, end='')
#     print()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////


# rows = int(input('Введите кол-во ступенек: '))
# new_num = 1
# for line in range(rows):
#     space_count = rows - line - 1
#     print('   ' * space_count, end='')
#     for number in range(line + 1):
#         print(new_num, end='    ')
#         new_num += 2
#     print()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


# depth = int(input('Введите глубину ямы:'))
# for line in range(depth):
#     for left_number in range(depth, depth - line - 1, -1):
#         print(left_number, end='')
#     point_count = 2 * (depth - line - 1)
#     print('.' * point_count, end='')
#     for right_number in range(depth - line, depth + 1):
#         print(right_number, end='')
#     print()

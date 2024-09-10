# for a in range(1, 10):
#     for b in range(1, 10):
#         print(a * b, end='\t')
#     print()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# N = int(input('Введите число: '))
# for i in range(0, N + 1):
#     for m in range(0, N + 1):
#         print(i + m, end=' ')
#     print()
# #
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

# for a in range(10):
#     for b in range(10):
#         print(a - b, end='\t')
#     print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# size = int(input('Введите размер матрицы: '))
# for i in range(1, size + 1):
#     for j in range(1, size + 1):
#         if i % 2 == 0:
#             print(i, end=' ')
#         else:
#             print(j, end=' ')
#     print()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print('-', end='')
#         elif col == 24:
#             print('|', end='')
#         else:
#             print(' ', end='')
#     print()

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# size = int(input('Введите размер матрицы: '))
# for i in range(1, size + 1):
#     for j in range(1, size + 1):
#         if j % 3 == 0:
#             print(j, end=' ')
#         else:
#             print(i, end=' ')
#     print()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# for i in range(20):
#     for j in range(50):
#         if j == 24:
#             print('|', end='')
#         elif i == 9:
#             print('-', end='')
#         else:
#             print(' ', end='')
#     print()

# /////////////////////////////////////////////////////////////////////////////////////////////////////////
# for i in range(1, 31):
#     for j in range(1, 21):
#         if j == 1:
#             print('-', end='')
#
#

# /////////////////////////////////////////////////////////////////////////////////////////////////////////

#
# size = int(input('Введите размер матрицы: '))
# for row in range(size):
#     for col in range(size):
#         if row < col:
#             print(0, end=' ')
#         elif row > col:
#             print(2, end=' ')
#         else:
#             print(1, end=' ')
#     print()
#

# ////////////////////////////////////////////////////////////////////////////////////////////////////////


# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print('-', end='')
#         elif col == row + 29:
#             print('\\', end='')
#         elif col == -row + 19:
#             print('/', end='')
#         elif col == 24:
#             print('|', end='')
#         else:
#             print(' ', end='')
#     print()

# /////////////////////////////////////////////////////////////////////////////////////////////////////////

# size = int(20)
# for i in range(size):
#     for j in range(size):
#         if i == 0:
#             print('-', end='')
#         elif j < 1:
#             print('|', end='')
#         elif j == 19:
#             print('|', end='')
#         elif i == 19:
#             print('-', end='')
#         else:
#             print(' ', end='')
#     print()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print('-', end='')
#         elif col == row + 29:
#             print('\\', end='')
#         elif col == -row + 19:
#             print('/', end='')
#         elif col == 24:
#             print('|', end='')
#         else:
#             print(' ', end='')
#     print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# size = int(input('Введите размер матрицы: '))
# for row in range(size):
#     for col in range(size):
#         if row > col:
#             print(0, end=' ')
#         elif row < col:
#             print(2, end=' ')
#         else:
#             print(1, end=' ')
#     print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# people = int(input('Введите кол-во людей: '))
# for hour in range(people + 1):
#     print('идет час:', hour)
#     for num in range(hour, people):
#         print('Номер в очереди:', num)
#     print()
# print('Очередь обслужена!')

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# seq_num = int(input('Сколько будет чисел: '))
# numeral = int(input('какую цифру считать: '))
# while numeral < 0 or numeral > 9:
#     numeral = int(input('Цифра должна быть в диапазоне от 0 до 9! Введите новую цифру: '))
# numeral_count = 0
# for num in range(seq_num):
#     print('Введите', num, '-e число: ')
#     number = int(input())
#     while number > 0:
#         if number % 10 == numeral:
#             numeral_count += 1
#         number //= 10
# print('Цифр', numeral, 'в последовательности:', numeral_count)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////


# seq_num = int(input('Сколько будет чисел: '))
# number_count = 0
# for num in range(seq_num):
#     numbers = int(input('Введите число: '))
#     while numbers > 0:
#         if numbers % 10 > 5:
#             number_count += 1
#         numbers //= 10
# print(number_count)
#
#

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////


# for i in range(6):
#     for j in range(i, 6):
#         print(j, end='\t')
#     print()


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# num = 5
# for i in range(num + 1):
#     print('час', i)
#     for j in range(i, num + 1):
#         print(j, end='\n')
#     print()
# print('очередь обслужена')

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
















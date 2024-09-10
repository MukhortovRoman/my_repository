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
# def number_start():
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
#
# number_start()

# ///////////////////////////////////////////////////////////////////////////////////////

# x = 1
# count = 0
# while x != 0:
#     x /= 2
#     count += 1
#     print(x)
# print('Кол-во делений:', count)

# ///////////////////////////////////////////////////////////////////////////////////////

# start_number = float(input("Введите число: "))
# count = 0
# while start_number > 10:
#     count += 1
#     start_number /= 10
#
# print(f"Формат плавающей точки: x = {start_number} * 10 ** {count}")

# ///////////////////////////////////////////////////////////////////////////////////////


# a = int(1e-3)
# x = 1
# count = 0
# while a < 2:
#     a += x
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


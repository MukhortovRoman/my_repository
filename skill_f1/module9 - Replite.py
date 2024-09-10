# score = 0
# for word in range(1, 11):
#     user = input('Введите слово: ')
#     if user == 'карамба' or user == 'Карамба':
#         # if user.lower() == 'карамба':
#         score += 1
#         print('Вы приняты на борт')
# print('Принято на борт', score, 'человек')

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# score = 0
# text = input('\nВведите текст: ')
#
# for symbol in text:
#     score += 1
#     if symbol == '*':
#         break
# print('Символ «*» стоит на позиции', score)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

# row = int(input('\nВведите кол-во рядов: '))
# seat = int(input('Введите кол-во сидений в ряде: '))
# space = int(input('Введите кол-во метров между рядами: '))
# print('\nСцена\n')
#
# symbol = '=' * seat + ' ' + '*' * space + ' ' + '=' * seat
# for lot in range(row):
#     print(symbol, end='\n')

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

# horizon = 8
# vertical = 10
#
# while True:
#     rover = input(f'Марсоход находится на позиции {horizon}, {vertical}, введите команду: ')
#     if rover == 'D' and horizon != 15:
#         horizon += 1
#     elif rover == 'A' and horizon != 1:
#         horizon -= 1
#     elif rover == 'W' and vertical != 20:
#         vertical += 1
#     elif rover == 'S' and vertical != 1:
#         vertical -= 1

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# score = 0
# max_text = 0
# text = input('Введите текст: ')
#
# for symbol in text:
#     if symbol != ' ':
#         score += 1
#     else:
#         score = 0
#     if score > max_text:
#         max_text = score
#
# print(f'Самое длинное слово, букв: {max_text}.')

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# score = 0
# total_score = 0
#
# text = input('Введите стойла ')
# for stall in text:
#     score += 1
#     if stall == 'b':
#         total_score += score
#
# print('За день произведено молока:', total_score * 2, 'литров')

# //////////////////////////////////////////////////////////////////////////////////////////////////////////

# milk = 0
# total_milk = 0
# score = 0
#
# for i in range(1, 11):
#     score += 1
#     text = input(f'введите стойло {score}: ')
#     for symbol in text:
#         milk += 1
#         if symbol == 'b':
#             total_milk += milk
#         else:
#             continue
#
# print('За день произведено молока:', total_milk * 2, 'литров')

# //////////////////////////////////////////////////////////////////////////////////////////////////////

# score = 0
# text_even = ''
# text_not_even = ''
# text = 'shacnidw'
#
# for i in text:
#     score += 1
#     if score % 2 != 0:
#         text_not_even += i
#     elif score % 2 == 0:
#         text_even = i + text_even
#
# print(text_not_even + text_even)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////

# text_1 = ''
# text = input('Введите слово: ')
#
# for symbol in text:
#     text_1 = symbol + text_1
# if text == text_1:
#     print('Да, это палиндром!')
# else:
#     print('Нет, это не палиндром!')

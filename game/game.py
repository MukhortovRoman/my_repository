
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


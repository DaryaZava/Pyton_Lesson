# Задача 10:
#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно
# перевернуть.

# import random
# number_coins = int(input("Введите количество монет: "))
# side_1_count = 0
# side_0_count = 0
# for i in range(number_coins):
#     side = random.randint(0, 1)
#     print(f'side of {i + 1} coin = {side}')
#     if side == 1:
#         side_1_count += 1
#     else:
#         side_0_count += 1
# if side_1_count < side_0_count:
#     print(f'Минимальное количчество переворотов = {side_1_count}')
# else:
#     print(f'Минимальное количество переворотов = {side_0_count}')

#     2. Задача 12
#  Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

# sum = int(input('Введите сумму чисел: '))
# prod = int(input('Введите произведение чисел: '))
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if sum == i + j and prod == i * j:
#             x, y = i, j
# print(f'X = {x}, Y = {y}')

# Задача 14: Требуется вывести все целые степени двойки(т.е. числа
#  вида 2k), не превосходящие числа N.

num = int(input('Введите число: '))
prod = 0
degree = 0
while prod * 2 < num:
    prod = 2 ** degree
    print(prod, end=' ')
    degree += 1
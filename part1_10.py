print('Задача 1. Тестовое задание')

# Степан пришёл устраиваться на работу, где ему дали тестовое задание:
# проанализировать такую таблицу,
# понять как она строится и написать программу для вывода её на экран.

# 0 2 4 6  8  10
# 1 3 5 7  9  11
# 2 4 6 8  10 12
# 3 5 7 9  11 13
# 4 6 8 10 12 14
# 5 7 9 11 13 15
#
# Помогите Степану реализовать такую программу.
# Подсказка: номера столбцов. А ещё не забудьте про литерал \t для табуляции


# for row in range(6):
#     for col in range(0, 12, 2):
#         print(row + col, end='\t')
#
#     print()

# -----------------------------------------------------------------------

print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# user_number = int(input('Введите число: '))
#
# for row in range(1, user_number + 1):
#     for col in range(row):
#         print(row, end='\t')
#
#     print()

# -----------------------------------------------------------------------

print('Задача 3. Рамка')

# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|

# width = int(input('Введите ширину: '))
# height = int(input('Введите высоту: '))
#
# for row in range(width + 1):
#     for col in range(height + 1):
#         if row == 0:
#             print('-', end='')
#         elif col == 0:
#             print('|', end='')
#         elif col == height:
#             print('|', end='')
#         elif row == width:
#             print('-', end='')
#         else:
#             print(' ', end='')
#     print()


# -----------------------------------------------------------------------

print('Задача 4. Простые числа')

# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.

# Простое число делится только на себя и на единицу. Последовательность задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна итерация — одно число.

# Пример:
# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.

# Количество простых чисел в последовательности: 4.

# ------------------------------- list -------------

# simple = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
#           71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
#           151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
#           241, 251, 257, 263, 269, 271, 277, 281]
#
# seqnum = int(input('Введите количество чисел: '))
# count = 0
# for n in range(seqnum):
#     number = int(input('Введите число: '))
#     for num in simple:
#         if number == num:
#             count += 1
# print(f'Количество простых чисел в последовательности: {count}')

# --------------

# seqnum = int(input('Введите количество чисел: '))
#
# count_simple = 0
# for n in range(seqnum):
#     count = 0
#
#     number = int(input(f'Введите {n+1} число: '))
#     for num in range(2, number // 2+1):
#         if number % num == 0:
#             count += 1
#     if count <= 0:
#         count_simple += 1
#
# print(f'Количество простых чисел в последовательности: {count_simple}')

# -----------------------------------------------------------------------

print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

# # начал решать через список, получилось давольно запутанно но работает
# number_list = []
# full_number = []
# seq = int(input('Сколько чисел ? '))
# for n in range(1, seq):
#     count = 0
#     user_number = str(input(f'Введите {n} число: '))
#     full_number.append(int(user_number))
#     for num in user_number:
#         count += int(num)
#     number_list.append(count)
#
# print(number_list)
# print(full_number)
# max_index = number_list.index(max(number_list))
# print(f'наибольшее число -  {full_number[max_index]} сумма его цифр - {max(number_list)}')


# -----------------------------------------------------------------------

print('Задача 6. Пирамидка')

# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

#
###
#####
#######

# дмитрий в целом вложенные циклы даются очень тяжело.
# не получается у меня построить эту пирамиду. Видел много решений этой задачи. Но как они работают мне не понятно.
# # а тупо переписывать чужой код не хочу, можете мне как то обяснить как это решать ?

# !!!!!!!!!!!!!!!!!!! Запомнить!!!!!!!!!!!!!!!!
# height = int(input('Введите высоту: '))

# for line in range(height):
#     for space in range(height - line, 0, -1):
#         print(end='\t')
#     for col in range(line + 1):
#         print('#', end='\t')
#         print('', end='\t')
#     print()
#

# -----------------------------------------------------------------------

print('Задача 7. Пирамидка 2')

# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

# !!!!!!!!!!!!!!!!!!! Запомнить!!!!!!!!!!!!!!!!

# height = int(input('Введите высоту: '))
# number = 1
# for row in range(height):
#     for space in range(height - row, 0, -1):
#         print(end='')
#     print('\t' * (height - row), end='')
#     for col in range(row + 1):
#         print(number, end='')
#         number += 2
#         print('\t' * 2, end='')
#
#     print()
# -----------------------------------------------------------------------

print('Задача 8. Яма ')

# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:

# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

# depth = 8#int(input('Введите глубину ямы: '))
#
# for row in range(depth):
#     for left_number in range(depth, depth - row - 1, -1):
#         print(left_number, end='')
#
#     point = 2 * (depth - row - 1)
#     print('.' * point, end='')
#
#     for right_number in range(depth - row, depth + 1):
#         print(right_number, end='')
#
#     print()

# -----------------------------------------------------------------------

# print('Задача 1. Кубы чисел')
import random

# В один из вечеров к Васе домой пришёл племянник и пожаловался на сложности с уроками математики: у него никак не получалось разобраться со степенями чисел. Вася решил помочь племяннику и написать программу, которая позволит наглядно увидеть возведение чисел в третью степень.

# Напишите программу, которая возводит в третью степень каждое число от 1 до N и выводит результат на экран.

# degree = int(input('Введите число: '))
# count = 0
# while count < degree:
#     count += 1
#     print(f'число {count} в третьей степени {count **3}')
#------------------------
# print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор,
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.

# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50

# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.

# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!

# name = input('Имя должника: ')
# debt = int(input('Сумма долга: '))
# print(f'{name} ваша задолженность составляет {debt} рублей')
# while True:
#     money = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?'))
#     if debt <= money:
#         break
#     print(f'Маловато, {name}. Давайте ещё раз.')
# print(f'Отлично, {name}! Вы погасили долг. Спасибо!')

#----------------------------------
# print('Задача 3. Слишком большие числа')

# У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие большие счета, что числа не помещаются на бумаге.

# Напишите программу, которая считала бы для него, сколько цифр во вводимом числе. Обратите внимание, что число 0 имеет одну цифру.

# Пример:
# Введите число: 567
# Ответ: 3

# Введите число: 1203
# Ответ: 4

# Решение через функцию len
# number = int(input('Введите число: '))
# print(f'Ответ: {len(str(number))}')
#
# #  Решение через цикл for
# sign = 0
# for n in str(number):
#     sign += 1
# print(f'Ответ: {sign}')
#
# # Решение через цикл while, самый не очевидный вариант
# count = 0
# while number > 0:
#     number //= 10
#     count += 1
# print(f'Ответ: {count}')

#--------------------------------------------
# print('Задача 4. Поставьте оценку!')

# Вася выложил своё новое приложение на платформу для начинающих разработчиков,
# на ней пользователи могут ставить оценку приложению от −100 до 100.
# Ему захотелось сравнить количество положительных и отрицательных отзывов,
# для этого он заранее отфильтровал все отзывы так,
# чтобы в конце были те, которые равны нулю.

# Напишите программу,
# которая находит количество положительных
# и количество отрицательных чисел в последовательности.
# Последовательность заканчивается на числе 0.

# Пример:
# Введите число: −4
# Введите число: −90
# Введите число: 6
# Введите число: 0
# Кол-во положительных чисел: 1
# Кол-во отрицательных чисел: 2

# #По условиям задачи не доконца понятно как это должно работать
# positive = 0
# negative = 0

# while True:
#     number = int(input('Введите число: '))
#     if number < 0:
#         negative += 1
#     elif number == 0:
#         break
#     else:
#         positive += 1
# print(f'Кол-во положительных чисел: {positive}')
# print(f'Кол-во отрицательных чисел: {negative}')

# Второй способ рабочий
# positive2 = 0
# negative2 = 0
# number2 = []
# while True:
#     dig = int(input('Введите число: '))
#     number2.append(dig)
#     if len(number2) == 4:
#         break
#
# for n in number2:
#     if n < 0:
#         negative2 += 1
#     else:
#         positive2 += 1
# print(f'Кол-во положительных чисел: {positive2}')
# print(f'Кол-во отрицательных чисел: {negative2}')
#-----------------------------------
# print('Задача 5. Обычный день на работе')

# Максим программирует целый день на работе и вечером идёт домой.
# Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа.
# И вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.

# Напишите программу,
# в которой считается, сколько задач выполнил Максим за день (8 часов).
# Если он хоть раз взял трубку,
# то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».

# Пример:
# Начался 8-часовой рабочий день
# 1 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 2 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 3 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 4 час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? (1-да, 0-нет) 1

# 5 час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 6 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 7 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1-да, 0-нет) 1

# 8 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин

# print('Начался восьмичасовой рабочий день.')
# count_hour = 1
# count_task = 0
# phone = 0
# while count_hour != 9:
#     # считаем задачи
#     print(f'{count_hour}-й час')
#     number_tasks = int(input('Сколько задач решит Максим?: '))
#     count_task = count_task + number_tasks
#
#     # звонок жены
#     call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет):"))
#     if call == 1:
#         phone = phone + call
#
#     count_hour += 1
#
# print(f'Рабочий день закончился. Всего выполнено задач: {count_task}, ответил на звонок {phone} раз')
# if phone > 0:
#     print("Нужно зайти в магазин.")

# while True:
#     # считаем задачи
#     print(f'{count}-й час')
#     number_tasks = int(input('Сколько задач решит Максим?: '))
#     task = task + number_tasks
#
#     # звонок жены
#     p = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет):"))
#     if p == 1:
#         phone = phone + p
#
#     count += 1
#     if count == 8:
#         break

# print(f'Рабочий день закончился. Всего выполнено задач: {task}, звоноков {phone}')
# if phone > 0:
#     print("Нужно зайти в магазин.")
#-----------------------------------
# print('Задача 6. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

# bank = int(input("Денег в банке:"))
# user_percent = int(input("увеличить вклад на процент в год:"))
# desired_result = int(input("желаемый результат:"))
# year = 0
# # percent = bank / 100 * user_percent
# while desired_result > bank:
#
#     bank = int(bank * (1 + user_percent / 100))
#     year += 1
#
# print(f'Через {year} лет сумма на вкладе достигнет значения {bank} рублей')

#-----------------------------------
# print('Задача 7. Игра «Угадай число»')

# В одной из практических работ мы делали задачу, где папа-программист написал для сына программу, которая просит его угадать число. Недостаток программы был в том, что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число. Теперь, когда мы знаем гораздо больше, пришло время исправить этот недостаток и заодно немного улучшить саму игру.

# Напишите программу-игру, которая запрашивает у пользователя число до тех пор, пока он его не отгадает. Выводите сообщения в соответствии с примером.

# Пример (загадали число 7)
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4

# number = random.choice(range(1, 11))
# print(number)
# count = 0
# while True:
#     user_number = int(input('Введите число: '))
#     count += 1
#     if user_number == number:
#         print(f"Вы угадали! Число попыток: {count}")
#         break
#     elif user_number < number:
#         print('Число меньше, чем нужно. Попробуйте ещё раз!')
#     else:
#         print('Число больше, чем нужно. Попробуйте ещё раз!')

#-----------------------------------
# print('Задача 8. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# Подсказка: используйте бинарный поиск, а не конкатенацию.

secret_number = int(input('Введите число от 1 до 100: '))
minimum = 1
maximum = 100
chose = 0
while True:
    guess = int(minimum + maximum) // 2
    chose = int(input(f'Если загаданное число это {guess} введите 1, если больше 2,'
                      f'если меньше 3:'))
    if chose == 1:
        print(f'Ваше число это {guess}')
        break
    elif chose == 2:
        minimum = guess
    elif chose == 3:
        maximum = guess

#-----------------------------------

# guess = (minimum + maximum)/2
# print(guess)
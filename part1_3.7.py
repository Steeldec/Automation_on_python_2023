# print('Задача 1. Язык математики')
#
# # В первый же день на сайте отвалилась формула по расчёту рекламной метрики, и только Вася может её поправить.
# # Часть программы с вводными данными представлена ниже, отдельно записана формула на математическом языке.
#
# # Дана программа:
#
# a = 8
# b = 10
# c = 12
# d = 18
#
# # Продолжите программу: переведите выражение с математического языка на язык Python, запишите его в переменную res и выведите результат.
#
# #
# # Выражение:
#
# res = ((-3 + a ** 2) * b - 2 ** 3) / (c - 2 * d)
# print(res)

# ___________------------------

# print('Задача 2. Финансовый отчёт')
#
# # Васе пришло очередное задание — автоматизация финансовой отчётности.
# # Звучит сложно, а на деле нужно просто написать код, который будет считать нужные для отчёта вычисления автоматически.
# # Вычисления, которые нужно реализовать в программе: сумму дохода первых двух кварталов поделить на сумму последних двух кварталов,
# # чтобы понять динамику роста или падения дохода.
#
# # Алгоритм действий в программе:
# # 1) Запросить у пользователя четыре числа.
# # 2) Отдельно сложить два первых и два вторых.
# # 3) Разделить первую сумму на вторую.
# # 4) Вывести результат на экран.
#
# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
# third_number = int(input("Enter third number: "))
# four_number = int(input("Enter four number: "))
#
# first_sum = first_number + second_number
# second_sum = third_number + four_number
# res = first_sum / second_sum
# print(res)

# --------3-----------
# print('Задача 3. Следующее и предыдущее числа')
#
# # В олимпиаде по программированию участвовали 1000 человек,
# # и программа автоматически распределила их по количеству баллов.
# # Иногда количество баллов у участников одинаковое,
# # и тогда комиссии нужно посмотреть фамилии одного из таких участников,
# # а также его соседей, это реализует специальная часть алгоритма.
# #
# # Напишите программу,
# # которая получает от пользователя число и выводит на экран два ответа — следующее и предыдущее число.
# # Результат:
#
# # Введите число: 5
# # После числа 5 идет число 6
# # До числа 5 идет число 4
# number = int(input('Enter number: '))
# more = number + 1
# less = number - 1
# print('После числа', number, 'идет число ', more)
# print('До числа', number, 'идет число', less)
# -----------4--------------
# print('Задача 4. Площадь треугольника')
#
# # Напишите программу,
# # которая запрашивает у пользователя длины двух катетов
# # в прямоугольном треугольнике и выводит его площадь.
# a = int(input('Enter side a: '))
# b = int(input('Enter side b: '))
# # Формула:
# s = (a * b) / 2
# print(f'Площадь прямоугольного треугольника с катетами {a} и {b} равна {s}')

# ========5---------
# print('Задача 5. Часы')
#
# # Напишите программу,
# # которая получает на вход число n — количество минут, — затем считает,
# # 1) сколько это будет в часах
# # 2) сколько минут останется
# # и выводит на экран эти два результата.
# # (В вычислениях вам помогут операции // и %)
#
# user_n = int(input('Enter number of minutes: '))
# hour = user_n // 60
# minutes = user_n % 60
# print(f'In {user_n} minutes, {hour} hour(s), and  {minutes} minute(s)')

# print('Задача 6. Проверяем бухгалтера')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79

# first_num = (input("Enter first number: "))
# second_num = (input("Enter second number: "))
# first_num = first_num[-2:]
# second_num = second_num[-2:]
# print("Сумма:", int(first_num) + int(second_num))
# one=int(input('Введите первое число: '))
# two=int(input('Введите второе число: '))
# summa=(one%100)+(two%100)
# print('Сумма: ',summa)
#----------7----------------
# user_num = int(input('Enter four-digit number: '))
# first_two = user_num // 100
# second_two = user_num % 100
# first_number = first_two // 10
# second_number = first_two % 10
# third_number = second_two // 10
# four_number = second_two % 10
# print('first -', first_number, 'second -',
#       second_number, 'third -', third_number, 'four -', four_number)
#--------------8------------------
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print(a, b)
# # # стереть эту строчку и вставить свой код здесь
# a = a + b
# b = a - b
# a = a - b
# print(a, b)


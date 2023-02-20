# first_name = input('Введите имя пользователя: ')
# greeting = 'Утро доброе'
# print(greeting, first_name)
# intro = "К сожалению, у Вас нет доступа к системе."
# info = "Пожалуйста, обратитесь к системному администратору."
# if first_name != 'Admin':
#     print(f"{intro}\n{info}")

# a = input('Введите первое слово: ')
# b = input('Введите второе слово: ')
# print(a, b)
# c = a
# a = b
# b = c
# print(a, b)
# ---------------3.5------------------------
# apples = 11
# boxes = 3
# full_boxes = apples // boxes
# print("Колличество полных ящиков ", full_boxes)
# rest_apples = apples % boxes
# print(f'Осталось яблок: {rest_apples}' )
#
# user = int(input('Введитечисло: '))
# print(f"Номер дома: {user % 10}")
# print(f"Номер квартиры: {user // 10}")

# raund = 100
# man1 = 204
# man2 = 202
# man3 = 206
# print(f'Первый спортсмен пробежал {man1 // raund} полных круга, и {man1 % raund} метра нового круга')
# print(f'Второй спортсмен пробежал {man2 // raund} полных круга, и {man2 % raund} метра нового круга' )
# print(f'Третий спортсмен пробежал {man3 // raund} полных круга, и {man3 % raund} метра нового круга')
# ------------------4.2 условные операторы-----------------------------------------------
# задача 2
# bank = int(input("Сколько у тебя денег?? "))
# price = 75000
# if bank >= price:
#     bank = bank - price
#     if bank < 5000:
#         bank = bank + 2000
#         print('сделана скидка')
#     print(f"Курс оплачен, на счету осталось {bank}")
# Задача 3
# son = int(input('number: '))
# l = list(range(1, 11))
# father = random.choice(l)
# print(f'отец загадал {father}')
# if son == father:
#     print('yes')
# else:
#     print('no')

# 5.2 __----------------

# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
# if x < y:
#     print('x меньше y')
# elif x > y:
#     print('y меньше x')
# else:
#     print('x равен y')

# задача 3
# money = int(input('Enter money: '))
# cheese = 60
# ice_cream = 20
# food = cheese + ice_cream
# if money >= cheese:
#     print('На сыр денег хватило')
#     money = money - cheese
#     if money >= ice_cream:
#         print('И на мороженое тоже!')
#     else:
#         print('Денег маловато, на мороженное не хватает')
# else:
#     print("Денег маловато")

# profit = int(input('сколько ты зарабатываешь ? '))
# if profit < 10000:
#     tax = profit * 13 / 100
#     print(f'Размер налога (13%) равен {tax}')
# elif 10000 <= profit <= 50000:
#     tax = profit * 20 / 100
#     print(f'Размер налога (20%) равен {tax}')
# elif profit < 0:
#     print('Доход не может быть отрицательным')
# else:
#     tax = profit * 30 / 100
#     print(f'Размер налога (30%) равен {tax}')


# while цикл________------------------------------
# balance = int(input('money on balance: '))
# while balance > 5000:
#     t = int(input('Цена: '))
#     balance = balance - t
# print(f"balance = {balance} хватит тратить")
# summ = 0
# number = int(input("Введите число: "))
# while number != 0:
#     summ += number
#     number = int(input('Введите число: '))
# print(summ)

# number = int(input("Введите password: "))
# while number != 235:
#     number = int(input("Введите password again: "))
#
# print('Пароль верен!')

# money = 0
# while money < 500000:
#     m = int(input("сколько отложить денег?"))
#     money = money + m
#     print(f'money = {money}')
# print(f'готово {money}')
# meters = 0
# weather = int(input('weather here: '))
# while weather > 15:
#     meters += 30
#     weather -= 2
#     if weather < 15:
#         print('Похолодало')
#         break
#     meters += 10
#     print(f'meters - {meters}, weather - {weather}')
# print(meters)
# трешовая задача, невозможно это воспринимать, че за дичь ?? еще и в обучающем ролике.
# с такими примерами можно отталкнуть всех начинающих изучать питон.
# Вы серьездно вы сами это читали ? это же невозможно нормально воспринимать
# summ = 0
# num = int(input('number here: '))
# while num != 0:
#     last_num = num % 10
#     print(last_num)
#     print(num)
#     if last_num == 5:
#         print('разрыв')
#         break
#     summ += last_num
#     num //= 10
# print(f'sum {summ}')
# import random
# num1 = range(1, 7)
# money = int(input('Введите стартовую сумму:'))
# while money < 10000:
#     # num = int(input('Сколько выпало на кубике?'))
#     num = random.choice(num1)
#     if num == 3:
#         print(f'Вы проиграли все! выпало {num}')
#         money = 0
#         break
#     print(f'Выиграли 500 рублей! выпало {num}')
#     money += 500
# print('Игра закончена.')
# print(f'итог осталось: {money} рублей')
# 6.4-------------------------------------------------------
# count = 10
# while count >= 0:
#     if count == 0:
#         print('Время вышло!')
#         #break
#     else:
#         print(count)
#     count -= 1

# while True:
#     n = int(input('продолжаем работать ? 1/0'))
#     if n == 0:
#         print('Приложение закрывается…')
#         break
# print('Работа завершена')
# n = 0
# while n != 5460:
#     print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
#     n = int(input('Введите код: '))
# print("Код верный, завершаю работу...")

# -----------6.5=------------------
# phrase = 'Я — программист!'
# count = 0
# r = int(input('количество строчек с фразой: '))
# while count < r:
#     print(phrase)
#     count += 1

# r = int(input('сколько раз ему напомнить?: '))
# phrase = 'Вы хотели не забыть о чём-то'
# count = 0
# while count < r:
#     print(phrase)
#     count += 1

# bag = int(input('Сколько мешков? '))
# count = 0
# total_weight = 0
# while count != bag:
#     weight = int(input('Сколько весит мешок?: '))
#     total_weight += weight
#     count += 1
#     ost = bag - count
#     print(f'осталось перенести мешков {ost}')
# print(f'Общий вес {total_weight} Кг')

# min, max = 1, 100
# hidden_number = int(input('Введите число от 1 до 100: '))
# choice = 0
# while True:
#     bufer = int((min + max)/2)
#     print('Если загаданное число это', bufer, 'поставьте 1, если больше 2, если меньше 3:')
#     choice = int(input())
#     if choice == 2:
#         min = bufer
#     if choice == 3:
#         max = bufer
#     if choice == 1:
#         print('Машина угадала ваше число, это -', bufer)
#         break


# По условиям задачи не доконца понятно как это должно работать
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
#
# # Второй способ, рабочий
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

# n = (100 + 1) // 2
# while True:
#     print('число больше равно или меньше', n)
#     ans = int(input('1-равно, 2 -больше, 3 - меньше'))
#     if ans == 1:
#         print('угадали')
#         break
#     elif ans == 2:
#         n = n + 1
#     else:
#         n -= 1

# for m in 100, 90, 95, 87, 102:
#     if m % 3 == 1:
#         print('yes')
#     else:
#         print('no')

# for n in 3, 7, 5, 6, 4:
#     two = n ** 2
#     three = n ** 3
#     four = n ** 4
#     print(two, three, four)

# winers = 0
# for n in 345, 19, 87, 1020, 421:
#     if len(str(n)) == 3 and n % 5 == 0:
#         print(f'tiket {n} win')
#         winers += 1
# print(winers)

# h = int(input('what time is it?'))
# for n in range(h):
#     print('re-ru')

# number = int(input('enter number: '))
# prime = True
# for divider in range(2, number):
#     if number % divider == 0:
#         prime = False
#         break
# if prime:
#     print('число простое')
# else:
#     print('число составное')

# number_students = 16
# list_students = []

# заполняем список
# for i in range(number_students):
#   list_students.append(random.randint(3, 5))
# print(list_students)
#
# count_3 = 0
# count_4 = 0
# count_5 = 0
#
# for score in list_students:
#   if score == 3:
#     count_3 += 1
#   elif score == 4:
#     count_4 += 1
#   else:
#     count_5 += 1
#
# if count_5 == count_4 == count_3:
#   print('\nСегодня всех поровну:', end=' ')
# else:
#   print('\nСегодня больше:', end=' ')
#   max_count = max(count_3, count_4, count_5)
#   if max_count == count_5:
#     print('\n\t\t\t\tотличников', end=' ')
#   if max_count == count_4:
#     print('\n\t\t\t\tхорошистов', end=' ')
#   if max_count == count_3:
#     print('\n\t\t\t\tтроечников', end=' ')
#
# print(f'\n\n("5":{count_5}, "4":{count_4}, "3":{count_3})')

# total_hours = int(input('сколько часов'))
# cells = 1
# for n in range(1, total_hours // 3 + 1):
#     cells = cells * 2
#     print(f'времени прошло {n * 3}, клеток {cells} , осталось {total_hours - (n * 3)}')
# print('ower')


# total_hours = int(input('число: '))
# for n in range(1, total_hours +1, 2):
#     kv = n ** 2
#     print(f'квадрат {n}, = {kv}')
#
# num = 1
# while total_hours >= num:
#     print(f'num {num} squere = {num ** 2}')
#     num += 2

# sec = int(input('сколько солдат '))
# rul = int(input('сколько правил '))
# total_ups = 0
# for n in range(sec, 0 , -4):
#     ans = int(input("answer "))
#     ups = 10 * n
#     if ans != rul:
#         print(f'{n} солдат, упал-отжался {ups} раз')
#         total_ups += ups
#
# print(total_ups)

# sec = int(input('сколько  '))
# for n in range(sec, 1 , -2):
#     print(n)

# envelope = 12 # 12 * 12 = 144
# letter = int(input('Введите размер письма: '))
# count = 0
#
# if envelope < letter:
#     eq = letter / 2
#     count += 1
#     if eq <= envelope:
#         print(f'письмо необходимо сложить {count} раз')
#
# else:
#     print('писимо помещается в конверт')


# print('Задача 9. Выражение')
# x, y = int(input('Введите x ')), 1
# for i in range(1,65):
#   if x - i == 0:
#     y = 0
#   else:
#     y *= (x - i) / (x - i - 1)
# print('Результат ', y)

# two_count = 0
# for n in range(5):
#   ans = input('Кто написал Онегина?')
#   if ans.lower() == 'пушкин':
#     print('правильно, садись 5')
#     break
#   else:
#     print('не верно, садись 2')
#     two_count += 1
#
# print(f"{two_count} из студентов получили двойку")

# while True:
#   ans = input('выполнил задание?')
#   if ans.lower() == 'ща':
#     break

# name = input('как тебя зовут?')
# ans = input(f'{name} Купи слона')
# while True:
#     ans = input(f'все говорят {ans} а ты Купи слона!')

# text = 'питон это мощный инструмент для создания программ самого разнобразного назначения' \
#        'доступный даже для начинающих. с его помощью можно решать задачи различных типов'
# o = 0
# n = 0
# first = input('enter first symbol')
# second = input('enter second symbol')
# for i in text:
#     if i.lower() == first:
#         o += 1
#     elif i.lower() == second:
#         n += 1
#
# print(f'в тексте буква "o" встречается {o} раз\n,буква "н" встречается {n} раз ')
# print('_' * 10)
# for n in range(4):
#     for i in range(10):
#         if i == 0 or i == 9:
#             print('|', end='')
#         else:
#             print('0', end='')
#     print()
# print('_' * 10)
# --------------------------------------
# print("-" * 10)
# for i in range(10):
#     if i == 0 or i == 9:
#         print("|", end="")
#     else:
#         print("0", end="")
# print()
# for i in range(10):
#     if i == 0 or i == 9:
#         print('|', end='')
#     else:
#         print('0', end='')
# print()
# for i in range(10):
#     if i == 0 or i == 9:
#         print('|', end='')
#     else:
#         print('0', end='')
# print()
# for i in range(10):
#     if i == 0 or i == 9:
#         print('|', end='')
#     else:
#         print('0', end='')
# print()
# print('_' *10)

# number = int(input('enter number: '))
# summ = 0
# step = 3
# for n in range(3):
#     print(number, end='.')
#     summ = number + summ
#     number += step
#
# print(summ)

# number = int(input('enter number (N >= 0): '))
# print('-=-', end='')
# for n in range(0, number + 10, 10):
#     print(n, end='-=-')

# ------------------ 10.1 Работа со вложенными циклами -----------------------------
# for n in range(1, 10):
#     for i in range(1, 10):
#         a = n * i
#         print(f'{n} * {i} = {a}')
#     print()

# for n in range(6):
#     for i in range(6):
#         print(n + i, end=' ')
#     print()

# for n in range(1, 10):
#     for i in range(1, 10):
#         print(n * i, end='\t')
#     print()

# num = int(input('Enter number: '))
# count = 0
# for n in range(num + 1):
#     for i in range(num + 1):
#         print(n + i, end=' ')
#     print()

# for row in range(10):
#     for col in range(0, -10, -1):
#         print(row + col, end='\t')
#     print()
# ----------- 10.2 ------------------
# size = int(input('size: '))
# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if row % 2 == 0:
#             print(row, end='\t')
#         else:
#             print(col, end='\t')
#     print()

# Координатные оси
# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print('-', end='')
#         elif col == 24:
#             print('|', end='')
#         else:
#             print(' ', end='')
#     print()

# size = 6#int(input('size: '))
# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if col % 3 == 0:
#             print(col, end='\t')
#         else:
#             print(row, end='\t')
#     print()

# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print('-', end='')
#         elif col == 24:
#             print('|', end='')
#         else:
#             print(' ', end='')
#     print()

# -----------------10.3--------------------------
# Как блять можно это понять ????

# size = 6#int(input('size: '))
# for row in range(size):
#     for col in range(size):
#         if row < col:
#             print(0, end='\t')
#         elif row > col:
#             print(2, end='\t')
#         elif row == col:
#             print(1, end='\t')
#
#     print()
# Пиздец!!!!

# for row in range(20):
#     for col in range(50):
#         # if row == 9:
#         #     print('-', end='')
#         if col == 24:
#             print('|', end='')
#         elif col == row + 29:
#             print('\\', end='')
#         elif col == - row + 19:
#             print('/', end='')
#         else:
#             print(' ', end='')
#
#     print()


# for row in range(20):
#     for col in range(30):
#         if row == 0:
#             print('-', end='')
#         elif col == 0:
#             print('|', end='')
#         elif col == 29:
#             print('|', end='')
#         else:
#             print(' ', end='')
#     print()

# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print('-', end='')
#         elif col == 24:
#             print('|', end='')
#         elif row == col - 29:
#             print('\\', end='')
#         elif col == - row + 19:
#             print('/', end='')
#         else:
#             print(' ', end='')
#
#     print()

# И как я до этого должен был догодаться ?? бредятина


# size = 5#int(input('size: '))
# for row in range(size):
#     for col in range(size):
#         buf_x = (size - 1) - row
#         if buf_x > col:
#             print(0, end='\t')
#         elif buf_x == col:
#             print(1, end='\t')
#         else:
#             print(2, end='\t')
#
#     print()

# people = int(input('кол-во людей в очереди: '))
#
# for hour in range(people + 1):
#     print(f'идет час {hour}')
#     for y in range(hour, people):
#         print(f'номер в очереди {y}')
#     print()
#
# print('Очередь обслужена!')

# seqnum = int(input('сколько будет чисел: '))
# numeral = int(input('какую цифру считаеем: '))
# while 0 < numeral > 9:
#     numeral = int(input('Цифра от 1 до 9! Введите новую цифру'))
#
# num_count = 0
# for num in range(seqnum):
#     number = str(input(f'Введите число {num +1}: '))
#     for n in number:
#         if str(numeral) == n:
#             num_count += 1
# print(num_count)

# people = int(input('кол-во людей в очереди: '))
# for hour in range(people):
#     print(f'идет час {hour}')
#     for n in range(hour, people):
#         print(f'номер в очереди {n}')
#
# print('end')

# numeral = int(input('Сколько всего будет чисел: '))
# count = 0
# num = str(input('Какое число ищем? '))
#
# for n in range(numeral):
#     number = str(input(f'введите число {n}: '))
#     for y in number:
#         if y == num:
#             count += 1
#
# print(f'число {num} встречается {count} раз')

# Задача 3. Лестница чисел
# num = int(input('enter number: '))
# for row in range(num + 1):
#     for col in range(row, num + 1):
#         print(col, end='\t')
#     print()


# pin = '1984'
# print("введите пинкод у вас 3 попытки")
# p = 3
# for n in range(p, 0, -1):
#     user = input(f':')
#     p -= 1
#     if user != pin:
#         print(f'неверно, осталось {p} попыток')
#         if p < 1:
#             print("ваша карта заблокирована")
#     else:
#         print('Correct!')
#         break

# a = int(input("Введите число: "))
# k = 0
# for i in range(2, a // 2+1):
#     if (a % i == 0):
#         k = k+1
# if (k <= 0):
#     print("Число простое")
# else:
#     print("Число не является простым")

# seqnum = int(input('Введите количество чисел: '))
#
# count_simple = 0
# for n in range(seqnum):
#     count = 0
#
#     number = int(input('Введите число: '))
#     for num in range(2, number // 2+1):
#         if number % num == 0:
#             count += 1
#     if count <= 0:
#         count_simple += 1
#         print('Число простое')
#     else:
#         print('Число не является простым')
#
# print(f'Количество простых чисел в последовательности: {count_simple}')

# sum_list = []
# full_number = []
# seq = int(input('Сколько чисел ? '))
# for n in range(1, seq):
#     count = 0
#     user_number = str(input(f'Введите {n} число: '))
#     full_number.append(int(user_number))
#     for num in user_number:
#         count += int(num)
#     sum_list.append(count)
#
# print(sum_list)
# print(full_number)
# max_index = sum_list.index(max(sum_list))
# print(f'наибольшее число -  {full_number[max_index]} сумма его цифр - {max(sum_list)}')

# height = int(input('Введите число - высоту пирамиды [5]: ') or 5)
# for y in range(0, height):
#     print(' ' * (height - y - 1), end='')
#     print('#' + '#' * 2 * y)
#
# print()

# rows = 5
# new_num = 1
#
# for line in range(rows): # Идем по строчкам
#     for space in range(rows - line, 0, -1):
#         print(end=' ')
#     for number in range(line + 1): # идем по числам
#         print(new_num, end='')
#         new_num += 2
#
#
#     print()


# height = 5
# for row in range(height):
#     for space in range(height - row, 0, -1):
#         print(end='\t')
#     for col in range(row + 1):
#         print('#', end='\t')
#         print('', end='\t')
#     print()

# for line in range(height):
#     for space in range(height - line, 0, -1):
#         print(end='\t')
#     for col in range(line + 1):
#         print('#', end='\t')
#         print('', end='\t')
#     print()

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

# ----- 11.2 float ---------------
# task 1
# bet = float(input('Сколько ставим?'))
# coeff = float(input('Какой коэффициент?'))
#
# win = round(bet * coeff, 3)
# print(f'Потенциальный выигрыш: {win}')

# task 2

# years = int(input('возраст'))
# temperature = float(input('температура'))
# print(f'gift {years * temperature * 1.5}')

# task 3

# height = float(input('Рост'))
# weight = float(input('Какой вес'))
# imt = round(weight / (height ** 2), 2)
#
# if imt <= 18.5:
#     print('недобор')
# elif imt <= 25:
#     print('всё нормально')
# elif imt <= 30:
#     print('избыток')
# else:
#     print('ожирение')

# 11.3 ---------

# task 1

# cht = int(input('Сколько чатлов? '))
#
# cr = cht / 2200
# print(f'это {cr} cr')
# ship = int(cr / 0.5)
# print(f'Можно купить кораблей {ship}')


# task 2
# while True:
#     print('Введите местоположение фигуры')
#     x = float(input('По горизонтали: '))
#     y = float(input('По вертикали: '))
#
#     if 0 < x < 0.8 and 0 < y < 0.8:
#         squere_x = int(x * 10)
#         squere_y = int(y * 10)
#         print(f'Фигура находится в клетке ({squere_x}, {squere_y})')
#         break
#     else:
#         print('Клетки с такой координатой не существует')

# task 3

# while True:
#     print('Введите местоположение фигуры')
#     x = float(input('По горизонтали: '))
#     y = float(input('По вертикали: '))
#
#     if 0 < x < 0.8 and 0 < y < 0.8:
#         squere_x = int(x * 10)
#         squere_y = int(y * 10)
#         print(f'Фигура находится в клетке ({squere_x}, {squere_y})')
#         centr_x = squere_x / 10 + 0.05
#         centr_y = squere_y / 10 + 0.05
#         delta_x = round(centr_x - x, 3)
#         delta_y = round(centr_y - y, 3)
#         print(f"Поправьте положение фигуры на ({delta_x}, {delta_y})")
#         break
#     else:
#         print('Клетки с такой координатой не существует')

# 11.4---------------
# task 1
# a = float(input('a: '))
# b = float(input('b: '))
# c = float(input('c: '))
#
# p = (a + b + c) / 2
#
# s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#
# print(f'площадь треугольника {s}')

# task 3

# a = float(input('a: '))
# print(f'округляет вниз {math.floor(a)}')
# print(f'округляет вверх {math.ceil(a)}')
# print(f'извлекает квадратный корень {math.sqrt(a)}')
# print(f'возводит экспоненту в степень, равную числу {math.exp(a)}')
# print(f'считает натуральный логарифм числа {math.log(a)}')
# print(f'считает логарифм числа по основанию 2 {math.log2(a)}')
# print(f'считает логарифм числа по основанию 10 {math.log10(a)}')
# print(f'считает синус числа {math.sin(a)}')
# print(f'считает косинус числа {math.cos(a)}')
# print(f'считает факториал числа {math.factorial(int(a))}')

# --- 12. 2 Функции и их вызов ___

# task 1

# def greeting():
#     print('Hi')
#     print('welcome!')
#
# while True:
#     answer = input('Come in ? "yes" or "no"')
#     if answer.lower() == 'yes':
#         greeting()
#     elif answer.lower() == 'no':
#         print('ok, good day!')
#     else:
#         print('`i not understand? try again')

# print('next!')

# task 2

# def summ():
#     a = int(input())
#     b = int(input())
#     print(f'Всего {a + b} шт.')
#
# print('Сколько мешков рыбы и мяса?')
# summ()
# print('Сколько буханок белого и чёрного хлеба?')
# summ()
# print('Сколько вёдер воды и молока?')
# summ()

# task 3

# def person():
#     print(f' Фамилия: Иванов\n Имя: Василий\n Улица: Пушкина\n Дом: 32\n ')
#
# person()
# person()
# person()


# - 12.3 ---

# task 1

# def about_wather(price):
#     print('Название: КлирВотер')
#     print('Производитель: ВодЗавод')
#     print(f'Цена: {price}')
#     print()
#
# about_wather(25)
# about_wather(30)
# about_wather(40)


# task 2

# radius1 = float(input('радиус планеты '))
#
#
# def sphere_area(radius):
#     s = 4 * math.pi * (radius ** 3)
#     print(f'площадь сферы {s}')
#
#
# def sphere_volume(radius):
#     v = 4 / 3 * math.pi * (radius ** 3)
#     print(f'объём шара {v}')
#
#
# sphere_area(radius1)
# sphere_volume(radius1)

# task 3


# number = int(input(' вводит число N'))

# def is_prime(number):
#     for n in range(2, int(number ** 0.5) + 1):
#         if number % n == 0:
#             print('не простое')
#             break
#     else:
#         print('простое')
#
# n = int(input("Введите количество чисел в последовательности: "))
# for i in range(n):
#     new_number = int(input("Введите число: "))
#     is_prime(new_number)

# - 12.4 ---

# task 1
# def middle(a, b):
#     all_num = 0
#     count = 0
#     for n in range(a, b + 1):
#         all_num += n
#         count += 1
#     mid = all_num / count
#     print(f'среднее арифметическое всех чисел из отрезка [{a}; {b}] это - {mid}')
#
# while True:
#     n_a = int(input("Введите число a: "))
#     n_b = int(input("Введите число b: "))
#     if n_a > n_b:
#         print('а всегда должно быть меньше, чем b')
#     else:
#         break

# middle(n_a, n_b)

# task 2

# def post(surname, name, country, city, street, house, apartment):
#     print(f'фамилия: {surname} ')
#     print(f'имя: {name}')
#     print(f'страна: {country}')
#     print(f'город: {city}')
#     print(f'улица: {street}')
#     print(f'дом: {house}')
#     print(f'квартира: {apartment}')
#
#
# post('ivanov', 'petya', 'belarusia', 'minsk', 'lenina', 32, 12)

# task 3
# def my_distance(x, y):
#     distance = math.sqrt(x ** 2 + y ** 2)
#     print(distance)
#
#
# def between_distance(x_1, y_1, x_2, y_2):
#     distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
#     print(distance)
#
# choise = int(input('1 - До точки, 2 - между точками'))
# if choise == 1:
#     x = float(input('введите x'))
#     y = float(input('введите y'))
#     my_distance(x, y)
# elif choise == 2:
#     x_1 = float(input('введите x1'))
#     y_1 = float(input('введите y1'))
#     x_2 = float(input('введите x2'))
#     y_2 = float(input('введите y2'))
#     between_distance(x_1, y_1, x_2, y_2)

# --------- 13.2 ---------
# task 1
# def summ(num):
#     count = 0
#     for n in range(1, num + 1):
#         count += n
#     return count
#
#
# num = int(input('number N'))
# result = int(summ(num))
# print(summ(num))
# print(summ(result))


# task 2

# def gcd(num1, num2):
#     count_x = 1
#     count_y = 1
#     list_x = []
#     list_y = []
#     x_y =[]
#     while count_x <= num1:
#         if num1 % count_x == 0:
#             list_x.append(count_x)
#         count_x += 1
#
#     while num2 >= count_y:
#         if num2 % count_y == 0:
#             list_y.append(count_y)
#         count_y += 1
#
#     for n in list_x:
#         if n in list_y:
#             x_y.append(n)
#     return max(x_y)
#
# num1 = int(input('Введите первое число:'))
# num2 = int(input('Введите второе число:'))
#
# print(f'НОД = {gcd(num1, num2)}')

# task 3

# def numeral_count(number1):
#     a = len(str(number1))
#     return a

# def numeral_count(num):
#     count = 0
#     while num > 0:
#         num //= 10
#         count += 1
#     return count


# tasks = int(input('Введите кол-во задач: '))
#
# count_max = 0
# count_num = 0
# for n in range(tasks):
#     number = int(input('Введите число: '))
#
#     if numeral_count(number) > count_max:
#         count_max = numeral_count(number)
#         count_num = number
#
# print(count_num)

# 13.3 ------------
# task 1
# x = 1
# count = 0
# while x != 0:
#     x /= 2
#     count += 1
#     print(x)
# print(count)

# task 2

# num = 5.02e-1#int(input('Введите число в эксп. форме: '))
# x = 1
# count = 0
# while x <= 2:
#     count += 1
#     x += num
#
# print(f'Кол-во прибавлений: {count}')

# task 3

# start_number = float(input("Введите число: "))
# count = 0
# while start_number > 10:
#     count += 1
#     start_number /= 10
#
# print(f"Формат плавающей точки: x = {start_number} * 10 ** {count}")

# 13.4 ------------
# task 1

# def func(tax, new_tax):
#     tax1 = tax + new_tax
#     if tax1 > tax:
#         print('Результат: Бюджет увеличится')
#     else:
#         print('Результат: Бюджет не изменится')
#
#
# tax = float(input('Введите бюджет страны: '))
# new_tax = float(input('Новые поступления (налог): '))
#
# func(tax, new_tax)


#task 2

# def fuc(a, b, c):
#     if a + b == c:
#         return True
#     else:
#         return False
#
# a = float(input('Введите бюджет страны: '))
# b = float(input('Новые поступления (налог): '))
# c = float(input('Новые поступления (налог): '))
#
#
# print(fuc(a, b, c))

# def reverse1():
#     number1 = int(input("Введите целое число: "))
#     number2 = 0
#     while number1 > 0:
#         last = number1 % 10
#         number1 = number1 // 10
#         number2 = number2 * 10
#         number2 = number2 + last
#     # print("Число наоборот: ", number2)
#     return number2
#
# def reverse2(number1):
#     number2 = 0
#     while number1 > 0:
#         last = number1 % 10
#         number1 = number1 // 10
#         number2 = number2 * 10
#         number2 = number2 + last
#     return number2
#
# num_1 = reverse1()
# num_2 = reverse1()
# summ = num_1 + num_2
# summ_2 = reverse2(summ)
#
# print(f'Первое число наоборот: {num_1}')
# print(f'Второе число наоборот: {num_2}')
# print(f'Сумма: {summ}')
# print(f'Сумма наоборот: {summ_2}')


# def reverse2(number1):
#     number2 = 0
#     while number1 > 0:
#         last = number1 % 10
#         number1 = number1 // 10
#         number2 = number2 * 10
#         number2 = number2 + last
#     return number2
#
# print(reverse2(456))

# def change_number(number, num_count):
#     temp = number
#     while temp > 0:
#         temp //= 10
#         last_digit = number % 10
#         first_digit = number // 10 ** (num_count - 1)
#         between_digits = number % 10 ** (num_count - 1) // 10
#         number = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
#     return number
#
# print(change_number(1275, 4))
# print(1 // 10)

# def count_numbers(number):
#     num_count = 0
#     temp = number
#     while temp > 0:
#         num_count += 1
#         temp = temp // 10
#
#     return num_count
#
# print(count_numbers(4564))

# def calc_depth(start, end):
#     return start + (end - start) / 2
#
#
# def calc_danger(num):
#     return num ** 3 - 3 * num ** 2 - 12 * num + 10
#
#
# max_danger = float(input('Введите максимально допустимый уровень опасности: '))
# depth_top = 0.0
# depth_bottom = 4.0
#
# if max_danger <= 0:
#     print('Ошибка. Максимально допустимый уровень должен быть больше 0')
# else:
#     depth = calc_depth(depth_top, depth_bottom)
#     danger = calc_danger(depth)
#     # print('Глубина:', depth, 'Опастность:', danger)
#     while abs(danger) > max_danger:
#         if danger > 0:
#             depth_top = depth
#         else:
#             depth_bottom = depth
#         depth = calc_depth(depth_top, depth_bottom)
#         danger = calc_danger(depth)
#         # print('Глубина:', depth, 'Опастность:', danger)
#     print('Приблизительная глубина безопасной кладки: ', depth, 'm')

# print(0.1 + 0.1 + 0.1)

result = 2 ** 3 ** 4
print(f'результат {result}')
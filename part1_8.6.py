print('Задача 1. Космическая еда')

# Ваш космический корабль потерпел крушение на пустынной планете.
# Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки.
# Из прошлого опыта вы знаете,
# что если будете экономно питаться, то у вас будет уходить по 4 килограмма гречки в месяц.
#
# Чтобы прикинуть гречневый бюджет,
# вы решили написать программу, которая выведет информацию
# о том сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее,
# пока она не закончится.
# Используйте цикл for.
# groats = 100
# month = 0
# for groat in range(groats, 0, -4):
#     month += 1
#     print(f'через {month - 1} месяц останеться {groat} кг гречки')
# print(f'гречки хватит на  {month} месяцев')
# ------------------------------------------------
print('Задача 2. Долги')

# МирПрогБанк наконец-то разделил законопослушных граждан и должников и поместил их в разные базы.
# Но банк не торопится как-то слишком сильно давить на возврат денег.
# Сейчас операторам банка дали задание
# позвонить каждому пятому должнику из списка (они нумеруются с нуля) и спросить,
# сколько примерно денег каждый из них задолжал банку.
#
# Напишите программу,
# которая принимает на вход количество должников,
# затем спрашивает у каждого пятого (начиная с 0) его долг.
# В конце выводится общая сумма долгов.

# Пример:
#
# Введите количество должников: 13
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Должник с номером 10
# Сколько должны? 2000
# Общая сумма долга: 8000
# debtors = int(input('Введите количество должников: '))
# count = 0
# for debtor in range(0,debtors, 5):
#     print('Должник с номером', debtor)
#     debt = int(input('Сколько должны? '))
#     count += debt
# print('Общая сумма долга:', count)

# ------------------------------------------------
print('Задача 3. Таймер для микроволновых печей')

# Мы разрабатываем микропрограмму — таймер обратного отсчета для микроволновых печей.
# Некоторым пользователям не нравится пищащий звук.
# Есть задача убрать звук по готовности и заменить его сообщением на LED-экране.
# В нашем случае будем выводить в консоль сообщение с обратным отсчетом в секундах от “reverse_timer” до момента готовности, то есть «0» секунд, и спрашивать пользователя, готов ли он забрать еду.

# Пользователь в любой момент может прервать режим разогрева, введя «1» (то есть ответить «Да, еда готова»), тогда программа выводит на экран сообщение «Ваша еда готова, можете забрать» и показывает, на какой секунде был прерван таймер.
# Если пользователь отвечает «0», что равноценно «Нет», то таймер уменьшается. Когда он достигнет «0» секунд, выводим сообщение «Ваша еда готова, осторожно горячo!»

# В данном задании используем цикл for.
# “reverse_timer” – переменная счетчик, которую запрашиваем у пользователя через функцию ввода input.

# reverse_timer = int(input('Введите кол-во секунд: '))
# user_input = 0
#
# for second in range(reverse_timer, 0, -1):
#     user_input = int(input(f'Готовиться уже {second} секунд, Готовы забрать еду? 1 - да, 2 - нет '))
#     if user_input == 1:
#         print(f'Ваша еда готова, можете забрать. таймер прерван на {second} секунде')
#         break
#
# if user_input != 1:
#     print('Ваша еда готова, осторожно горячo!')


# ------------------------------------------------
print('Задача 4. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры три числа a, b и c,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).

# start_a = int(input('Введите число a: '))
# end_b = int(input('Введите число b: '))
# num_c = int(input('Введите число c: '))
#
# total_num = 0
# count = 0
# for n in range(start_a, end_b + 1):
#     if n % num_c == 0:
#         total_num = n + total_num
#         count += 1
#         #print(f' число - {n} сумма -  {total_num} всего чисел - {count}')
# print(f'Среднее арифметическое = {int(total_num / count)}')


# ------------------------------------------------
print('Задача 5. Функция 2')

# В прошлый раз мы написали Саше программу,
# которая считает функцию  в каждой точке отрезка и с нужным шагом, начиная с конца - от большего значения X к меньшему, выводит ответ на экран.
# Но теперь ему нужно,
# чтобы значения считались в обратном порядке.
# Плюс к этому в программе ему нужно сделать так,
# чтобы можно было настраивать шаг, с которым он скачет по точкам отрезка.
#
# Напишите программу,
# которая получает на вход начало и конец отрезка, а также шаг.
# Затем высчитывает функцию игрек в каждой точке отрезка
# и с нужным шагом, начиная с конца, и выводит ответ на экран.

# Сама функция выглядит так:
# y = x**3 + 2*x**2 - 4x + 1

# Пример:
#
# Введите начало отрезка: -2
# Введите конец отрезка: 2
# Введите шаг: -1
# В точке 2 функция равна 9
# В точке 1 функция равна 0
# В точке 0 функция равна 1
# В точке -1 функция равна 6
# В точке -2 функция равна 9

# start_a = int(input('Введите начало отрезка: '))
# end_b = int(input('Введите конец отрезка: '))
# step = int(input('Введите шаг: '))
# for x in range(end_b, start_a - 1, step):
#     y = (x ** 3) + (2 * (x ** 2)) - (4 * x) + 1
#     print(f'В точке {x} функция равна {y}')


# ------------------------------------------------
print('Задача 6. Письмо')  # 111!!!!!!!!!!

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
#
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.

# convert = 12
# letter = int(input('Введите размер письма: '))
# count = 0
# решение через while
# while True:
#     if convert < letter:
#         letter = letter - 12
#         count = count + 1
#
#     elif convert >= letter:
#         print(f'писимо ,было сложено {count} раз, теперь размером {letter} см')
#         print(f'писимо помещается в конверт')
#         break
# решение пока не придумал !!!!!!!!!!!
# for n in range(letter, convert, -12):
#     count += 1
#     letter = letter - 12
#
# print(f'писимо ,было сложено {count} раз, теперь размером {letter} см')


# ------------------------------------------------
print('Задача 7. Стипендия')

# Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
#
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

# educational_grant = int(input('Введите стипендию: '))
# expenses = int(input('Введите расходы на проживание: '))
# total_expenses = expenses
# total_grant = 0
# for n in range(1, 11):
#     # считаем расходы
#     if n > 1:
#         percent = (expenses / 100) * 3
#         expenses = expenses + percent
#         total_expenses = total_expenses + expenses
#     #     print(f'расходы - {expenses:.3f} рублей в {n} месяц')
#     # else:
#     #     print(f'расходы - {expenses:.3f} рублей в {n} месяц')
#
#     # Считаем стипендию
#     total_grant = educational_grant + total_grant
#
# print(f'У родителей необходимо попросить {total_expenses - total_grant:.3f}')


# ------------------------------------------------
print('Задача 8. Сумма ряда')

# Дано натуральное число n.
# Напишите программу для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N
# Решение загуглаил, как это решается не имею ни малейшего понятия.
# Зачем давать такие задачи, где чистая математика как они помогают разобраться в цикле ?
# number = int(input('Введите число n: '))
# s = 1
# for n in range(1, number + 1):
#     s += (-1) ** n * 1 / 2 ** n
#     print('Сумма ряда n равно ', s)
# ------------------------------------------------
print('Задача 9. Выражение')

# Дано число x.
# Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))
# number, y = int(input('Введите число x: '))
# # y = 1
# for n in range(1, 65):
#     if number - n == 0:
#         y = 0
#     else:
#         y *= (number - n) / (number - n -1)

# number = int(input('Введите число x: '))
#
# for n in range(1, 7): #1, 3, 7, 15, 31, 63:
#     num1 = (number - (2 ** n - 1))
#     print(n)
#     print(num1)

x = int(input('Введите число X: '))
numerator = 1
denominator = 1

for num in range(1, 7):
   exp1 = (x - (2 ** num - 1))
   numerator *= exp1
   exp2 = (x - 2 ** num)
   denominator *= exp2

if denominator == 0:
   print('На 0 делить нельзя!')
else:
   print(numerator / denominator)
# ------------------------------------------------
print('Задача 10. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
#
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
#
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

# boys = int(input('Введите количество мальчиков: '))
# girls = int(input('Введите количество девочек: '))
# result = ''
#
# if (boys - girls) > 2 or (girls - boys) > 2:
#     print('Ответ: Нет решения')
# elif boys >= girls:
#     two = boys - girls
#     for n in range(two):
#         result += ' B G B'
#     for i in range(girls - two):
#         result += ' B G'
#
# else:
#     two = girls - boys
#     for n in range(two):
#         result += ' G B G'
#     for j in range(two):
#         result += ' G B'
#
#
# print(f'Ответ: {result}')
# ----------------------------------------

# ------------------------------------------------

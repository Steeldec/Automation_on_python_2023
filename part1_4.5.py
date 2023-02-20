# print('Задача 1. Датчик погоды')

# В за окном квартиры стоит датчик погоды, который определяет, идёт ли дождь. Если идёт, датчик оповещает сообщением: «Пошёл дождь. Возьмите зонтик!»

# Напишите программу, которая получает на вход число 0 или 1. Единица означает, что дождь идёт. В таком случае выводите на экран сообщение: «Пошёл дождь. Возьмите зонтик!». Ноль означает, что дождя нет, в этом случае надо вывести сообщение «Дождя нет!»

# Пример 1:
# На улице идёт дождь? 1
# Пошёл дождь. Возьмите зонтик!

# Пример 2:
# На улице идёт дождь? 0
# Дождя нет!

# while True:
#     rain = int(input("На улице идет дождь ? 1 = (Да), 2 = (Нет) "))
#     if rain == 1:
#         print("Пошел дождь. Возмите зонтик!")
#         break
#     elif rain > 2:
#         print('Введите 1(Да) или 2(Нет)')
#     else:
#         print('Дождя нет!')
#         break
#-----------------------------------------------------------------
# print('Задача 2. Поступление')

# Вася работает разработчиком, и его компания создаёт сайт для образовательной компании. Заказчики попросили реализовать калькулятор баллов ЕГЭ в помощь поступающим. Эту задачу отдали Васе.

# Напишите программу, которая запрашивает у пользователя результаты ЕГЭ по трём экзаменам, и проверяет, поступил ли он на бюджет. Проходной балл равняется 270. Выведите соответствующее сообщение.

# Пример 1:
# Введите количество баллов по русскому языку: 90
# Введите количество баллов по математике: 90
# Введите количество баллов по информатике: 90

# Поздравляю, ты поступил на бюджет!

# Пример 2:
# Введите количество баллов по русскому языку: 100
# Введите количество баллов по математике: 50
# Введите количество баллов по информатике: 70

# К сожалению, ты не прошёл на бюджет.

# score = 270
# russian = int(input('Введите количество баллов по русскому языку: '))
# math = int(input('Введите количество баллов по математике: '))
# computer_since = int(input('Введите количество баллов по информатике: '))
#
# all_score = russian + math + computer_since
#
# if score <= all_score:
#     print('Поздравляю, ты поступил на бюджет!')
# else:
#     print('К сожалению, ты не прошёл на бюджет.')


#-------------------------------------------------------------------------
# print('Задача 3. Следим за расписанием')

# После выполненной задачи Вася устал и понял, что весь следующий день ему придётся восстанавливать силы. Вася решил, что работать он будет только в чётные дни и написал небольшую программу, которая поможет ему не пропустить рабочий день.

# Напишите программу, которая проверяет, чётное ли число ввёл пользователь, и выводит соответствующее сообщение.

# Подсказка: для проверки чётности используйте оператор %.

# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print('Число четное')
# else:
#     print('Число не четное')





#------------------------------------------------------------------------------
# print('Задача 4. Калькулятор скидки')

# Васин друг переехал в новую квартиру, и ему нужно купить три стула в разные комнаты. Цены на стулья  разные, а в некоторых магазинах есть скидки. Друг хочет заказать у Васи калькулятор скидки, чтобы проще ориентироваться в ценах.

# Напишите программу, которая запрашивает три стоимости товара и вычисляет сумму чека. Если сумма чека превышает 10 000 руб., нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100). Итоговая сумма должна выводиться на экран.

# total_price = 0
# for n in range(1, 4):
#     price = int(input(f"Введите стоимость {n} покупки: "))
#     total_price = price + total_price
#
# if total_price > 10000:
#     discount = (total_price * 10) / 100
#     total_price = total_price - discount
#     print(f"Ваша скидка {discount} руб. итоговая сумма с учетом скидки {total_price} руб.")
# else:
#     print(f"Общая стоимость покупок {total_price} руб")



#--------------------------------------------------------------------------------
# print('Задача 5. Модуль числа')

# Создайте программу, которая найдёт модуль очередного числа x. Если число x отрицательное, то она должна перевести его в положительное, а в конце на экране должен быть модуль введённого числа.

# Пример:
# Ввели 5, ответ 5
# Ввели −7, ответ 7

# Подсказка: в некоторых случаях достаточно переприсвоить переменную со знаком минус.
# user_input = int(input('Введите число: '))
# if user_input < 0:
#     print(f"Ввели {user_input}, Ответ {user_input * -1} ")
# else:
#     print(f"Ввели {user_input}, Ответ {user_input} ")
#
# # решение через функцию абсольтного значения
# print(f"Ввели {user_input}, Ответ {abs(user_input)}")
#--------------------------------------------------------------------------------
# print('Задача 6. Игра в кубики')

# Вася понимает, как важен отдых после тяжёлого рабочего дня, поэтому часто ходит в местный бар с друзьями. Владелец бара любит азартные игры и иногда предлагает посетителям с ним сыграть. Вася избегает азартные игры, но предложил владельцу купить у него программу для расчёта результатов игры, которую можно выводить на экраны бара.

# Напишите программу: на вход в неё подаётся два числа. Если первое число больше или равно второму, то нужно вывести на экран их разность и отдельной строкой: «Игрок платит». В противном случае, вывести их сумму и отдельной строкой: «Владелец платит». Последней строкой на экран должна быть выведена фраза: «Игра окончена».

# Пример:
# Кубик Кости: 3
# Кубик владельца: 4
# Сумма: 7
# Владелец платит
# Игра окончена

# number_one = int(input('Введите первое число: '))
# number_two = int(input('Введите второе число: '))
#
# if number_one >= number_two:
#     differ = number_one - number_two
#     print(f"Кубик гостя: {number_two}\nКубик владельца: {number_one}\nРазность: {differ}")
#     print("Игрок платит")
# else:
#     total = number_one + number_two
#     print(f"Кубик гостя: {number_two}\nКубик владельца: {number_one}\nСумма: {total}")
#     print("Владелец платит")
#     print('Игра окончена')

#------------------------------------------------------------------------------------
# print('Задача 7. Хватит ли зарплаты')

# Вася набрался опыта и решил поискать вакансию с большей зарплатой. Его привлекла вакансия со странной формулой для расчёта заработной платы:
# 200 * hours / 2 ** 3 + hours


# Он хочет понять, сколько часов нужно отработать, чтобы хватило на погашение кредита и еду.

# Напишите программу, которая запрашивает у пользователя три числа: количество отработанных часов, остаток по кредиту и количество денег на еду. После этого рассчитывается зарплата по формуле. Если зарплата больше или равна сумме, которая требуется на кредит и еду, то выводится сообщение: «Часов хватает. Можно отдохнуть». В противном случае: «Часов не хватает. Придётся работать больше!»

# Пример:
# Введите отработанные часы: 80
# Введите остаток по кредиту: 1000
# Введите траты на еду: 5000
# Часов не хватает. Придётся работать больше!

# hours = int(input('Введите отработанные часы:'))
# credit = int(input('Введите остаток по кредиту:'))
# food = int(input('Введите траты на еду:'))
#
# pay = (200 * hours) / (2**3) + hours
# spend = credit + food
# if pay >= spend:
#     print('Часов хватает. Можно отдохнуть')
# else:
#     print('Часов не хватает. Придётся работать больше!')
#----------------------------------------------------------------------------------------
print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно
print('все числа разные')
number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))
number_three = int(input('Введите третье число: '))

# if number_one > number_two and number_one > number_three:
#     print(f'первое число {number_one}, больше второго {number_two}, и третьего {number_three}')
# elif number_two > number_one and number_two > number_three:
#     print(f'второе число {number_two}, больше первого {number_one}, и третьего {number_three}')
# elif number_three > number_one and number_three > number_two:
#     print(f'третье число {number_three}, больше второго {number_two}, и первого {number_one}')



# решение через список
num_list = []
num_list.append(number_one)
num_list.append(number_two)
num_list.append(number_three)
#
print(f"максимальное из введеных чисел {max(num_list)}")
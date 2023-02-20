# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
n = ''
a = 0
ph = ''
e = ''
i = ''
index = ''
post = ''
# данные о предпринимателе
nip = ''  # Добавил ввод полей ОГРНИП
inn = ''  # Добавил ввод полей и ИНН
pay = ''  # Расчётный счёт
bank = ''
bik = ''
corr = ''  # корреспондентский счет


def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, i_parameter, index_parameter,
                      post_parameter):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Индекс:', index_parameter)
    print('Почтовый адрес: ', post_parameter)

    if i:
        print('')
        print('Дополнительная информация:')
        print(i_parameter)


print('Приложение MyProfile для предпринимателей')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                n = input('Введите имя: ')
                while 1:
                    # validate user age
                    a = int(input('Введите возраст: '))
                    if a > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                ph = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        ph += ch

                e = input('Введите адрес электронной почты: ')
                user_index = input('Введите индекс: ')
                # Индекс вводится как произвольная строка, но в приложении сохраняются только цифры.
                for i in user_index:
                    if '0' <= i <= '9':
                        index += i

                post = input('Введите Почтовый адрес (без индекса):')
                i = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # Информация о предпринимателе
                while 2:
                    nip = input('Введите ОГРНИП (15 цифр): ')
                    if len(nip) != 15:
                        print('Номер ОГРНИП содержит 15 цифр, попробуйте еще раз')
                    else:
                        break
                inn = input('Введите ИНН: ')
                while 2:
                    pay = input('Введите Расчётный счёт (20 цифр): ')
                    if len(pay) != 20:
                        print('Номер Расчетного счета содержит 20 цифр, попробуйте еще раз')
                    else:
                        break
                bank = input('Введите Название банка: ')
                bik = input('Введите БИК: ')
                corr = input('Введите «Корреспондентский счёт: ')

            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(n, a, ph, e, i, index, post)

            elif option2 == 2:
                general_info_user(n, a, ph, e, i, index, post)

                # print social links
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП:', nip)
                print('ИНН: ', inn)
                print('Банковские реквизиты')
                print('Р/с:   ', pay)
                print('Банк:', bank)
                print('БИК: ', bik)
                print('К/с:   ', corr)

            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')

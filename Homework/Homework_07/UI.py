import adding as add
import logger as lg


print('\nТелефонная книга')


def ls_menu():
    while True:
        print('\nМЕНЮ')
        print('1. Показать все записи.')
        print('2. Добавить новую запись.')
        print('3. Изменить существующую запись.')
        print('4. Удалить существующую запись.')
        print('5. Выход.\n')
        n = сheck_number(input('Выберите пункт меню: '))

        if n == 1:
            lg.logging.info('The user has selected item number 1')
            print(add.retrive())

        elif n == 2:
            lg.logging.info('The user has selected item number 2')
            name = input('Введите имя: ')
            lg.logging.info('User entered: {name}')
            surname = input('Введите фамилию: ')
            lg.logging.info('User entered: {surname}')
            number = input('Введите номер телефона: ')
            lg.logging.info('User entered: {number}')
            email = input('Введите электронную почту: ')
            lg.logging.info('User entered: {email}')
            add.create(name, surname, number, email)

        elif n == 3:
            lg.logging.info('The user has selected item number 3')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            change = сheck_number(input('Введите номер пункта: '))

            if change == 1:
                lg.logging.info('The user has selected item number 3.1')
                search = input('Введите фамилию: ')
                lg.logging.info('User entered: {search}')
                add.retrive(surname=search)
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logging.info('User entered: {new_number}')
                add.update(id=user_id, new_number=new_number)

            elif change == 2:
                lg.logging.info('The user has selected item number 3.2')
                search = input('Введите имя: ')
                lg.logging.info('User entered: {search}')
                add.retrive(name=search)
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logging.info('User entered: {new_number}')
                add.update(id=user_id, new_number=new_number)

            elif change == 3:
                lg.logging.info('The user has selected item number 3.3')
                search = input('Введите номер телефона: ')
                lg.logging.info('User entered: {search}')
                add.retrive(number=search)
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logging.info('User entered: {new_number}')
                add.update(id=user_id, new_number=new_number)

            else:
                lg.logging.warning('User entered an invalid menu value')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 4:
            lg.logging.info('The user has selected item number 4')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            deleting = сheck_number(input('Введите номер пункта: '))

            if deleting == 1:
                lg.logging.info('The user has selected item number 4.1')
                search = input('Введите фамилию: ')
                lg.logging.info('User entered: {search}')
                print(add.retrive(surname=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                add.delete(id=user_id)

            elif deleting == 2:
                lg.logging.info('The user has selected item number 4.2')
                search = input('Введите имя: ')
                lg.logging.info('User entered: {search}')
                print(add.retrive(name=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                add.delete(id=user_id)

            elif deleting == 3:
                lg.logging.info('The user has selected item number 4.3')
                search = input('Введите номер телефона: ')
                lg.logging.info('User entered: {search}')
                print(add.retrive(number=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                add.delete(id=user_id)

            else:
                lg.logging.warning('User entered an invalid menu value')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 5:
            lg.logging.info('End')
            print('Спасибо за работу!')
            break

        else:
            lg.logging.warning('User entered an invalid menu value: {n}')
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

def сheck_number(arg):
    while arg.isdigit() != True:
        lg.logging.warning('User entered an invalid menu value: {arg}')
        print('\nОшибка. Вы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)

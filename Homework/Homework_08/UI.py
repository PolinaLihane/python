from time import time
import adding as add
import logger as lg


print('\nСотрудники компании')


def ls_menu():
    while True:
        print('\nВыберети необходимое действие')
        print('1. Показать все записи.')
        print('2. Поиск сотрудника по фамилии.')
        print('3. Сделать выборку сотрудников по должности.')
        print('4. Сделать выборку сотрудников по зарплате.')
        print('5. Добавить нового сотружника.')
        print('6. Обновить данные сотрудника.')
        print('7. Удалить существующую запись.')
        print('8. Закончить работу.\n')
        n = сheck_number(input('Выберите пункт меню: '))

        if n == 1:
            lg.logging.info('The user has selected item number 1')
            base = add.retrive()
            for lines in base:
                for line in lines:
                    print(line, end=' ')
                print()
           # print(*add.retrive(), sep='\n')

        elif n == 2:
            lg.logging.info('The user has selected item number 2')
            search = input('Введите фамилию: ')
            lg.logging.info(f'User entered: {search}')
            base = add.retrive(surname=search)
            for lines in base:
                for line in lines:
                    print(line, end=' ')
                print()
            # print(*add.retrive(surname=search), sep='\n')

        elif n == 3:
            lg.logging.info('The user has selected item number 3')
            search = input('Введите должность: ').lower()
            lg.logging.info(f'User entered: {search}')
            base = add.retrive(position=search)
            for lines in base:
                for line in lines:
                    print(line, end=' ')
                print()
            # print(*add.retrive(position=search), sep='\n')

        elif n == 4:
            lg.logging.info('The user has selected item number 4')
            search = input('Введите минимальную заработную плату: ')
            lg.logging.info(f'User entered: {search}')
            base = add.retrive(salary=search)
            for lines in base:
                for line in lines:
                    print(line, end=' ')
                print()
            # print(*add.retrive(salary=search), sep='\n')

        elif n == 5:
            lg.logging.info('The user has selected item number 5')
            name = input('Введите имя: ')
            lg.logging.info(f'User entered: {name}')
            surname = input('Введите фамилию: ')
            lg.logging.info(f'User entered: {surname}')
            number = input('Введите номер телефона: ')
            lg.logging.info(f'User entered: {number}')
            email = input('Введите электронную почту: ')
            lg.logging.info(f'User entered: {email}')
            salary = input('Введите зарплату: ')
            lg.logging.info(f'User entered: {salary}')
            position = input('Введите занимаемую должность: ')
            lg.logging.info(f'User entered: {position}')
            add.create(name, surname, number, email, salary, position)

        elif n == 6:
            lg.logging.info('The user has selected item number 6')
            print('1. Найти сотрудника по фамилии.')
            print('2. Найти сотрудника по должности.')
            change = сheck_number(input('Введите номер пункта: '))

            if change == 1:
                lg.logging.info('The user has selected item number 6.1')
                search = input('Введите фамилию: ')
                lg.logging.info(f'User entered: {search}')
                base = add.retrive(surname=search)
                for lines in base:
                    for line in lines:
                        print(line, end=' ')
                    print()
                # print(*add.retrive(surname=search), sep='\n')
                user_id = input('Введите id записи: ')
                lg.logging.info(f'User entered: {user_id}')
                new_position = input('Введите новую должность: ')
                lg.logging.info(f'User entered: {new_position}')
                add.update(id=user_id, new_position=new_position)
                new_salary = input('Введите новую заработную плату: ')
                lg.logging.info(f'User entered: {new_salary}')
                add.update(id=user_id, new_salary=new_salary)

            elif change == 2:
                lg.logging.info('The user has selected item number 6.2')
                search = input('Введите должность: ')
                lg.logging.info(f'User entered: {search}')
                base = add.retrive(position=search)
                for lines in base:
                    for line in lines:
                        print(line, end=' ')
                    print()
                # print(*add.retrive(position=search), sep='\n')
                user_id = input('Введите id записи: ')
                lg.logging.info(f'User entered: {user_id}')
                new_position = input('Введите новую должность: ')
                lg.logging.info(f'User entered: {new_position}')
                add.update(id=user_id, new_position=new_position)
                new_salary = input('Введите новую заработную плату: ')
                lg.logging.info(f'User entered: {new_salary}')
                add.update(id=user_id, new_salary=new_salary)

            else:
                lg.logging.warning('User entered an invalid menu value')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 7:
            lg.logging.info('The user has selected item number 7')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по должность.')
            deleting = сheck_number(input('Введите номер пункта: '))

            if deleting == 1:
                lg.logging.info('The user has selected item number 7.1')
                search = input('Введите фамилию: ')
                lg.logging.info(f'User entered: {search}')
                base = add.retrive(surname=search)
                for lines in base:
                    for line in lines:
                        print(line, end=' ')
                    print()
                # print(*add.retrive(surname=search), sep='\n')
                user_id = input('Введите id записи: ')
                lg.logging.info(f'User entered: {user_id}')
                add.delete(id=user_id)

            elif deleting == 2:
                lg.logging.info('The user has selected item number 7.2')
                search = input('Введите должность: ')
                lg.logging.info(f'User entered: {search}')
                base = add.retrive(position=search)
                for lines in base:
                    for line in lines:
                        print(line, end=' ')
                    print()
                # print(*add.retrive(position=search), sep='\n')
                user_id = input('Введите id записи: ')
                lg.logging.info(f'User entered: {user_id}')
                add.delete(id=user_id)

            else:
                lg.logging.warning('User entered an invalid menu value')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 8:
            lg.logging.info('End')
            print('Спасибо за работу!')
            break

        else:
            lg.logging.warning('User entered an invalid menu value: {n}')
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def сheck_number(arg):
    while arg.isdigit() != True:
        lg.logging.warning(f'User entered an invalid menu value: {arg}')
        print('\nОшибка. Вы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)

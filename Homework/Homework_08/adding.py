import csv
import os.path
import logger as lg


db_file_name = ''
db = []
global_id = 0


def init_data_base(file_name='employees_base.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if (row[0] != 'ID'):
                    db.append(row)
                    if (int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(name='', surname='', number='', email='', salary='', position=''):
    global global_id
    global db
    global db_file_name
    if (name == ''):
        print("Внимание. Не введено ИМЯ.")
        return
    if (surname == ''):
        print("Внимание. Не введена ФАМИЛИЯ.")
        return
    if (number == ''):
        print("Внимание. Не введен НОМЕР ТЕЛЕФОНА.")
        return
    if (email == ''):
        print("Внимание. Не введен EMAIL.")
        return
    if (salary == ''):
        print("Внимание. Не введена ЗАРПЛАТА.")
        return
    if (position == ''):
        print("Внимание. Не введена ДОЛЖНОСТЬ.")
        return

    for row in db:
        if (row[1] == name.title() and row[2] == surname.title() and row[3] == number and row[4] == email.lower() and row[5] == salary and row[6] == position.lower()):
            print("ЗАПОЛНЕНО")
            return

    global_id += 1
    new_row = [str(global_id), name.title(),
               surname.title(), number, email.lower(), salary, position.lower()]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


def retrive(id='', name='', surname='', number='', email='', salary='', position=''):
    global global_id
    global db
    global db_file_name
    result = []

    for row in db:
        if (id != '' and row[0] != id):
            continue
        if (name != '' and row[1] != name.title()):
            continue
        if (surname != '' and row[2] != surname.title()):
            continue
        if (number != '' and row[3] != number):
            continue
        if (email != '' and row[4] != email.lower()):
            continue
        if (salary != '' and int(row[5]) < int(salary)):
            continue
        if (position != '' and row[6] != position):
            continue
        result.append(row)
    if len(result) == 0:
        return ('Контакты не найдены!')
    else:
        return result


def update(id='', new_name='', new_surname='', new_number='', new_email='', new_salary='', new_position=''):
    global global_id
    global db
    global db_file_name
    if (id == ''):
        print('Укажите id для внесения изменений')
        return
    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if (row[0] == id):
                if (new_name != ''):
                    row[1] = new_name.title()

                if (new_surname != ''):
                    row[2] = new_surname.title()

                if (new_number != ''):
                    row[3] = new_number

                if (new_email != ''):
                    row[4] = new_email.lower()

                if (new_salary != ''):
                    row[5] = new_salary

                if (new_position != ''):
                    row[6] = new_position.lower()

            writer.writerow(row)


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if (id == ''):
        print('Укажите id для удаления')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)

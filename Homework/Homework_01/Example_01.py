#1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input('Введите цифру '))

if number == 1:
    print('Понедельник')
if number == 2:
    print('Вторник')
if number == 3:
    print('Среда')
if number == 4:
    print('Четверг')
if number == 5:
    print('Пятница')
if number == 6:
    print('Суббота')
if number == 7:
    print('Воскресельнье')
elif number < 1 or number > 7:
    print('Ошибка')

#еще вариант

day_week = ['Понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
day = int(input('Введите день недели: '))

if day < 1 or day > 7:
    print('введите цифру от 1 до 7')
elif day == 6 or day == 7:
    print(day_week[day - 1], '- выходной!')
else:
    print(day_week[day - 1], '- рабочий день')    

# и еще

number = int(input('введите число: '))
if number in range(1, 6):
    print('нет')
elif number in range(6, 8):
    print('да')
else:
    print('введите число в диапазоне от 1 до 7')
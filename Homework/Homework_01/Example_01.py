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

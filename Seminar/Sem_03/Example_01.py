# Задайте список. Напишите прог-му, которая определит присутствует ли в заданном списке некое число

lst = ['1', '1', '2', '3', 'hfdt']
digit = input('введите число ')

for item in lst:
    if digit in item:
        print('присутствует')
        break
if digit != item:
    print('no')

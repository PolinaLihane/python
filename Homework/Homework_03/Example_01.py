# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from Example_01 import get_list
import random
lst = ['1', '3', '5', '8']
sum = 0

for i in range(len(lst)):
    if i % 2 == 0:
        sum += int(lst[i])

print(lst)
print(f' ответ: {sum}')

# решение с семинара


s = []
for i in range(int(input('Размер списка: '))):
    s.append(random.randint(-10, 10))

result = s[1::2]  # срез берем с первого до последнего с шагом 2
print(s)
print(
    f'элементы на нечетных позициях - {result}, сумма этих элементов = {sum(result)}')

# vможно создать отдельный файл для функций.


def get_list(mark=True):
    number_type = '' if mark else 'вещественных'
    input_lst = input(
        f'введите список из {number_type} чисел:\n'
    ).split()
    if mark:
        result_list = [int(i) for i in input_lst]
    else:
        result_list = [float(i) for i in input_lst]
    print(f'Список:\n{result_list}')
    return result_list


input_list = get_list()
print(f'сумма: '
      f'{sum(el for i, el in enumerate(input_list) if i % 2)}')

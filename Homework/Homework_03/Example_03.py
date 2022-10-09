# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части

lst = [1.1, 1.2, 3.1, 5, 10.01]

max = lst[0]
min = lst[1]

for item in lst:
     if item % 1 * 10 > max:
         max = item % 1 * 10
     elif item % 1 * 10 < min:
         min = item % 1 * 10

print(round((max - min) / 10, 2))

# решение с сем

n = int(input('размер'))
lst1 = []
lst = [float(input(f' введите {i} элемент списка ')) for i in range(n)]
for i in lst:
    lst1.append(i-int(i))

print(round((max(lst1)-min(lst1)),2))

# еще

import random
n = int(input('Введите количество элементов списка'))
list = []
for i in range(n):
    list.append(round(random.uniform(0, 10),2))

min = list[0]-int(list[0])
max = list[0]-int(list[0])
for item in list:
    if item-int(item) <= min:
        min = item-int(item)
    if item-int(item) >= max:
        max = item-int(item)

res = round(max-min,2)
print(f'В списке {list}, \nмакс и мин дробная часть {max} и {min}, их разница {res}')


# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random, numpy


n = int(input('Введите количество элементов списка'))
list = []
for i in range(n):
    list.append(random.randint(0, 10))

res = numpy.array(list)
unique_list = numpy.unique(res)
print(res)
print()
print(unique_list)
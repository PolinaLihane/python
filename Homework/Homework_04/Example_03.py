# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from collections import Counter
import random

import numpy


n = int(input('Введите количество элементов списка'))
list = []
for i in range(n):
    list.append(random.randint(0, 10))

res = NUMPY.array(list)
unique_list = NUMPY.unique(res)
print(res)
print()
print(unique_list)

# решение с сем


n = int(input('Введите количество элементов списка'))
lst = []
for i in range(n):
    lst.append(random.randint(0, 10))
print(lst)
newlst = []
for i in lst:
    if lst.count(i) < 2:
        newlst.append(i)
print(newlst)

#еще решение
data = []
for i in range(n):
    n = random.randint(1,10)
    data.append(n)

print(data)

newlist = []
data_count = dict(Counter(data))
print(data_count)
for d in data:
    if data_count[d] == 1:
        newlist.append(d)

print(newlist)
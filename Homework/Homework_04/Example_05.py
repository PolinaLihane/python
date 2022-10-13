# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

#import numpy as np
from sympy import Symbol, expand
import sympy


def read_file(file):
    with open(str(file)) as data:
        tmp = data.read()
    return tmp


file1 = 'Polynomial1.txt'
file2 = 'Polynomial2.txt'

poly1 = read_file(file1).replace(' = 0', '')  # читаем и убираем концовку
poly2 = read_file(file2).replace(' = 0', '')

my_poly1 = sympy.polys.polytools.poly_from_expr(poly1)[0]  #возвращает полигон
my_poly2 = sympy.polys.polytools.poly_from_expr(poly2)[0]

print(my_poly1, my_poly2)

polysum = my_poly1+my_poly2  # сложение полиномов
print(polysum.as_expr())
with open('Polynomial-sum.txt', 'w') as data:
    data.write(str(polysum.as_expr()).replace('**', '^')+' = 0')  # реплейс для красоты


# еще решение

def lineCountInFile(path):
    file = open(path, 'r')
    lines = 0
    for line in file:
        if line != "\n":
            lines += 1
    return lines


def mergeLinesInFles(path1, path2):
    if lineCountInFile(path1) != lineCountInFile(path2):
        print('The contents of the files do not match!')
        return
    poly1 = open(path1, 'r')
    poly2 = open(path2, 'r')
    with open('polySum.txt', 'w') as result:
        for i in range(lineCountInFile(path1)):
            result.write(poly1.readline().replace('=0\n', '+') +
                         poly2.readline())

    poly1.close()
    poly2.close()


path1 = 'poly1.txt'
path2 = 'poly2.txt'

mergeLinesInFles(path1, path2)
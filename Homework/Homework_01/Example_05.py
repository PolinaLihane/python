#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from math import sqrt

x1 = int(input('Введите координату x1 '))
x2 = int(input('Введите координату x2 '))
y1 = int(input('Введите координату y1 '))
y2 = int(input('Введите координату y2 '))
distance = ((x1 - y1) ** 2 + (x2 - y2) ** 2) ** (0.5)
print(format(distance, '.2f'))

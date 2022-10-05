#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 

number = int(input('Введите число: '))
sum = 0
while (number != 0):
    sum += int(number % 10)
    number = number / 10
print(sum)

#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input('Введите число: '))
sum = 1
for i in range(1,number + 1):
    sum = sum * i
    print((sum), end =', ')
print()
#3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

number = int(input('Введите число: '))
sum = 0
for i in range(1, number + 1):
    sum += (1 + 1 / i) ** i
print(sum)

#4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input('Введите число: '))
from random import randint
result = 1
ar = []
for i in range(number):
    ar.append(randint(-number,number))
f = open('1.txt', 'r')
for i in ar(number):
    if i == f.read():
        result = result * ar[i]
f.close()
print(result)

#5. Реализуйте алгоритм перемешивания списка.

import random
ar = [1,2,3]
random.shuffle(ar)
print(ar)

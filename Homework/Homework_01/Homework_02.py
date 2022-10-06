#  1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

import random
from random import randint
number = int(input('Введите число: '))
sum = 0
while (number != 0):
    sum += int(number % 10)
    number = number / 10
print(sum)

#  С семинара решение


def sum_digital_number(input_number):
    sum_digit = 0
    while input_number != 0:
        sum_digit += input_number % 10
        input_number //= 10
    return sum_digit


number = input('add digit: ')
number = number.replace('-', '').replace('.', '').replace(',', '')

if number.isdigit():
    sum_digits = sum_digital_number(int(number))
    print(f'sum = {sum_digits}')
else:
    print('Не допустимый ввод. Можно вводить только числа')

# еще решение

print(sum(int(i) for i in input('введите число') if i.isdigit()))

# еще решение

num = float(input('Введите число: '))
while int(num) != num:
    num *= 10

result = 0
while num:  # пока true. пока не 0
    result += num % 10
    num //= 10

print(result)

#  2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input('Введите число: '))
sum = 1
for i in range(1, number + 1):
    sum = sum * i
    print((sum), end=', ')
print()

#  решение с семенара


def factorial(input):
    f = 1
    for i in range(2, input + 1):
        f *= i
    return f


print([
    factorial(i) for i in range(1, int(input('N:')) + 1)
])

# рекурсия


def fib(N):
    if N == 1:
        return N

    return N * fib(N - 1)


N = int(input('N: '))
lst = []
for i in range(1, N + 1):
    lst.append(fib(i))

# еще решение


def fib(N):
    last = 1
    for i in range(1, N + 1):
        last *= i
        yield last  # возврат в точку вызова


N = int(input('N: '))
lst = list(fib(N))  # лист делает список
print(lst)

#  3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

number = int(input('Введите число: '))
sum = 0
for i in range(1, number + 1):
    sum += (1 + 1 / i) ** i
print(sum)

#  4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input('Введите число: '))
result = 1
ar = []
for i in range(number):
    ar.append(randint(-number, number))
f = open('1.txt', 'r')
for i in ar(number):
    if i == f.read():
        result = result * ar[i]
f.close()
print(result)

#  5. Реализуйте алгоритм перемешивания списка.

ar = [1, 2, 3]
random.shuffle(ar)
print(ar)

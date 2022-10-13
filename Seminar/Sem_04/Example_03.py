# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

from math import lcm, gcd
A = int(input('A: '))
B = int(input('B: '))

if A > B:
    Maxi = A
else:
    Maxi = B

while True:
    if not Maxi % A and not Maxi % B:
        print(Maxi)
        break
    Maxi += 1

# еще решение


a, b = tuple(map(int, input('введите числа через пробел: ').split()))
print(f'lcm = {lcm(a, b)}')

# еще вариант


a, b = tuple(map(int, input('введите числа через пробел: ').split()))
# если не добавлять директорию gcd то:
# def gcd(x, y):
#   if y > x:
#        x, y = y, x
#
#   if y ==0:
#       return x
#
#   return gcd(y, x  % y)

print(f'lcm = {a * b / (gcd(a, b))}')

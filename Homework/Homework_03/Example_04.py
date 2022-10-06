# 0Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def to_bin(N):
     if N == 0:
         print(N)
         return
     elif N != 1:
         to_bin(N // 2)
     print(N % 2, end = '')


N = int(input('введите число:'))
to_bin(N)

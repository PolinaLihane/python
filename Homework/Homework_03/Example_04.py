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

# еще решение

N = int(input('введите число'))
s = ''
while N > 0:
    s = str(N % 2) + s
    N = N // 2  # N >>= 1 битовый сдвиг вправо
print(s)

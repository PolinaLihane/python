# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def ne_fib(N):
     if N == 0 or N == 1:
         return N
     if N == -1:
         return not N
     if N < 0:
         return round(ne_fib(abs(N)) * (-1) ** (N + 1))
     else:
         return ne_fib(N - 1) + ne_fib(N - 2)


N = int(input('введите число: '))
print(ne_fib(N))

for i in range(-N, N + 1):
     print(ne_fib(i), end=' ')

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


#еще решение

def fib(n):
    if not n:
        return 0 # n
    if n < 0:
        return (-1) ** (-n + 1) * fib(-n)
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


neg_fib = []
for i in range(-N, N + 1):
    neg_fib.append(fib(i))

print(neg_fib)
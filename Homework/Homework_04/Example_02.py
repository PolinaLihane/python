# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


number = int(input("Введите N: "))

for i in range(2, int(number ** (1/2)) + 1):  #теория чисел. если число не простое то есть хотя бы 1 множитель который не может быть больше чем корень этого числа
    while (number % i == 0):
        print(i)
        number //= i

if (number != 1):
    print(number)


# еще решение

# проверка на простоту перебором
from math import factorial


def is_prime(N):
    if N in (2, 3):
        return True
    div = 3
    while div <= N ** (1 / 2):
        if N % div == 0:
            return False
        div += 1
    else:
        return True

# проверка на простоту перебором
def vilson(N):
    if (factorial(N - 1) + 1) % N == 0:
        return True
    return False

if __name__ == '__main__':
    N = int(input('Введите число: '))
    prime_div = []
    div = 2
while N != 1:
# print(N)
    if is_prime(div) and N % div == 0:
        prime_div.append(div)
        N //= div
        div = 2
    else:
        div += 1

print(prime_div)

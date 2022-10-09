# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python

import sympy
A = int(input('A: '))
B = int(input('B: '))
C = int(input('C: '))

D = B * B - 4 * A * C

x1 = (-B + D ** (1/2)) / (2 * A)
x2 = (-B - D ** (1/2)) / (2 * A)

print(f"Корни квадратного уровнения {A}*x^2 + {B}*x + {C} = 0: {x1}, {x2}")


x = sympy.Symbol('x')

print(sympy.solveset(1 * x ** 2 - 2 * x - 3, x))


import math

print("Ax² + Bx + C = 0")
a = float(input('Введите А: '))
b = float(input('Введите B: '))
c = float(input('Введите C: '))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
# %.2f" % после последнего % берем от значения последние 2 цифры

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
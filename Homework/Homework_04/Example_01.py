# Вычислить число c заданной точностью d

from decimal import Decimal

digit = Decimal(input('Введите число: '))
digit = digit.quantize(Decimal(input('Введите точность d:')))
print(digit)

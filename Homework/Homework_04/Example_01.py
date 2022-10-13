# Вычислить число c заданной точностью d

from decimal import Decimal

digit = Decimal(input('Введите число: '))
digit = digit.quantize(Decimal(input('Введите точность d: ')))
print(digit)

# с семинара
import math
from math import pi
d = input("Введите точность d: \n").count("0")  # считаем нули в строке
d = len(input("Введите точность d: \n").split(".")[1])  #сплит делит строку на части с разделением . лен считает длину строки во втором символе строки,тоесть после запятой
print(f"число с заданной точностью {d}={round(pi, d)}")
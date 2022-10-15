# написать программу сложения двух чисел

from re import X


x = 0
y = 0

def init(a, b):  # инициализатор данных
    global x
    global y
    x = a
    y = b

def do_it():
    return x * y
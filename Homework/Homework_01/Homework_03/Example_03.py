# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части

lst = [1.1, 1.2, 3.1, 5, 10.01]
difference = 0
max = lst[0]
min = lst[1]

for item in lst:
     if item % 1 * 10 > max:
         max = item % 1 * 10
     elif item % 1 * 10 < min:
         min = item % 1 * 10

difference = max - min
print(round(difference/10, 2))


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = [1, 3, 5, 8, 5]
sum = [0]

for i in range(len(lst) // 2):
     sum.append(int(lst[i]) * int(lst[len(lst) - i - 1]))
if not len(lst) % 2 == 0:
     sum.append(lst[len(lst)-len(lst) // 2 - 1] * 2)

sum.remove(0)
print(sum)


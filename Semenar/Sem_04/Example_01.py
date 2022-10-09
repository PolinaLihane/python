# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

string = "1 5 3  87 98"

# list меняет формат map/map перебирает строку
lst = list(map(float, string.split()))

print(f'{max(lst)}  {min(lst)}')  # мин и макс встроеные функции

line = '3, 5, 7, 4, 5'
list = []

for i in range(len(line)):
    if line[i] != ',' and line[i] != ' ':list.append(int(line[i]))

print(*list)
print(f'Min: {min(list)}')
print(f'Max: {max(list)}')
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = [1, 3, 5, 8, 5]
sum = [0]

for i in range(len(lst) // 2):
    sum.append(int(lst[i]) * int(lst[len(lst) - i - 1]))
if not len(lst) % 2 == 0:
    sum.append(lst[len(lst)-len(lst) // 2 - 1] * lst[len(lst)-len(lst) // 2 - 1])

sum.remove(0)
print(sum)


# решение с семинара

def fill_list():
    result = []
    while True:
        lst = input("введите элемент (нажмите 'Enter', что бы закончить): ")
        if lst.isdigit():
            result.append(int(lst))
        elif lst.replace(".", "", 1).isdigit():
            result.append(float(lst))
        elif lst:
            print("введено не число")
        if not lst:
            return result


print("Полученный список: ", lst2 := fill_list())

print("Произведение пар чисел: ", list(lst2[i] * lst2[-i-1] for i in range(len(lst2) // 2 + len(lst2) % 2)))


# еще одно // деление на цело

N = int(input('N: '))
lst = [randrange(N) for i in range(N)]
print(lst)

result = []
print(lst[:(N + 1) // 2], lst[N // 2:][::-1])
for el_1, el_2 in zip(lst[:(N + 1) // 2], lst[N // 2:][::-1]):result.append(el_1 * el_2)
print(result)


# еще

N = int(input('N: '))
lst = [randrange(N) for i in range(N)]
print(lst)
lst_copy = lst[:]  # копия списка
print([i*lst_copy.pop() for i in lst_copy])

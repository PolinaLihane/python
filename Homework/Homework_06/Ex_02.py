# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности, список повторяемых  и убрать дубликаты из заданной последовательности.


lst = [1, 2, 3, 5, 1, 5, 3, 10]

print(lst)
print(list(filter(lambda i: lst.count(i) < 2, lst)))
print(list(set(filter(lambda i: lst.count(i) >= 2, lst))))
print(list(set(lst)))

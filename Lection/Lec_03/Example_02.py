# в файле хранятся числаБ нужно выбрать четные и составить список пар число-квадрат

path ='/Users/golland/Desktop/git/Python/python/Lection/Lec_03/file.txt' 
f = open(path, 'r')
data = f.read() + ' '  # спецом добавляет пробел
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))  # от первого символа до пробела превращаем в число
    data = data[space_pos+1:]  # берем след эл

out = []
for e in numbers:
    if not e % 2:
        out.append((e,e ** 2))
print(out)

# c lambda

def select(f, col): # фильтр перем
    return [f(x) for x in col]

def where(f, col):  #тут условие
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15'.split()
data = select(int,data)
data = where(lambda x: not x % 2, data)
data = list(select(lambda x: (x, x**2), data))

# сокращяем еще

data = '1 2 3 5 8 15'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print(data)

# с фильтром


# Создайте программу для игры в "Крестики-нолики".

xo = (10060, 11093)
feild = [49, 50, 51, 52, 53, 54, 55, 56, 57]
wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def printField(feild):
    for i in range(len(feild)):
        if (i+1) % 3:
            print(' ', chr(feild[i]), end=' ')
        else:
            print(' ', chr(feild[i]), '\n')
    print("------------\n")


def getPos(a, b):
    pos = 0
    while True:
        pos = input('Введите значение: ')
        if (str(pos).isdigit() and a <= int(pos) <= b):
            break
    return int(pos)


def isEmpty(feild, pos):
    while True:
        if feild[pos-1] in xo:
            print("Клетка уже занята")
            return False
        return True


def isWin(feild):
    for i in wins:
        if feild[i[0]] == feild[i[1]] == feild[i[2]]:
            return True
    return False


print('Кто будет ходить первый?\n0->"x" 1->"0": ', end='')
move = getPos(0, 1)
while True:
    print(chr(xo[move % 2]))
    print('В какую клетку: ')
    printField(feild)
    pos = getPos(1, 9)
    if isEmpty(feild, pos):
        feild[pos-1] = xo[move % 2]
        printField(feild)
        move += 1
    else:
        continue
    if move > 4:
        if isWin(feild):
            printField(feild)
            move += 1
            print('Выиграл: ', chr(xo[move % 2]))
            break
    if move > 8:
        printField(feild)
        print('Ничья')
        break

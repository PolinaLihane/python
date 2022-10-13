# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import random


def isBot():
    choice = int(input(
        'Играем с ботом?\n0 - игрока № 2 - человек\n1 - игрока № 2 ботом\nВаш ответ:'))
    return bool(choice)


def coinToss():
    player = random.randint(1, 2)
    print('Бросаем монету...\nПервым ходит игрок №', player)
    return player


def userMove(player):
    while True:
        print('Ход игрока № ', player, ', конфет на столе:', count)
        candies = int(input('сколько конфет взять? '))
        if (min <= candies <= max and candies <= count):
            return candies
        else:
            print('Неверное количество конфет!')
            continue


def botMove(count, min, max):
    if count <= max:
        candies = count
    elif count > max:
        if count < max*2:
            candies = count-max-1
        else:
            while True:
                candies = random.randint(min, max)
                if candies % 2:
                    break
    else:
        while True:
            candies = random.randint(min, count)
            if candies % 2:
                break
    print('Ход игрока № 2, конфет на столе:', count,
          ',игрока № 2 берет ', candies, ' конф.')
    return candies


count = 2021
min = 1
max = 28
bot = isBot()
player = coinToss()
while count > 0:
    if (player == 1):
        candies = userMove(player)
    if (player == 2):
        if bot:
            candies = botMove(count, min, max)
        else:
            candies = userMove(player)
    count -= candies
    if (player == 1):
        player = 2
    else:
        player = 1
if (player == 2):
    print('Победил игрок №1')
else:
    print('Победил игрок №2')

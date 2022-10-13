# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

#from random import randint as r


#def formu(k):
 #   operator = ['-', '+']
 #   with open('in_1.txt', 'a', encoding='utf-8') as in_1:
 #       for i in range(k):
  #          coef = r(0, 10)
   #         oprIndx = r(0, 1)
   #         pow = k - i
   #         skip = False
    #        if coef != 0:
    #            in_1.write(str(coef))
    #            if pow > 1:
    #                in_1.write('*x^' + str(pow))
     #           if pow == 1:
     #               in_1.write('*x')
     #       if coef == 1:
      #          if pow > 1:
       #             in_1.write('x^' + str(pow))
       #         if pow == 1:
       #             in_1.write('x')
 #           if coef == 0:
 #               skip = True
  #          if not skip:
 #               in_1.write(str(operator[oprIndx]))
 #       in_1.write(str(r(0, 10)) + '=0\n')


#for i in range(2, 9):
#    formu(i)

# решение с сем
#import numpy as np
#from random import randint
#from sympy import Symbol, expand

#k = randint(2,5)


#def get_ratios(k):  # генерирует коэфиценты
#    ratios = [randint(0,100) for i in range(k +1)]
#    return ratios


#ratios = get_ratios(k)  # лист коэф
#ratios=[0,4,12]
#print(ratios)
#p = np.poly1d(ratios)  # преобразуем поли номер из коэф для красивой печати
#x = Symbol('x')  # символ для многочлена

#with open('in_1.txt', 'w')  as data:
#    data.write(str(expand(p(x))).replace('**', '^')+" = 0")  # ** изменить на ^

# еще решение
import os
from random import randint

k =int(input('введите степень k: '))
ratios = [randint(0,10) for i in range(k+1)]

print(ratios)  #коэф

terms =[]  # записываем сюда слогаемые
for ratio in ratios:
    if ratio:
        ratio =ratio if k == 0 else '' if ratio == 1 else ratio  # если коэф равен 0 то слогаемого не будет
        #power ="".join((indexes[ch] for ch in str(k)))  # красивая степень сверху
        power = 'x' if k == 1 else '' if k == 0 else f'x^{k}'  #тернарный опратор cktdf bcnbyjcnm
        term = f'{ratio}{power}'
        terms.append(term)

    k-= 1
polynom = ' + '.join(terms) + ' = 0'  # формируем полином
print(polynom)

result_dir ='file'  #имя директории

if not os.path.exists(result_dir):  # если директории нет то создать
    os.mkdir(result_dir)

with open(f'{result_dir}\\{"_".join(map(str, ratios))}.txt', 'w', encoding='utf-8') as file:  #
    file.write(polynom)


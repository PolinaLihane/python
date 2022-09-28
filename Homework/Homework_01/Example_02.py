#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите x '))
y = int(input('Введите y '))
z = int(input('Введите z '))

number1 = not(x or y or z)
number2 = not x and not y and not z
if number1 == number2:
    print(True)
else:
    print(False)
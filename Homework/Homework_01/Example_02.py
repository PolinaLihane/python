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

# решение с семенара

for x in 1, 0:
    for y in 1, 0:
        for z in 1,0:
            print(f"{x = } {y = } {z = }  {not(x or y or z) == (not x and not y and not z)}")

# решение с семенара

for x in range(2):
    for y in range(2):
        for z in  range(2):
            print(f"{x = } {y = } {z = }  {not(x or y or z) == (not x and not y and not z)}")

# от учителя

values = False, True
print(all(not(x or y or z) == (not x and not y and not z) for x in values for y in values for z in values))
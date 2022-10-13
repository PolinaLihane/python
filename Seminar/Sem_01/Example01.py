#1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.


a=int(input("Введите а"))
b=int(input("Введите в"))

if b==a**2: 
    print("да")
elif a==b**2:
     print("да")
else:
     print("no")


#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

a=int(input("Введите а"))
b=int(input("Введите b"))
c=int(input("Введите c"))
d=int(input("Введите d"))
f=int(input("Введите f"))
max=a

if b>max: 
    max=b
if c>max:
     max=c
if d>max:
     max=d
if f>max:
     max=f
print(max)
# еще решение
a=5
data=[]

for count in range(0,a):
    data.append(int(input("Input number")))

maxl=data[0]
for value in data:
    if value >maxl:
        maxl = value

print(maxl)

#3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

a=int(input("Введите а"))

for i in range(-a,a+1):
    print(i,end = ', ')

# print(*range(-a,a+1),sep = ', ')  # * распоковка элемента,в кот есть другие элементы
    
#4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

a=float(input("Введите а"))
if a - int(a) ==0:
    print('нет')
else:
    num=int((a-int(a))*10)
    print(num)

# ЕЩЕ решение
res=(a*10)%10
if res == 0:
    print("no")
else:
    print(int(res))

#5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

a=int(input("Введите а"))
if ((a % 5==0 and a % 10==0) or a % 15==0) and a % 30!=0:
    print("да")
else:
    print("no")

# еще решение
print(bool((a % 5==0 and a % 10==0) or a % 15==0) and a % 30!=0)
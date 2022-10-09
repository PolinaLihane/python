from cgi import print_environ


print('Hello World')

a=123
b=1.23
print(type(b)) #комент
print (a,b,s)
print(f'{a}-{b}-{s}')
print('{1}-{2}-{0}'.format(a,b,s ))
f=False
list=[] # список
a=int(input());
b=float(input());


a=1<2
print(a)

a=1<3<5<4
print(a)

f=1>2 or 4<6

f=[1,2,3,4]
print (not 2 in f)

is_odd=not f[0]%2==0 #нечетное?
print(is_odd)

for i in range(1,10,2): #от 1 до10 с шагом 2
    print(i)
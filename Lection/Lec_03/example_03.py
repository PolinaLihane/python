# map

li = [x for x in range(1,20)]

li = list(map(lambda x:x+10), li)

print(li)

data = list(map(int, input().split()))  # считываем с консоли строку и превращаем в число в список лист
print(data)

# filter

data = [x for x in range(10)]

res = list(filter(lambda x: x %2, data))
print(res)

# zip

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4,5,9,14,7]

data = list(zip(users,ids))
print(data)

# enumerate

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4,5,9,14,7]

data = list(enumerate(users))
print(data)
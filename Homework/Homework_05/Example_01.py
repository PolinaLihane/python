# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'ваб вба абв ваб бва абв'
print(text)


def del_some_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)


text = del_some_words(text)
print(text)

# еще  решение 

import re

s = "автобус аэробус машина зимбабве самозабвенный главрыба Напишите программу, удаляющую из текста все слова, содержащие"
#words = s.split()
words = re.split('\W+', s)  #'\W+' хоть сколько пробелов разделителем будут

ex = ["а", "б", "в"]

#for i in range(len(words)):
#    if words[i].find(ex[0]) != -1 and words[i].find(ex[1]) != -1 and words[i].find(ex[2]) != -1:
#        words[i] = None
# print (' '.join(words))
#words = [txt for txt in words if txt]
#print(*words)
for i in range(len(words)-1, -1, -1):
    if words[i].find(ex[0]) != -1 and words[i].find(ex[1]) != -1 and words[i].find(ex[2]) != -1:
        #print(words.pop(i))
        del words[i]
print(words)
# еще
text ='xnj nj yfgbcfyj'

print(' '.join(filter(lambda x: not any(True if char in x else False for char in 'абв'), text.split())))

#
print(*filter(lambda x: not set(x) >= (set('абв')), text.split()), sep=' ') # issuperset
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'ваб вба абв ваб бва абв'
print(text)


def del_some_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)


text = del_some_words(text)
print(text)

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст: ').split()
new_text = list(filter(
    lambda word: 'а' not in word and 'б' not in word and 'в' not in word, text))

print(new_text)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encoding(s):
    count = 1
    res = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            res = res + str(count) + s[i]
            count = 1
    if count > 1 or (s[len(s)-2] != s[-1]):
        res = res + str(count) + s[-1]
    return res


def decoding(s):
    number = ''
    res = ''
    for i in range(len(s)):
        if not s[i].isalpha():
            number += s[i]
        else:
            res = res + s[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодирования (RLE): ")
print(f"Текст после кодировки: {encoding(s)}")
print(f"Текст после дешифровки: {decoding(encoding(s))}")

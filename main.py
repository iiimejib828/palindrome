'''
Проверяем, является ли введённая строка палиндромом
Алгоритм 1: Сравнить перевёрнутую строку с исходной и вернуть результат сравнения.
Алгоритм 2: Вычилить длину строки
            В цикле сравнить символы строки от начала до целой части половины длины строки
            с симметрично расположенными символами из хвоста строки. В случае несовпадения 
            немедленно возвращаем False, если несовпадений не найдено, возвращаем True.
'''

def is_palindrome_1(test_string):
    return test_string == test_string[::-1]

def is_palindrome_2(test_string):
    test_string_len = len(test_string)
    for i in range(test_string_len // 2):
        if test_string[i] != test_string[test_string_len-i-1]:
            return False

    return True

prev_str = "Start"
cur_str = 'Start'

while cur_str + prev_str != '':
    prev_str = cur_str
    cur_str = input('Введите строку для проверки. Для выхода два раза подряд введите пустую строку:\n')
    if cur_str != '':
        if is_palindrome_1(cur_str):
            print('Алгоритм 1: Палиндром')
        else:
            print('Алгоритм 1: Не палиндром')
        if is_palindrome_2(cur_str):
            print('Алгоритм 2: Палиндром')
        else:
            print('Алгоритм 2: Не палиндром')

print('До следующей встречи!')

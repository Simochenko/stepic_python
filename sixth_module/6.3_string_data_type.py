# s = input()  # переменная s имеет строковый тип str

# Длина строки
# Длиной строки называется количество символов из которых она состоит. Чтобы посчитать длину строки используем встроенную функцию len() (от слова length – длина).
#
# Следующий программный код:

# s1 = 'abcdef'
# length1 = len(s1)               # считаем длину строки из переменной s1
# length2 = len('Python rocks!')  # считаем длину строкового литерала
# print(length1)
# print(length2)
#
# Преобразование чисел в строку
# Для преобразования строки к числу мы использовали функции int() и float(). Для обратного преобразования, то есть из числа в строку мы используем функцию str():
#
# Рассмотрим следующий программный код:
#
# num1 = 1777    # целое число
# num2 = 17.77   # число с плавающей точкой
# s1 = str(num1) # преобразовали целое число в строку '1777'
# s2 = str(num2) # преобразовали число с плавающей точкой в строку '17.77'
# print(s1)
# С помощью конкатенации строк можно эмулировать вывод данных, который раньше мы делали используя необязательные параметры sep и end. Следующие две строки кода делают одно
# и тоже:
#
# print('a', 'b', 'c', sep='*', end='!')
# print()  # переход на новую строку
# print('a' + '*' + 'b' + '*' + 'c' + '!')

# В Python так же можно умножать строку на число. Такой оператор повторяет строку указанное количество раз.
#
# Рассмотрим следующий программный код:
#
# s = 'Hi' * 4
# print(s)
# Результатом выполнения такого кода будет:
#
# HiHiHiHi
#
# print('-' * 175)

# Строку можно умножать на число, но нельзя умножать на строку.

# Примечание 1. Тройные кавычки в Python используются для многострочного (multiline) текста. Например,

text = '''Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python design 
philosophy emphasizes code readability with its notable use of significant whitespace.'''

# mystr = 'да'
# mystr = mystr + 'нет'
# mystr = mystr + 'да'
# print(mystr)
#
# str1 = '1'
# str2 = str1 + '2' + str1
# str3 = str2 + '3' + str2
# str4 = str3 + '4' + str3
# print(str4)
#
# mystr = '123' * 3 + '456' * 2 + '789' * 1
# print(mystr)
#
# a = '"Python is a great language!", '
# b = 'said Fred. '
# c = '"I don\'t ever remember having this much fun before."'
# print(a + b + c)

'''Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:

«Hello [введенное имя] [введенная фамилия]! You just delved into Python».

Формат входных данных
На вход программе подаётся две строки (имя и фамилия), каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.'''
# a = input()
# b = input()
# print('Hello '+ a + ' '+ b + '! You just delved into Python')

'''Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:

«Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

Формат входных данных
На вход программе подаётся строка – название футбольной команды.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.'''
# k = input()
# L = str(len(k))
# print('Футбольная команда ' + k + ' имеет длину ' + L + ' символов')

'''Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
Примечание. Гарантируется, что длины названий всех трех городов различны.'''

# a = input()
# b = input()
# c = input()
# Lmin = min(a, b, c, key=len)
# Lmax = max(a, b, c, key=len)
# print(Lmin)
# print(Lmax)

'''Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.
Формат выходных данных
Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.'''
# a = len(input())
# b = len(input())
# c = len(input())
# Lmin = min(a, b, c)
# Lmax = max(a, b, c)
# Ls = a + b + c - Lmax - Lmin
# if (Lmax - Ls) == (Ls - Lmin):
#     print('YES')
# else:
#     print('NO')
#
'''Оператор in
В Python есть специальный оператор in, который позволяет проверить, что одна строка находится внутри другой.

Рассмотрим следующий код:

s = input()
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а')
Такой код проверяет, содержится ли в переменной s символ a и выводит соответствующий текст.

Мы можем использовать оператор in вместе с логическим оператором not. Например

s = input()
if '.' not in s:
    print('Введенная строка не содержит символа точки')
С помощью оператора in мы можем упростить следующий код, проверяющий, что в переменной s находится один из 5 символов a, e, i, o, u:

if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    print('YES')
до вида:

if len(s) == 1 and s in 'aeiou':
    print('YES')
Примечания
Примечание. Если строка s1 содержится в строке s2, то говорят, что строка s1 является подстрокой для строки s2. Другими словами, оператор in определяет является
 ли одна строка подстрокой другой.'''

'''Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.'''
#
# s = input()
# if 'синий' in s:
#     print('YES')
# else:
#     print('NO')
'''Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
Формат входных данных
На вход программе подается одна строка.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.'''
# s = input()
# if ('суббота' in s) or ('воскресенье' in s):
#     print('YES')
# else:
#     print('NO')
'''Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.

Формат входных данных
На вход программе подаётся одна строка – email адрес.

Формат выходных данных
Программа должна вывести строку «YES», если email адрес является корректным и «NO» в ином случае.

Примечание. Наличие символов @ и . недостаточно для корректности email адреса, однако их отсутствие гарантировано влечёт за собой неверный email.'''
s = input()
if ('@' in s) and ('.' in s):
    print('YES')
else:
    print('NO')
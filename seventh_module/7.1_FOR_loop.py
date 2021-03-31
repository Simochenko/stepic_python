"""Рассмотрим код, который распечатает 10 раз слово "Привет":"""

# for i in range(10):
#     print('Привет')
#
# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# print('A')
# print('B')
# for i in range(5):
#     print('C')
#     print('D')
# print('E')
'''Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.
Формат входных данных
Формат выходных данных
Программа должна вывести 10 раз текст «Python is awesome!», каждый на отдельной строке.'''
# for i in range(10):
#     print('Python is awesome!')
'''Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.
Формат входных данных
В первой строке записано текстовое предложение, во второй — количество повторений.
Формат выходных данных
Программа должна вывести указанное текстовое предложение нужное количество раз. Каждое повторение должно начинаться с новой строки.'''
# a = input()
# b = int(input())
# for i in range(b):
#     print(a)
'''Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:'''
# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')
'''На вход программе подается натуральное число n.
Напишите программу, которая печатает звездный прямоугольник размерами n×19.
Формат входных данных
На вход программе подаётся натуральное число n∈[1;20] — высота звездного прямоугольника.
Формат выходных данных
Программа должна вывести звездный прямоугольник размерами n×19.
Подсказка. Для печати звездной линии используйте умножение строки на число.'''

# n = int(input())
# for i in range(n):
#     print('*' * 19)
# for i in range(10):
#     print(i)

'''Если переменная цикла не используется в теле цикла, то указывайте вместо нее символ нижнего подчеркивания'''

'''Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9, каждая с указанной строкой текста.

Формат входных данных
На вход программе подается одна строка текста.

Формат выходных данных
Программа должна вывести десять строк в соответствии с условием задачи.'''
# n = input()
# for i in range(10):
#     print(str(i) + ' ' + n)
'''На вход программе подается натуральное число nn. Напишите программу, которая для каждого из чисел от 00 до nn (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).
Формат входных данных
На вход программе подается натуральное число nn.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.'''
# n = int(input())
# for (i) in range(n + 1):
#     print('Квадрат числа ' + str(i) + ' равен ' + str(i * i))

'''На вход программе подается натуральное число n≥2 – катет прямоугольного равнобедренного треугольника.
Напишите программу, которая выводит звездный треугольник в соответствии с примером.
Формат входных данных
На вход программе подается одно натуральное число n≥2.
Формат выходных данных
Программа должна вывести треугольник в соответствии с условием задачи.'''
# n = int(input())
# for i in range(n):
#     print('*' * (n-i))
'''На вход программе подается три натуральных числа m, p,n:

m: стартовое количество организмов;
p: среднесуточное увеличение в %;
n: количество дней для размножения.
Напишите программу, которая предсказывает размер популяции организмов. Программа должна выводить размер популяции в каждый день, начиная с 11 и заканчивая n-м днем.

Формат входных данных
На вход программе подается три натуральных числа.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.'''

# m, p, n = float(input()), float(input()), int(input())
# [print(i + 1, m * (1 + p / 100) ** i) for i in range(n)]
m, p, n = int(input()), int(input()), int(input())
for i in range(1, n + 1):
    print(i, float(m))
    m += m * (p / 100)
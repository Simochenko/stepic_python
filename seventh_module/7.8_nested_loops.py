'''Вложенные циклы
Вложенный цикл расположен в еще одном цикле. Часы служат хорошим примером работы вложенного цикла. Секундная, минутная
 и часовая стрелки вращаются вокруг циферблата.Часовая стрелка смещается всего на 1 шаг для каждых 60 шагов минутной
  стрелки. И секундная стрелка должна сделать 60 шагов для 1 шага минутной стрелки. Это означает, что для каждого
  полного оборота часовой стрелки (12 шагов), минутная стрелка делает 720 шагов.'''
'''Рассмотрим цикл, который частично моделирует электронные часы. Он показывает секунды от 0 до 59:'''
# for seconds in range(60):
#     print(seconds)
'''Можно добавить переменную minutes и вложить цикл написанный выше внутрь еще одного цикла, который повторяется
 60 раз:'''
# for minutes in range(60):
#     for seconds in range(60):
#         print(minutes, ':', seconds)
#
'''Для того, чтобы сделать модель законченной, можно добавить еще одну переменную для подсчета часов:'''
# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)
'''Самый внутренний цикл сделает 60 итераций для каждой итерации среднего цикла. Средний цикл сделает 60 итераций для 
каждой итерации самого внешнего цикла. Когда самый внешний цикл сделает 24 итерации,
 средний сделает 24⋅60=1440 итераций, и самый внутренний цикл сделает 24⋅60⋅60=86400 итераций!

Пример имитационной модели часов подводит нас к нескольким моментам, имеющим отношение к вложенным циклам:

вложенный цикл выполняет все свои итерации для каждой отдельной итерации внешнего цикла;
вложенные циклы завершают свои итерации быстрее, чем внешние циклы;
для того, чтобы получить общее количество итераций вложенного цикла, надо перемножить количество итераций всех циклов.
    Мы можем вкладывать друг в друга циклы как for, так и while.'''

'''Оператор break выполняет прерывание ближайшего цикла в котором он расположен. Аналогично, оператор continue 
осуществляет переход на следующую итерацию ближайшего цикла.

Рассмотрим программный код:

for i in range(3):
    for j in range(3):
        print(i, j)
Результатом его выполнения будут 9 строк:

0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
Изменим код, добавив во вложенный цикл условный оператор с оператором break:

for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)
Результатом выполнения нового кода будут 3 строки:

1 0
2 0
2 1
Изменим оператор прерывания break на оператор continue:

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)
Результатом выполнения нового кода будут 6 строк:

0 1
0 2
1 0
1 2
2 0
2 1'''

'''Для того чтобы завершить весь вывод таблицы звездочек, нам нужно выполнить этот цикл восемь раз. Мы можем поместить 
этот цикл в еще один цикл, который делает восемь итераций, как показано ниже:
'''
# for i in range(8):
#     for j in range(6):
#         print('*', end='')
#     print()
'''Внешний цикл делает восемь итераций. Во время каждой итерации этого цикла внутренний цикл делает 6 итераций. 
(Обратите внимание, что в строке 4 после того, как все строки были напечатаны, мы вызываем функцию print().
 Мы должны это сделать, чтобы в конце каждой строки продвинуть экранный курсор на следующую строку. Без этой 
 инструкции все звездочки
будут напечатаны на экране в виде одной длинной строки.)
Давайте рассмотрим еще один пример. Предположим, что вы хотите напечатать звездочки в комбинации, которая похожа на 
приведенный ниже звездный треугольник:'''
'''Представим эту комбинацию звездочек, как сочетание строк и столбцов. В этой комбинации всего восемь строк. 
В первой строке один столбец. Во второй строке – два столбца. В третьей строке – три. И так продолжается до восьмой
 строки, в которой восемь столбцов.'''
# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)
''' 8 '''
'''Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n ×3 состоящую из 
данного числа (числа отделены одним пробелом).
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести таблицу размером n×3 состоящую из данного числа.
Примечание. В конце строки может быть пробел.'''

# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()
'''Таблица-2
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×5, где в i-ой 
строке указано число i (числа отделены одним пробелом).
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести таблицу размером n ×5 в соответствии с условием.
Примечание. В конце строки может быть пробел.'''
# n = int(input())
# for i in range(n):
#     for j in range(5):
#         print(i + 1, end=' ')
#     print()
'''Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу сложения для всех 
чисел от 1 до n в соответствии с примером.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести таблицу сложения для всех чисел от 1 до n.
Примечание. В конце строки может быть пробел.'''
#
# n = int(input())
# for i in range(1, n // 2 + 2):
#     print('*' * i, end='')
#     print()
# for i in range(n // 2, 0, -1):
#     print('*' * i, end='')
#     print()
#
# n = int(input())
# for i in range(1, n + 1):
#     print('*' * min(i, n - i + 1))
#
#
# n = int(input())
#
# for i in range(n):
#     k = (n // 2 + 1) - abs(n // 2 - i)
#     for _ in range(k):
#         print('*', end='')
#     print()
#
# n = int(input())
# count = 0
# step = 1
# for _ in range( n):
#     if count == n//2 + 1:
#         step = -1
#     count += step
#     print('*' * count)
'''Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:

1
22
333
4444
55555
...
Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести треугольник в соответствии с условием.

Примечание. Используйте вложенный цикл for.'''
# n = int(input())
# for i in range(n):
#     for j in range(i + 1):
#         print(i+1, end='')
#     print()

'''Использование вложенных циклов при решении уравнений
Вложенные циклы можно использовать для решения уравнений с несколькими переменными. Зная, что решения (корни) уравнения 
являются натуральными (целыми) числами, несложно написать программу, содержащую вложенный цикл и перебирающую все 
возможные значения переменных.

Решение задач
Задача 1. Найдите все пары натуральных чисел (и их количество) являющихся решением уравнения 12x+13y =777.

Решение. Поскольку по условию числа xx и yy являются натуральными, то x≤64,y≤59 . Напишем
 программу, которая перебирает всевозможные пары чисел (x;y) и проверяет для них выполнение условия
  12x+13y = 777'''

# total = 0
# for x in range(1, 65):
#     for y in range(1, 60):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print('x =', x, 'y =', y)
# print('Общее количество натуральных решений =', total)
'''Задача 2. Найдите все пары натуральных чисел (и их количество) являющихся решением уравнения x^2+y^2+z^2 = 2020
'''
# total = 0
# for x in range(1, 45):
#     for y in range(1, 45):
#         for z in range(1, 45):
#             if x ** 2 + y ** 2 + z ** 2 == 2020:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)

'''12 месяцев
Решите уравнение в натуральных числах 28n + 30 k + 31 m = 36528n+30k+31m=365.

Примечание. Используйте вложенный цикл for. В первую очередь запишите решение с наименьшим значением nn.'''
# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28 * n + 30 * k + m * 31 == 365:
#                 print('n =', n, 'k =', k, 'm =', m)

# for B in range(1, 11):
#     for K in range(1, 21):
#         for T in range(1, 201):
#             if (10 * B + 5 * K + 0.5 * T == 100) and (B + K + T == 100):
#                 print('B =', B, 'K =', K, 'T =', T)

'''Гипотеза Эйлера о сумме степеней
В 1769 году Леонард Эйлер сформулировал обобщенную версию Великой теоремы Ферма, предполагая, что по крайней мере n 
энных степеней необходимо для получения суммы, которая сама является энной степенью для n>2. Напишите программу для 
опровержения гипотезы Эйлера (продержавшейся до 1967 года), и найдите четыре положительных целых числа, сумма 5-х 
степеней которых равна 5-й степени другого положительного целого числа.

Таким образом, найдите пять натуральных чисел a,b,c,d,e удовлетворяющих условию:
a^5+b^5+c^5+d^5=e^5.
В ответе укажите сумму a+b+c+d+e.

Примечание 1. Используйте вложенный цикл for.

Примечание 2. Считайте, что числа a, b, c, d,  не превосходят 150.

Примечание 3. Программа может работать дольше чем обычно. В зависимости от способа решения задачи на выполнение 
программы может уходить до нескольких минут. Попробуйте сократить количество вложенных циклов. '''

# for a in range(1, 151):
#     for b in range(a + 1, 151):
#         for c in range(b + 1, 151):
#             for d in range(c + 1, 151):
#                 e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
#                 if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
#                     print(a + b + c + d + e)
'''Численный треугольник 4
Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии 
с примером:'''

# total = 0
# n = int(input())
# for i in range(n):
#     for j in range(i):
#         print(i, end=' ')
#     print()
# n = int(input())
# t = 1
# for i in range(1, n + 1):
#     k = 0
#     for j in range(1, t + 1):
#         if j <= i:
#             k = k + 1
#         else:
#             k = k - 1
#         print(k, end='')
#     print()
#     t += 2
'''На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит натуральное 
число из отрезка [a; b] с максимальной суммой делителей.'''

# a, b = int(input()), int(input())
# t_maximum = 0
# digit = 0
# for i in range(a, b + 1):
#     maxi = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             maxi += j
#         if maxi > t_maximum:
#             t_maximum = maxi
#             digit = j
# print(digit, t_maximum)
# a, b = int(input()), int(input())
# counter = 0 # счетчик подсчета суммы делителей
# number = 1 # число которое будем выводить (минимум 1)
# summa = 0  # тут будет сумма делителей, которую надо будет вывести
# for i in range(a, b + 1):  # проверяем каждое число в [a;b]
#     counter = 0 # обнуляем счетчик для каждого i
#     for j in range(1, i + 1):  # берем по очереди каждый делитель числа от [1 до самого числа]
#         if i % j == 0:  # если число делится на j без остатка, значит j - делитель числа
#             counter += j  # создаем сумму делителей
#     if counter >= summa:  # если сумма делителей больше или равна, чем суммаа делителей предыдущего числа
#         summa = counter  # то counter теперь равно кол-ву делителей этого числа вместо кол-ва предыдущего
#         number = i  # число у которого делителей оказалось больше, теперь равно number
# print(number, summa) # в конце концов, выводим само число (у которого больше делителей) и сумму этих делителей
'''Делители-2
На вход программе подается натуральное число nn. Напишите программу, выводящую графическое изображение делимости чисел
 от 1 до n включительно. В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у 
 этого числа.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести графическое изображение чисел от 1 до n, каждое на отдельной строке.
Sample Input:
5
Sample Output:
1+
2++
3++
4+++
5++'''
# n = int(input())
# for x in range(1, n + 1):
#     count = 0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             count += 1
#     print(x, '+' * count, sep='')
'''Цифровой корень
На вход программе подается натуральное число nn. Напишите программу, которая находит цифровой корень данного числа. 
Цифровой корень числа nn получается следующим образом: если сложить все цифры этого числа, затем все цифры найденной
 суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра), которое и называется 
 цифровым корнем данного числа.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести цифровой корень введенного числа.
Примечание. Используйте вложенные циклы while.'''
# num = int(input())
# while num > 9:
#     Sum = 0
#     while num > 0:
#         last_digit = num % 10
#         Sum += last_digit
#         num //= 10
#     else:
#         num = Sum
# print(num)

'''Сумма факториалов
Дано натуральное число n. Напишите программу, которая выводит значение суммы 1!+2!+3!+…+n!.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значение суммы 1!+2!+3!+…+n!.
Примечание 1. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 1 до n, то есть
n!=1⋅2⋅3⋅…⋅n
Примечание 2. Задачу можно решить без вложенного цикла. Напишите две версии программы =)
Sample Input:
3
Sample Output:
9'''
# n = int(input())
# fak = 1
# SumFak = 0
# for i in range(1, n+1):
#     fak *= i
#     SumFak += fak
# print(SumFak)


# for num in range(a, b + 1):
#     prime = True
#     for i in range(a, num):
#         if (num % i == 0) and (num > 1):
#             prime = False
#     if prime:
#         print(num)
'''Простые числа
На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит все простые 
числа от a до b включительно.
Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести все простые числа от aa до bb включительно, каждое на отдельной строке.
Примечание. Число 1 простым не является.
Sample Input 1:
2
15
Sample Output 1:
2
3
5
7
11
13
Sample Input 2:
1
5
Sample Output 2:
2
3
5'''
# a = int(input())
# b = int(input())
# for num in range(a, b+1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
# for i in range(10, 5, -1):
#     print(i)

# for i in range(10, 25):
#     print('Python awesome!')
# n = int(input())
# counter = 0
#
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 7 != 0:
#         counter += 1
# print(counter)
# i = 4
# while i <= 10:
#     print ('Python!')
#     i += 1
# n = int(input())
# res = 1
# i = 2
# while i <= n:
#     res *= i
#     i += 1
# print(res)
#
# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# print(i)
'''Ревью кода - 7 🌶️
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран сумму чётных цифр этого 
числа или 0, если чётных цифр в записи нет. Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только 
одну строку и может быть исправлена без изменения других строк.

Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно,
 использующую другой алгоритм решения.'''
# n = int(input())
# s = 0
# while n > 10:
#     if n % 2 == 0:
#         s = s + n
#         n //= 10
#     print(s)
'''Ревью кода - 8 🌶️
На обработку поступает последовательность из 8 целых чисел. Известно, что вводимые числа по абсолютной величине не 
превышают 10^6 
 . Нужно написать программу, которая выводит на экран количество делящихся нацело на 4 чисел в исходной 
 последовательности и максимальное делящееся нацело на 4 число. Если делящихся нацело на 4 чисел нет, требуется на
  экран вывести «NO». Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только 
одну строку и может быть исправлена без изменения других строк.
Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно, 
использующую другой алгоритм решения.'''
# n = 8
# count = 0
# maximum = -10**6 -1
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')
'''Ревью кода - 9
На обработку поступает последовательность из 4 целых чисел. Известно, что вводимые числа по абсолютной величине не 
превышают 10^6
 . Нужно написать программу, которая выводит на экран количество нечётных чисел в исходной последовательности и 
 максимальное нечётное число. Если нечётных чисел нет, требуется на экран вывести «NO». Программист торопился и 
 написал программу неправильно.
Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только 
одну строку и может быть исправлена без изменения других строк.
Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно,
 использующую другой алгоритм решения.'''
# n = 4
# count = 0
# maximum = -10**6 - 1
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

'''Звездная рамка
На вход программе подается натуральное число n. Напишите программу, которая печатает звездную рамку размерами n×19.
Формат входных данных
На вход программе подаётся натуральное число n∈[3;19] — высота звездной рамки.
Формат выходных данных
Программа должна вывести звездную рамку размерами n×19.
Подсказка. Для печати зведной линии используйте умножение строки на число.'''
# n = int(input())
# for i in range(n):
#     if i in (0, n - 1):
#         print('*' * 19)
#     else:
#         print('*'.ljust(18) + '*')
# n = int(input())
# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print('*' * 19)
#     else:
#         print('*' + ' ' * 17 + '*')
'''Все вместе 2
Дано натуральное число. Напишите программу, которая вычисляет:

количество цифр 3 в нем;
сколько раз в нем встречается последняя цифра;
количество четных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
Формат входных данных 
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.'''
# a = int(input())
# c = 0
# f = 0
# d = a % 10
# g = 0
# h = 0
# k = 1
# o = 0
# while a != 0:
#     b = a % 10
#     if a % 10 == d:
#         f += 1
#         d = b
#     if b == 3:
#         c = c + 1
#     if b % 2 == 0:
#         g += 1
#     if b > 5:
#         h += b
#     if b > 7:
#         k = k * b
#     if (b == 0) or b == 5:
#         o += 1
#     a = a // 10
# print(c)
# print(f)
# print(g)
# print(h)
# if k == 0:
#     print(1)
# else:
#     print(k)
# print(o)

'''Третья цифра
Дано натуральное число n(n>99). Напишите программу, которая определяет его третью (с начала) цифру.
Формат входных данных 
На вход программе подается одно натуральное число, состоящее как минимум из трех цифр.
Формат выходных данных
Программа должна вывести его третью (с начала) цифру.'''
# a = (input())
# print(a[2])
# n = int(input())
# while n >= 100:
#     s = n % 10
#     n //=10
# print(s)

'''Числа Рамануджана 🌶️
Сриниваса Рамануджан – индийский математик, славившийся своей интуицией в области чисел. Когда английский математик 
Годфри Харди навестил его однажды в больнице, он обмолвился, что номером такси, на котором он приехал, было 1729, 
такое скучное и заурядное число. На что Рамануджан ответил: "Нет, нет! Это очень интересное число. Это наименьшее 
число, выражаемое как сумма двух кубов двумя разными способами". Другими словами:
1729 = 1^3 + 12^3 = 9^3 + 10^3.
Напишите программу, которая находит аналогичные интересные числа. В ответе запишите первые 5 чисел в порядке 
возрастания, включая число 1729.
Примечание. Используйте вложенный цикл.'''
'''
1729
4104
13832
20683
32832'''
'''Двоеточие (:) в конце строки с инструкцией while сообщает Python, что дальше находится блок команд. В блок входят
все строки, расположенные с отступом от строки с инструкцией while, вплоть до следующей строки без отступа.
Блок команд, который выполняется в цикле while, называется телом цикла.
Рассмотрим код, использующий цикл while, который распечатает 10 раз слово Привет:'''
# i = 0
# while i < 10:
#     print('Привет')
#     i += 1
'''Напишем программу, которая считывает числа и выводит их квадраты, пока не будет введено -1. При такой постановке 
задачи мы не можем воспользоваться циклом for, так как не знаем сколько чисел будет предшествовать числу -1.'''

# num = int(input())
# while num != -1:
#     print('Квадрат вашего числа равен:', num * num)
#     num = int(input())
'''Цикл for VS цикл while
Мы всегда можем заменить цикл for с помощью цикла while. Следующие две программы выводят числа от 0 до 100:'''
# # используем for
# for i in range(101):
#     print(i)
#
# # используем while
# i = 0
# while i < 101:
#     print(i)
#     i += 1

'''Напишем программу, выводящую все числа, кратные 3, используя цикл for и while:'''
# # используем for
# for i in range(0, 100, 3):
#     print(i)
#
# # используем while
# i = 0
# while i < 100:
#     print(i)
#     i += 3
'''Считывание данных до стоп значения
Часто при решении задач на цикл while, мы считываем данные, до тех пор пока пользователь не введет некоторое значение, 
которое называют стоп значением. Напишем программу, которая считывает числа и находит их сумму, до тех пор пока 
пользователь не введет слово stop:'''
# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print('Сумма чисел равна', total)
'''Пример бесконечного цикла:'''
# i = 0
# total = 0
# while i < 10:
#     total += i
# while True:
#     print('Спасибо за курс \ (•◡•) /')
# count = 10
# while count < 1:
#     print('Python awesome!')
# count = 1
# while count < 10:
#     print('Python awesome!')
#     count += 1
#
# count = 1
# while count < 10:
#     print('Python awesome!')
# i = 5
# while i <= 11:
#     print('Python awesome!')
#     i += 1
# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)

'''До КОНЦА 1
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является
 слово «КОНЕЦ» (без кавычек). Напишите программу, которая выводит члены данной последовательности.
Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.
Формат выходных данных
Программа должна вывести члены данной последовательности.'''
# text = input()
# while text != 'КОНЕЦ':
#     print(text)
#     text = input()
'''До КОНЦА 2
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является
 слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек). Напишите программу, которая выводит члены 
 данной последовательности.
Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.
Формат выходных данных
Программа должна вывести члены данной последовательности.'''
# text = input()
# while (text != 'КОНЕЦ') and (text != 'конец'):
#     print(text)
#     text = input()
'''Количество членов
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности 
является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). Напишите программу,
 которая выводит общее количество членов данной последовательности.
Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.
Формат выходных данных
Программа должна вывести общее количество членов данной последовательности.'''
# text = input()
# total = 0
# while (text != 'стоп') and (text != 'хватит') and (text != 'достаточно'):
#     num = text
#     total += 1
#     text = input()
# print(total)
'''Пока делимся
На вход программе подается последовательность целых чисел делящихся на 7, каждое число на отдельной строке. Концом 
последовательности является любое число не делящееся на 7. Напишите программу, которая выводит члены данной 
последовательности.
Формат входных данных
На вход программе подается последовательность чисел, каждое число на отдельной строке.
Формат выходных данных
Программа должна вывести члены данной последовательности.'''
# n = int(input())
# while n % 7 == 0:
#     print(n)
#     n = int(input())
'''Сумма чисел
На вход программе подается последовательность целых чисел, каждое число на отдельной строке. Концом последовательности является любое отрицательное число. Напишите программу, которая выводит сумму всех членов данной последовательности.
Формат входных данных
На вход программе подается последовательность чисел, каждое число на отдельной строке.
Формат выходных данных
Программа должна вывести сумму членов данной последовательности.'''
# count = 0
# n = int(input())
# while n > 0:
#     count += n
#     n = int(input())
# print(count)

'''Количество пятерок
На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число
 на отдельной строке. Концом последовательности является любое отрицательное число, либо число большее 5. Напишите 
 программу, которая выводит количество пятерок.
Формат входных данных
На вход программе подается последовательность чисел, каждое число на отдельной строке.
Формат выходных данных
Программа должна вывести количество пятерок.'''

# n = int(input())
# count = 0
# while 6 > n > 0:
#     if n == 5:
#         count += 1
#     n = int(input())
# print(count)
'''Ведьмаку заплатите чеканной монетой
Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, к тому же ведьмак не 
принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 
1, 5, 10,25.
Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
Формат входных данных 
На вход программе подается одно натуральное число, цена за услугу ведьмака.
Формат выходных данных
Программа должна вывести минимально возможное количество чеканных монет для оплаты.'''
# n = int(input())
# count = 0
# while n >= 25:
#     n -= 25
#     count += 1
# while n >= 10:
#     n -= 10
#     count += 1
# while n >= 5:
#     n -= 5
#     count += 1
# while n >= 1:
#     n -= 1
#     count += 1
# print(count)

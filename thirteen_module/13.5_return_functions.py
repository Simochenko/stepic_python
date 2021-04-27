'''Тема урока: функции с возвратом значения
Функции с возвратом значения
Решение задач
Аннотация. Кроме функций, возвращающих числовые значения, можно писать и возвращающие логические, строковые и другие
 значения.

Возвращение булевых значений
Python позволяет писать булевы функции, возвращающие либо истину (True), либо ложь (False). Булеву функцию можно
применять для проверки условия, тогда значения True и False будут сигнализировать о его выполнении.

Булевы функции широко применяются для упрощения сложных условий, проверяемых в структурах принятия решения и
структурах с повторением.
Например, напишем программу, которая просит пользователя ввести число, и определяет четное оно или нечетное.

Это можно сделать так:

number = int(input())
if number % 2 == 0:
    print('Это число четное. ')
else:
    print('Это число нечетное.')
Этот фрагмент кода будет легче понять, если написать булеву функцию is_even(), которая принимает число в качестве
аргумента и возвращает True, если оно четное, и False если нечетное.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
Теперь можно переписать инструкцию if-else основной программы так, чтобы она для определения четности переменной
number вызывала функцию is_even():

number = int(input())
if is_even(number):
    print('Это число четное. ')
else:
    print('Это число нечетное.')
Так логику программы легче понять, а функцию можно вызывать в программе всякий раз, когда необходимо проверить
четность числа.

Использование булевых функций для валидации входных данных
Булевы функции можно также использовать для упрощения сложного кода валидации входных данных. Например в программе,
предлагающей пользователю ввести номер модели изделия, где возможны только значения 100, 200 и 300, можем написать
такой код:

model = int(input())

while model != 100 and model != 200 and model != 300:
    рrint('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input())
Цикл валидации использует длинное составное булево выражение, и повторяется до тех пор, покаmodel не будет
равняться 100 и 200 или 300.

Вместе с тем, цикл валидации можно упростить, написав булеву функцию проверки переменной model, и вызывая ее в цикле.
 Напишем функцию is_invalid(), которая принимает один параметр model и возвращает значение True, если модель
 недопустима и False в противном случае. Тогда цикл валидации можно переписать следующим образом:

while is_invalid(model):
    print('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input())
После этого изменения цикл становится легче читать. Теперь вполне очевидно, что цикл повторяется до тех пор, пока
номер модели недопустим. Приведенный ниже фрагмент кода показывает, как можно было бы написать функцию is_invalid().
Она принимает номер модели в качестве аргумента, и если аргумент не равен 100, 200 и 300, то эта функция
 возвращает True, говоря, что он недопустимый. В противном случае функция возвращает False.

def is_invalid(model):
    if model != 100 and model != 200 and model != 300:
        return True
    else:
        return False
Создание функций, реализующих такую простую логику — не всегда оптимальное решение, так как увеличивает размер кода
и ведет к затратам времени на вызов функции и возврат обратно результата, что может сказаться на производительности
программы.'''

'''Is Valid Triangle?
Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа,
 и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в 
 противном случае.

Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора.

Примечание 2. Следующий программный код:

print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))
должен выводить:

True
False
True'''

# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     if (side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side2 + side1):
#         return True
#
#     else:
#         return False
#
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))


'''Is a Number Prime? 🌶️
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение 
True если число является простым и False в противном случае.
 Примечание. Следующий программный код:
print(is_prime(1))
print(is_prime(10))
print(is_prime(17))
должен выводить:
False
False
True'''

# # объявление функции
# def is_prime(num):
#     flag = True
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             flag = False
#     if num > 1 and flag == True:
#         return True
#     else:
#         return False
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))

'''Next Prime 🌶️🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает
 первое простое число большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

 Примечание 2. Следующий программный код:

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
должен выводить:

7
11
17'''

# # объявление функции
# def get_next_prime(num):
#     flag = True
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             flag = False
#     if num > 1 and flag == True:
#         return True
#     else:
#         return False
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
#
#
# while not get_next_prime(n + 1):
#     n += 1
#     continue
# print((n+1))

'''Good password 🌶️
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля 
password и возвращает значение True если пароль является надежным и False в противном случае.

Пароль является надежным если:

его длина не менее 8 символов; 
он содержит как минимум одну заглавную букву (верхний регистр); 
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
 Примечание. Следующий программный код:

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
должен выводить:

True
False'''

# def is_password_good(password):
#     total = 0
#     if len(password) > 8:
#         total += 1
#     if password.isalnum():
#         total += 1
#     for i in password:
#         if i.islower():
#             total += 1
#             break
#
#     for i in password:
#         if i.isupper():
#             total += 1
#             break
#
#     if total >= 4:
#         return True
#     elif total < 4:
#         return False
#
#
# txt = input()
# print(is_password_good(txt))
#
#
# def is_password_good(password):
#     upp = [i for i in password if i.isupper()]
#     low = [i for i in password if i.islower()]
#     dig = [i for i in password if i.isdigit()]
#     return all([len(password) >= 8, upp, low, dig])
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))

'''Ровно в одном
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и 
возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.

 Примечание. Следующий программный код:

print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))
должен выводить:

True
True
False
False
Sample Input:

bike
hike
Sample Output:

True'''

# def is_one_away(word1, word2):
#     for i in word1:
#         if i  in word2 :
#             word2 = word2.replace(i, '', 1)
#             word1 = word1.replace(i, '', 1)
#     m2 = len(word2)
#     m1 = len(word1)
#     return m1 == m2 == 1
#
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))

'''Палиндром 🌶️
Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение 
True если указанный текст является палиндромом и False в противном случае.

Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также
 символы , . ! ? -.

Примечание 3. Следующий программный код:

print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))
должен выводить:

True
True
False'''

# # объявление функции
# def is_palindrome(text):
#     text = [i.lower() for i in text if i not in (',.!?- ')]
#     return text == text[::-1]
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_palindrome(txt))

'''BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK
 фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля 
password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в 
противном случае.

 Примечание. Следующий программный код:

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:

True
False
False
False'''

# def isPrime(n):
#     if n % 2 == 0: return(n == 2)
#     d = 3
#     while d * d <= n and n % d != 0: d += 2
#     return(d * d > n)
#
# def isPalindrom(n):
#     n = str(n)
#     return(n == n[::-1])
#
# def isEven(n): return(not n % 2)
#
# def is_valid_password(password):
#     try:
#         a, b, c = map(int, password.split(':'))
#         return(isPalindrom(a) and isPrime(b) and isEven(c))
#     except: return(False)
#
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))

'''Правильная скобочная последовательность
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую 
из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной 
последовательностью и False в противном случае.

Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), 
где каждой открывающей скобке найдется парная закрывающая скобка.

Примечание 2. Следующий программный код:

print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))
должен выводить:

True
False'''


# # объявление функции
# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#
#     # Возвращаем True, если text с пустой строкой
#     return not text
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))

'''Змеиный регистр
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем 
регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.

Примечание 2. Следующий программный код:

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
должен выводить:

this_is_camel_cased
is_prime_number'''
# объявление функции
def convert_to_python_case(text, sep='_'):
    snake_register = ''
    for i in text:
        if i.isupper():
            snake_register += sep + i.lower()
        else:
            snake_register += i
    return snake_register.lstrip(sep)

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
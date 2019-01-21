"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных
 в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Урок 2:
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


import timeit


n = int(input("Давайте найдем сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... Выберите, чему равно n "))
i = 1
number = 1
# вычисляем, какое число будет n-ным в последовательности 1, -0.5 , 0,25 ....

#Способ №1 через цикл
def loop(n, number, i):
    list_num = [1]
    while i < n:
        number = number / -2
        list_num.append(number)
        i += 1
    return sum(list_num)

print(loop(n, number, i))

print(timeit.timeit(("loop(n, number, i)"), setup="from __main__ import loop, n, number, i"))
# при  n = 6 время выполнения пишет 5.8 секунд, хотя столько между вводом числа 6 и выводом результата функции
# явно не прошло


#Способ №2 алгоритм как он был написан ко второму уроку: цикл + рекурсия, но время только рекурсии (( -
while i < n:
    number = number / -2
    i += 1
last_number = number
print(last_number)


# выход из алгоритма на условии else,
# когда первый аргумент становится равен n-ному числу последовательности
def num_sum(number, last_number):
    if number != last_number:
        return number + num_sum(number/ -2, last_number)
    else:
        return number
# вызываем функцию от 1 и уже определенного нами ранее n-нного числа последовательности
#print(num_sum(1, last_number))
print(timeit.timeit(("num_sum(1, last_number)"), setup="from __main__ import num_sum, last_number"))
# при  n = 6 время выполнения пишет 4 секунды. Но при этом первый цикл while как я понимаю, в это время не входит.


#Способ №3 Учитываем и цикл по нахождению n-ного числа в ряду, и рекурсию


def loop_2(n, number, i):
    while i < n:
        number = number / -2
        i += 1
    return number

def num_sum_2(number, last_number):
    if number != last_number:
        return number + num_sum(number/ -2, last_number)
    else:
        return number


n = int(input("Давайте найдем сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... Выберите, чему равно n "))
i = 1
number = 1

# вызываем функцию от 1 и уже определенного нами ранее n-нного числа последовательности (результат функции-цикла)
print(num_sum_2(1, loop_2(n, number, i)))



print(timeit.timeit(("num_sum(1, loop_2(n, number, i))"), setup="from __main__ import num_sum, loop_2, n, number, i"))
# при  n = 6 время выполнения пишет 8 секунд.
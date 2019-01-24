"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных
 в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Урок 2:

7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

"""
import cProfile
from random import randint
import timeit


#Способ №1 рекурсия

def eq_check():

    def sum_up(n, last):
        if n == last:
            return n
        else:
            return n + sum_up(n + 1, last)

    last = randint(1, 100)
    n = 1
    return sum_up(n, last) == last*(last+1)/2


print(eq_check())
cProfile.run('eq_check()')
# если задать вручную n = 568, то время показывает 0,004 сек

print(timeit.timeit(("eq_check()"), setup="from __main__ import eq_check"))
# время выполнения пишет больше 58 секунд, хотя результат на print(eq_check()) выдает очень быстро. Почему?


#Способ №2 


def check():
    num = randint(1, 100)
    num_list = [n for n in range(1, num+1)]
    return sum(num_list) == int(num*(num+1)/2)

print(check())
cProfile.run('check()')
# если задать вручную n = 568, то время показывает 0,000 сек, если число выбрать значительно больше, то на рекурсии
# (способ №1) его уже не проверить, так как пишет превышение глубины. Время в любом случае без рекурсии меньше

print(timeit.timeit(("check()"), setup="from __main__ import check"))
# время выполнения пишет больше 22 секунд, хотя результат на print(check()) выдает тоже очень быстро. Почему?
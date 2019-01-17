"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""
from random import randint

def sum_up(n, last):
    if n == last:
        return n
    else:
        return n + sum_up(n+1, last)
n = 1
last = randint(1, 100)

print(f"{sum_up(n, last)} = {last}({last}+1)/2)")

if sum_up(n, last) == int(last*(last+1)/2):
    print("Равенство выполняется")
else:
    print("Равенство 1+2+...+n = n(n+1)/2 не выполняется")




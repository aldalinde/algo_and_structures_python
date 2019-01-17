"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""
from random import randint

def count(num_quant, figure, i, quant):
    if num_quant != i:
        num = str(randint(0, 9999))
        print(num)
        quant = num.count(figure)
        return quant + count(num_quant, figure, i+1, quant)
    else:
        return 0

num_quant = int(input("Введите количество чисел в последовательности "))
figure = input("Введите цифру")

print(f"Количество цифр {figure} в последовательности - {count(num_quant, figure, 0, 0)}")
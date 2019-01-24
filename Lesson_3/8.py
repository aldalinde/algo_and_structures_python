"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. 
В конце следует вывести полученную матрицу.
"""
from random import random


M = 4
N = 4
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 100))
        print("%5d"% b[j], end='')
    a.append(b)
    print('    |', sum(b))

for i in range(M):
    print("   --", end='')
print()

for i in range(M):
    n = 0
    for j in range(N):
        n += a[j][i]
    print("%5d"% n, end='')
print()
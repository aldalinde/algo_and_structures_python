"""
6.	В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint


# making a list of 10 random integers in range 0 : 20
rand_num_list = []
while len(rand_num_list) < 10:
    rand_num_list.append(randint(0 , 20))
print(rand_num_list)

a_max = rand_num_list.index(max(rand_num_list))
b_min = rand_num_list.index(min(rand_num_list))

#print(a_max, rand_num_list[a_max], b_min, rand_num_list[b_min])

if a_max > b_min:
    print(f"Сумма чисел между минимальным и максимальным числами равна {sum(rand_num_list[b_min + 1:a_max])}")
else:
    print(f"Сумма чисел между минимальным и максимальным числами равна {sum(rand_num_list[a_max + 1:b_min])}")
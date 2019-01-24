"""
7.	В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться. 
"""
from random import randint


# making a list of 10 random integers in range 0 : 20
rand_num_list = []
while len(rand_num_list) < 10:
    rand_num_list.append(randint(0 , 20))
print(rand_num_list)

min1 = min(rand_num_list)
rand_num_list.remove(min1)

min2 = min(rand_num_list)

print(f"Двумя наименьшими элементами списка являются {min1} и {min2}")
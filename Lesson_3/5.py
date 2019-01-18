#5.	В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint


# making a list of 10 random integers in range - 10 : 10
rand_num_list = []
while len(rand_num_list) < 10:
    rand_num_list.append(randint(-10 , 10))
print(rand_num_list)

negatives = [n for n in rand_num_list if n < 0]

print(f"Максимальное отрицательное число {max(negatives)} имеет в ряду индекс {rand_num_list.index(max(negatives))}")

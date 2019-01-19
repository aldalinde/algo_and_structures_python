#3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

numbers = [j for j in range(2, 100)]
random.shuffle(numbers)
list1 = numbers[:9]
print(list1)
a = list1.index(max(list1))
b = list1.index(min(list1))
list1[a], list1[b] = list1[b], list1[a]

print(list1)
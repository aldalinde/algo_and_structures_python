# 4.	Определить, какое число в массиве встречается чаще всего.

from random import randint


# making a list of 20 random integers in range 0 - 10
rand_num_list = []
while len(rand_num_list) < 20:
    rand_num_list.append(randint(0, 10))
print(rand_num_list)

new_list = list(map(str, rand_num_list))

# forming a dictionary number:quantity
d = {}
for i in new_list:
    a = new_list.count(i)
    d[i] = a

max_quantity = max(d.values())

max_value = []
for k, v in d.items():
    if v == max_quantity:
        max_value.append(k)

# print(d) #dictionary output
print(f"Число(а) {max_value} имеют(ет) максимальное количество вхождений: {max_quantity}")


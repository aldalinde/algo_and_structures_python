"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random

# функция сортировки
def sort_array(array):
    return sorted(array)

# функция создания списка длиной 2m + 1
def array(m):
    array = []
    for n in range(2 * m + 1):
        array.append(random.randint(0, 100))
    return array

# функция определения медианы без сортировки списка
def median(array, m):
    # создаем копию списка
    arr = array[:]
    # обходим по очереди числа списка и вводим переменные счетчиков больших и меньших чисел
    for num in array:
        greater = 0
        less = 0
    # сравниваем число по очереди со всеми числами ряда; в зависимости от сравнения наращиваем счетчики less и greater
        for a in arr:
            if a < num:
                less += 1
            elif a > num:
                greater += 1
        # как только доходим до числа, по результатам сравнения с которым количество меньших или больших чисел ряда
        # равно половине длины ряда(то есть переменной m), функция возвращает значение этого числа
        if less == m or greater == m:
            return num


m = 15
# для проверки выводим случайный ряд, сотрированный ряд, медиану, найденную путем сортировки
check = array(m)
print(check)
print(sort_array(check))

# вызываем функцию нахождения медианы без сортировки и выводим ее результат
print(sort_array(check)[m])

#
print(median(check, m))
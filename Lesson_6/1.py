"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

# разрядность ОС - 64 бита, Python 3.7

# для анализа использовался memory_profiler


from memory_profiler import profile

@profile
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(36,60))
# на каждой строке используется 15 МиБит с 0 инкрементом



# Способ с решетом Эратосфена


@profile
def sieve(i):
    num_list_e = [n for n in range(2, i ** 2)]
    num_copy = num_list_e[:]
    num_plain = [n for n in range(1, i ** 2)]
    for n in num_list_e:
        if n in num_plain:
            for num in num_copy:
                if n == num_plain[i]:
                    return num_plain
                else:
                    if num % n == 0 and num != n:
                        if num in num_plain:
                            num_plain.remove(num)




i = 100


print(sieve(i)[i])
# на каждой строке используется от 15 до 16 МиБит с 0 инкрементом, только на строках 33 - 35 инкремент 0,1 МиБит (строки
# формирования числового списка с помощью генератора и его копирование


# Способ без решета
@profile
def plain(i):
    num_list = [2]
    n = 2
    while len(num_list) < i:
        counter = 0
        n += 1
        for num in num_list:
            counter += 1
            if n % num != 0:
                if counter == len(num_list):
                    num_list.append(n)

                    break
            else:
                break


    return num_list

print(plain(i)[i-1])

# на каждой строке используется от 15.1 МиБит с 0 инкрементом

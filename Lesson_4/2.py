"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""



# Способ с решетом
import cProfile
import timeit


def plain_1(i):
    num_list_1 = [n for n in range (1, i**2)]
    num_plain_1 = [1, 2]
    for num in num_list_1:
        if num != 1 and num != 2:
            c = 1
            for pl in num_plain_1:
                if pl != 1 and pl != num:
                    if num % pl == 0:
                        break
                    else:
                        c += 1
                        if c == len(num_plain_1):
                            num_plain_1.append(num)
                            break
    return num_plain_1[i]

i = 20
# выводим число из результата функции (плученного списка num_plain_1
print(plain_1(i))
cProfile.run('(plain_1(i))')
# i = 20: 0.007 секунд, при  i = 200: 22302 function calls in 0.025 seconds


#print(timeit.timeit(("plain_1(i)"), setup="from __main__ import plain_1, i"))
#время выполнения пишет 5.8 секунд, хотя столько между выводом результата функции (71)
# явно не прошло и пары секунд, а вот результат timeit пришлось ждать очень долго. Похоже было
# как раз (вот до сих пор жду ..... UPD прошло три минуты, результата нет. прерываю процесс

# Способ без решета

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

print(plain(i)[-1])

cProfile.run('(plain(i)[-1])')

#i = 20: 0.001 секунда, при  i = 200: 22302 function calls in 0.024 seconds - значительно быстрее решета
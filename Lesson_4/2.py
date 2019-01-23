"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""




import cProfile
import timeit
# Способ с решетом
# Взяла алгоритм из википедии:
# 1. Выписать подряд все целые числа от двух до n (2, 3, 4, …, n).
# 2. Пусть переменная p изначально равна двум — первому простому числу.
# 3. Зачеркнуть в списке числа от 2p до n считая шагами по p (это будут числа кратные p: 2p, 3p, 4p, …).
# 4. Найти первое незачёркнутое число в списке, большее чем p, и присвоить значению переменной p это число.
# 5. Повторять шаги 3 и 4, пока возможно.
# Получается, что заранее у нас очень большой список. Чтобы обеспечить попадание i-того простого числа в наш список,
# мы вынуждены возвести i в степень 2 и перебирать уже этот длинный список.
# Отсев проводится не до конца списка, а до ограничиеля - когда делитель равен i-тому отсеиваемом списке


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




i = 20

print(sieve(i))

cProfile.run('(sieve(i)[i])')
# Способ №2 - без решета Эратосфена

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


# выводим число из результата функции
print(plain_1(i))
cProfile.run('(plain_1(i))')
# i = 20: 0.007 секунд, при  i = 200: 8907759 function calls in 14.584 seconds


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

#i = 20: 0.010 секунда, при  i = 200: 22302 function calls in 0.024 seconds - значительно быстрее решета
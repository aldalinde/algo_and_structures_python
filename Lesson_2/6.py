"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
from random import randint

print("Угадайте число от 0 до 100 за 10 попыток")

def guess(number, i):
    tries = 11 - i
    print(f"Попыток осталось {tries}")
    n = int(input(f"Введите число "))

    if n == number:
        print("Вы угадали!")
        return number
    elif i == 10:
        print("Вы проиграли")
        return number
    else:
        i += 1
        print("Не угадали")

        while True:
            if n < number:
                print(f"Число {n} меньше загаданного")
                a = guess(number, i)
            elif n > number:
                print(f"Число {n} больше загаданного")
                a = guess(number, i)
            print()
            return a


number = randint(0, 100)
result = guess(randint(0, 100), 1)

print(f"Загаданное число было {result}")


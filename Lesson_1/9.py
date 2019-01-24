# 9.	Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input("Введите три разных числа. Первое число "))
b = int(input("Второе число "))
c = int(input("Третье число "))

if a == b or b == c or a == c:
    print("Все три числа должны быть разными ")
else:
    print("Среднее по значению число ")
    if a > b:
        if b > c:
            print(b)
        else:
            if a > c:
                print(c)
            else:
                print(a)
    else:
        if a > c:
            print(a)
        else:
            if b > c:
                print(c)
            else:
                print(b)



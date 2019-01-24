#2.	Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

num1 = 5
num2 = 6

num_or = num1 | num2
num_and = num1 & num2
num_xor = num1 ^ num2
num1_right = num1 >> 2
num1_left = num1 << 2

print("Результат побитового OR: %2s" % bin(num_or))
print("Результат побитового AND: %2s" % bin(num_and))
print("Результат побитового XOR: %2s" % bin(num_xor))
print("Результат побитового сдвига вправо %2s: %s" % (bin(num1), bin(num1_right)))
print("Результат побитового сдвига влево %2s: %s" % (bin(num1), bin(num1_left)))
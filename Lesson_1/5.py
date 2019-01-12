#5.	Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
import string

letter1 = input("Enter the first letter ")
letter2 = input("Enter the second letter ")
ind_1 = string.ascii_lowercase.index(letter1)
ind_2 = string.ascii_lowercase.index(letter2)
print("Number of letters between given: ")
print(string.ascii_lowercase.index(letter2) - string.ascii_lowercase.index(letter1) - 1)

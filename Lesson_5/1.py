"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections

fin_report = collections.defaultdict(list)
comp_number = int(input("Общее число предприятий: "))

for n in range(comp_number):
    comp_name = input(f"Наименование {n + 1}-го предприятия: ")
    profit_1_quater = float(input("Прибыль за 1-й квартал: "))
    profit_2_quater = float(input("Прибыль за 2-й квартал: "))
    profit_3_quater = float(input("Прибыль за 3-й квартал: "))
    profit_4_quater = float(input("Прибыль за 4-й квартал: "))
    fin_report[comp_name] = profit_1_quater + profit_2_quater + profit_3_quater + profit_4_quater

average_profit = sum(fin_report.values()) / comp_number

print("Средняя годовая прибыль предприятий %s составляет %.2f" % (list(fin_report.keys()), average_profit))

better_doing = []
worse_doing = []

for company in fin_report:
    if fin_report[company] > average_profit:
        better_doing.append(company)
    elif fin_report[company] < average_profit:
        worse_doing.append(company)

print(f"Компании с прибылью выше средней: {better_doing}")
print(f"Компании с прибылью ниже средней: {worse_doing}")
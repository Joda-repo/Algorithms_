"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

company = namedtuple('Company', 'name Q1 Q2 Q3 Q4 year')

count_company = int(input('Введите количество компаний для анализа: '))
companies = [0 for _ in range(count_company)]
profit = 0

for i in range(count_company):
    name = input(f'Введите название {i + 1}-й компании: ')
    quarters = [float(j) for j in input('Введите через пробел прибыль в каждом квартале: ').split()]

    year = 0
    for quarter in quarters:
        year += quarter

    profit += year
    companies[i] = company(name, *quarters, year)


if count_company == 1:
    print(f'Для анализа передано 1 компании: {companies[0].name}. Eё годовая прибыль: {companies[0].year}')

else:
    profit_average = profit / count_company

    less = []
    more = []

    for i in range(count_company):

        if companies[i].year < profit_average:
            less.append(companies[i])

        elif companies[i].year > profit_average:
            more.append(companies[i])

    print(f'\nСредняя годовая прибыль по компаниям: {profit_average}')

    print(f'Компании, чья прибыль меньше {profit_average}:')
    for com in less:
        print(f'Компания "{com.name}" с прибылью {com.year}')

    print(f'\nКомпании, чья прибыль больше {profit_average}:')
    for com in more:
        print(f'Компания "{com.name}" с прибылью {com.year}')

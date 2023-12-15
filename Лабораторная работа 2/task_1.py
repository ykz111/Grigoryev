money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
n = 0
s = float(money_capital)
f = 1
i=0
while f:
    if s > 0:
        spend = spend*((1+increase)**(i))
        s = s+salary-spend
        n+=1
        i+=1
    else:
        f=0
print("Количество месяцев, которое можно протянуть без долгов:", n+1)

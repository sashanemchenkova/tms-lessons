# Пользователь вводит два числа: x, y, где x - сумма рублей, которую он кладёт на депозит под 10% годовых,
# y - количество лет. Каждый год вклад увеличивает на 10%. Эти деньги прибавляются к сумме вклада, и на них в
# следующем году тоже будут проценты Вывести конечную сумму на счету по прошествии y лет.
x = float(input('enter amount : '))
y = int(input('enter years : '))
print(x * 1.1 ** y)
price = [57.8, 46.51, 97.6, 345.10, 55.3, 677.24, 7355.12, 150.33]
rub = 0
kop = 0

for i in price:
    money = str(i).split(".")
    if len(money) == 2:
        rub, kop = money
    print(f"{int(rub)} р. {int(kop):02d} коп.,", end=" ")

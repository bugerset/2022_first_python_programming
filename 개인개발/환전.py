money = int(input("얼마 넣음"))
price = int(input("얼마 짜리"))

change = money - price

coin500 = change // 500
reform_change = change % 500
coin100 = reform_change // 100
coin50 = reform_change % 100 // 50

print(coin500, coin100, coin50)
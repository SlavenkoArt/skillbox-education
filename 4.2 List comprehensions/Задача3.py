def promotion(price, percent):
    return round(price * (1 + percent / 100), 2)

price_list = [1.09, 23.56, 57.84, 4.56, 6.78]

first_year_percent = int(input('Повышение на первый год: '))
second_year_percent = int(input('Повышение на второй год: '))

first_year = [promotion(i, first_year_percent) for i in price_list]
second_year =[promotion(i, second_year_percent) for i in first_year]

print('Сумма цен за каждый год: ', round(sum(price_list), 2), round(sum(first_year), 2), round(sum(second_year), 2))
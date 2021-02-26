def simple_calc():
    x = float(input('Количество отработанных часов : '))
    y = float(input('Ставка оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии: - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc()}')

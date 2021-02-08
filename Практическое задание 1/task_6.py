a = float(int(input('Введите расстояние которое надо пробежать в первый день в км: ')))
b = float(int(input('вседите расстояник в км которое надо достичь: ')))

counter = 1
while a <= b:
    print(f'{counter} день: {round(a, 2)} км.')
    a *= 1.1
    counter += 1

print(f'{counter} день: {round(a, 2)} км.')
print(f'Спортсмен пробежит не менее {b} км на {counter} день.')

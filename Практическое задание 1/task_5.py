a = int(input('Введите выручку компании в рублях a: '))
b = int(input('Ведите размер издержек в рублях b: '))
if (a >= b):
    print('У компании прибыль!')
    print('Рентабельность предприятия в процентах:', (a - b) / a * 100)
else:
    print('У компании убыток')
c = int(input('Введите число сотрудников: '))
print('Прибыль на одного сотрудника руб.:', (a - b) / c)

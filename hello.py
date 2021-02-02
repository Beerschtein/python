a = int(input('Введите a: '))
b = float(input('Введите b: '))
print(a > b)

a = int(input('Введите выручку компании в рублях a: '))
b = int(input('Ведите размер издержек b: '))
if (a >= b):
    print('Прибыль')
    print('Рентабельность предприятия в процентах:', (a - b) / a * 100)
else:
    print('Убыток')
c = int(input('Введите число сотрудников: '))
print('Прибыль на одного сотрудника:', (a - b) / c)




a = (input('text: '))
print("This is my string:", a)



a = 10
b = a + 5
print("10+5 =", b)

a = 'Pioner'
print(a)

n = int(input('Введите число n: '))
a = n
print(a)

a = int(input('Введите число n: '))
b = n * 10 + n
c = n * 100 + n * 10 + n
print('Сумма n+nn+nnn равняется: ', a + b + c)



sec = int(input('Введите время в секундах: '))
h = sec // 3600
m = (sec-h*3600) // 60
s = sec % 60
print(h,'час',m,'мин',s,'сек')




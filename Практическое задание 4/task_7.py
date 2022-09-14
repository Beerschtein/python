from itertools import count
from math import factorial


def fgen():
    for i in count(1):
        yield factorial(i)

generator = fgen()
x = 0
n = int(input('Введите число: '))
for k in generator:
    if x < n:
        print(k)
        x += 1
    else:
        break



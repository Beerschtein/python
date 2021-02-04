from itertools import count, cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

cycler = cycle([10, 15, 20])
action = None
print('Нажмите Enter для вывода следующего числа списка')
print('Нажмите q, чтобы прервать операцию')
while action != 'q':
    print(next(cycler), end='')
    action = input()


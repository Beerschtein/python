l = [8, 7, 5, 4, 2, 1]
while True:
    new_digit = input('Введите число: ')
    if new_digit == 'stop':
        break
    new_digit = int(new_digit)

    for i in range(1, len(l)):
        if new_digit >= max(l):
            l.insert(0, new_digit)
            break
        elif new_digit <= min(l):
            l.append(new_digit)
            break
        elif l[i - 1] >= new_digit >= l[i]:
            l.insert(i, new_digit)
            break
    print(l)






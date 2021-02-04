def my_func():
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        return a / b
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        return

print(my_func())





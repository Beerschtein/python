def my_func(x: float, y: int):
    a = 1
    for _ in range(abs(y)):
        a *= x
    return x ** y


print(my_func(2.8, -3))




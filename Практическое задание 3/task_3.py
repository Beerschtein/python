def my_func(a, b, c):
    d = [a, b, c]
    d.remove(min(a, b, c))
    return sum(d)
print(my_func(5, 10, 15))


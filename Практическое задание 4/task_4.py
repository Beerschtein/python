my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) < 2]

print(my_new_list)

# наверное здесь надо было делать как-то через множество
# оно показывает уникальные числа
# но там элементы расположены в беспорядке

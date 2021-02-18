f = open('f_txt_1.txt', 'w')
line = input('Введите текст \n')
while line:
    f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

f.close()







f_file = 'f_file_2.txt'

with open(f_file, 'r') as f:
    lines = f.readlines()
print(f'Количество строк {len(lines)}')
for i, line in enumerate(lines, 1):
    print(f'Количество слов в {i} строке {len(line.split())}')
rows = int(input('Enter th number of rows:'))
for i in range(0, rows):
    for j in range(rows-1, i, -1):
        print(j, end='')
    for k in range(i+1, rows):
        print(k, end="")
    print('\n', end='')

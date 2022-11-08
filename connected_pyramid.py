rows = int(input('Enter th number of rows:'))
for i in range(rows):
    for k in range(i+1, rows):
        print(k, end="")
    for j in range(rows-1, i, -1):
        print(j, end='')
    print('\n', end='')

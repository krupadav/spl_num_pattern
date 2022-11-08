rows = int(input('Enter the number of rows:'))
last_even_num = 2*rows
even_num = last_even_num
for i in range(rows):
    even_num = last_even_num
    for j in range(i):
        print(even_num, end=' ')
        even_num -= 2
    print('')

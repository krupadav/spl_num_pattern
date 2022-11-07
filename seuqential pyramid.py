current_number = int(input('Enter current number:'))
stop = int(input('stop point:'))
rows = int(input('Enter number of rows:'))
for i in range(rows):
    for j in range(1,stop):
        print(current_number, end='')
        current_number += 1
    print('')
    stop += 2

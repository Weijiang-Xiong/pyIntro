row=5

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j > i:
            print(' ', end = '')
        else:
            print('*', end='')
    print()
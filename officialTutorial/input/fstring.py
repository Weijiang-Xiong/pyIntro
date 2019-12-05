import math

print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

for index, name in enumerate(table):
    print(f'{index:10d} ==> {name:10}')

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
from timeit import Timer

# Timer('Expressions', 'Given Data')
time_1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
time_2 = Timer('a,b = b,a', 'a=1; b=2').timeit()

print(time_1 - time_2)
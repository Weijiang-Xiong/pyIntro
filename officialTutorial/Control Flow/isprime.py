for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:               # 下一行的 print(n) 事实上属于语句块 for i in range(2, n): 
        print(n)        # 整个循环结束，都没有发生 break 的情况下，才执行一次 print(n)
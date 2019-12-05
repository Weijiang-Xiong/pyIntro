"""a function to calculate Fibonacci series

    you can launch prompt from this directory, and 'import fibo'
    this way, those functiosn must be called by fibo.function_name()
    if you use 'from fibo import *', you can directly use fib(arg) and fib2(arg)

    Note: For efficiency reasons, each module is only imported once per interpreter session. Therefore, if
    you change your modules, you must restart the interpreter – or, if it’s just one module you want to test
    interactively, use importlib.reload(), e.g. import importlib; importlib.reload(modulename). 
"""
# Fibonacci numbers module
def fib(n): # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# you can use 'pyton fibo.py 5' in command prompt window
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

def scope_test():

    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal() 
    # nonlocal variables can be accessed by statements outside the function
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
    scope_test()
    print("In global scope:", spam)

scope_test()
# global variables can be accessed throughout the whole programme.
print("In global scope:", spam)
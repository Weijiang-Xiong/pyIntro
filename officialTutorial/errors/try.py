while True:
    try:
        # at first, these will be executed
        x = int(input("Please enter a number: "))
        break
        # if anything goes wrong, python will skip the things above and look for the error message in the follwing exceptions
    except ValueError:
        # if valueerror occurs, these will be executed
        print("Oops! That's not a valid number. Try again!...")

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

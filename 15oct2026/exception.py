try:
    a=input("enter number 1:")
    b=input("enter number 2:")
    print(int(a)/int(b))
except ValueError:
    print("Give the number as a input")
except ZeroDivisionError:
    print("Cannot Divide by Zero")
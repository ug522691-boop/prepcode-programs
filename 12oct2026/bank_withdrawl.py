amount = int(input("enter the withdraw amount"))
balance = int(input("enter the balance amount"))
if amount  <= balance and amount % 500==0:
    print("transaction is a allowed")
else:
    print("transaction is not allowed")
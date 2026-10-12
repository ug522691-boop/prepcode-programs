p1=int(input("enter the first product price"))
p2=int(input("enter the second product price"))
if p1<p2:
    print("first product is cheaper")
elif p1>p2:
    print("first product is more expensive")
else:
    print("both products have the same price")
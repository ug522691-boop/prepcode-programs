upendra=dict()
s=input("enter your name")
for ch in s:
    if ch not in upendra:
        upendra[ch]=1
    else:
        upendra[ch]=upendra[ch]+1
print(upendra)
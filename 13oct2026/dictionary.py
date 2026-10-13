meghana=dict()
s=input("enter your name")
for ch in s:
    if ch not in meghana:
        meghana[ch]=1
    else:
        meghana[ch]=meghana[ch]+1
print(meghana)            
ashok=dict()
s=input("enter your name")
i=0
for ch in s:
    if ch not in ashok:
        ashok[ch]=[i]
    else:
        ashok[ch].append(i)
    i=i+1
print(ashok)    
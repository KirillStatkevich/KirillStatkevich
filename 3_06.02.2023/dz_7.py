x=input("input yours sentansies\n")
m=[]
for i in x:
    if i==i.lower():
        y=i.upper()
        m.append(y)
    else:
        y=i.lower()
        m.append(y)
s="".join(m)
m=str(s)
print(m)
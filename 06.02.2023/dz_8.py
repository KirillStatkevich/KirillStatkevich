x=input("input your volue:\n")
m=0
l=0
for i in x:
        i=int(i)
        x=int(x)
        m=m+i
        l=l+1
m=float(m)
l=float(l)
m=m//l
print(f"{m:.3f}")
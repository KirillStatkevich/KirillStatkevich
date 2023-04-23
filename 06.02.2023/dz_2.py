x=input("введите список чисел\n")
v=0
for i in x:
    i=int(i)
    x=int(x)
    if i%2==0:
        v=v+i
    continue
print(v)
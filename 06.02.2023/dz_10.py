l= input("введите список чисел\n")
m,v1,q,v,k=0,0,0,0,0
for i in l:
    if i[0]<=l[m]:
        v1=l[m]
        v1=int(v1)
        i=int(i)
        v=int(v)
        if v<i:
            for i in range(10):
                if (v1 % i == 0):
                    k = k+1
                    if (k <= 0):
                        v=i
        m=m+1
        k=0
        continue
print(v)
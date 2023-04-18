l= [53,23,235,5,32,4234,2352,6,3,23,24,1,5,78,4]
m=0
for i in range (1, len(l)):
    if l[i]<=l[m]:
        m=i
print(m,l[m])
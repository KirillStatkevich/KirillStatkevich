y=int(input("do u want to input your value?(yes-1, none-0)\n"))
x=[]
while y==1:
    x1=input("input your value\n")
    x.append(x1)
    y=int(input("are u wish to input one more value?(yes-1, none-0)\n"))
    if y==0:
        break
    continue
else:
    print("you are a joker) he-he")
    exit()
q=0 
k = 0
x2=[]
for i1 in range(len(x)-1): # заменить на x
    if q>len(x):
        break
    x=x[q]
    x5=int(x)
    i1=int(i1)
    if (x5 % i1 == 0):
        k = k+1
    q=q+1
    x5=x
    if (k <= 0):
        x2.append(i1)
    k=0
print(x2)

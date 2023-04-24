y=int(input("are u wish to input your string?(yes-1, none-0)\n"))
x=[]
while y==1:
    x1=input("input your string\n")
    x.append(x1)
    y=int(input("are u wish to input one more string?(yes-1, none-0)\n"))
    if y==0:
        break
    continue
else:
    print("you are a joker) he-he")
    exit()
z=[]
for i in x:
    if len(i)>5:
        z.append(i)
print(z)




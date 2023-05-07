y=int(input("1-yes 0 no\n"))
x=[]
while y ==1:
    x1=input("input string\n")
    x.append(x1)
    y=int(input("1-yes 0 no\n"))
    if y==0:
        break
    continue
def strings (x):
    y=[]
    for i in x:
        if len(i)>5:
            y.append(i)
    print(y)
    return strings
print(strings(x))
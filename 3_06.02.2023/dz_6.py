x=input("введите ваше словосочетание\n")
x.lower
x=list(x)
y=set("уеыаоэяиюё")
for i in x:
    if i in y:
        x.remove(i)
    for i in x:
        if i in y:
            x.remove(i)
v="".join(x)
v=str(v)
print(v)
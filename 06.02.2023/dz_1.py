x=input("введите ваше словосочетание\n")
x.lower
x=list(x)
v=0
y=set("уеыаоэяиюё")
for i in x:
    if i in y:
        v+=1
    

        
print(v)
    
    
    
    


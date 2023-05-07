x=str(input("input your string\n"))
def string_1(x):
    u=0
    l=0
    for i in x:
        if i==i.upper():
            u+=1
        else:
            l+=1
    print(f"{u}: количество заглавных, {l}:количество строчных")
    return string_1
print(string_1(x))
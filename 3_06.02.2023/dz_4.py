l= input("введите список чисел\n")
m,v1,q,v=0,0,0,0
for i in l:
    if i[0]<=l[m]:
        m=m+1
        i=int(i)
        v=int(v)
        if v<i:
            v=i
            v1=m-1
        continue
x=list(l)
z=[]
for i in x:                 #c помощью этой функции удаляю дубликаты ненужного числа
    if i not in z:          #если i не присутствует в z, то мы его добавляем
        z.append(i)
x=z
  
del x[v1]
v,m,i=0,0,0
for i in x:
    if i[0]<=x[m]:
        m=m+1
        i=int(i)
        v=int(v)
        if v<i:
            v=i
        continue
print("Предпоследнее число по величине это: ",v)

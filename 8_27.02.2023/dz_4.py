def stepen(a,v,p=1):
    if v>=1:
        p=p*a
        return stepen(a,v-1,p)
    if v<1:
        print (p)
        return
    stepen(a)
stepen(125,113)

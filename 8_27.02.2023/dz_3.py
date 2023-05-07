sent="admiral makaroff"
def summa_simvola(text, m=input("input your bukva\n"),z=0,i=0):
    if i==len(sent)-1:
        return print(z)
    if text[i]==m:
        z+=1
        return summa_simvola(text,m,z,i+1)
    return summa_simvola(text,m,z,i+1)
summa_simvola(sent)
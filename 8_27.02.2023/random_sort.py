import random
l=[3,1,2,4,7,5,9]

def random_sort(l):
    counter=0
    while not is_sorted(l):
        swap(l)
        counter+=1
    print(counter)

def is_sorted(l):#проверка на сортировку
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    return True
   
def swap(l):
    i=generate_index(len(l))
    j=i
    while i==j:
        j=generate_index(len(l))
    l[i],l[j]=l[j],l[i]


def generate_index(n):#генерирует индекс
    return random.randint(0,n-1)
random_sort(l)
print(l)



# i,j=random.randint(0,len(l)-1),random.randint(0,len(l)-1)
# l[i],l[j]=l[i],l[i]
# print(l)
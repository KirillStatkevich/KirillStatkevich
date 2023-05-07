l=[1,2,3,4,5,6,7,8,9,10]#для этого метода поиска должна быть обязательно проведена сортировка по возрастанию или убыванию
def search(l,target,low,high):
    if low>high:
        return print("syntaksis out of range")
    mid=(low+high)//2
    if l[mid]==target:
        return mid
    if l[mid]>target:
        return search(l,target,low,mid-1)
    if l[mid]<target:
        return search(l,target,mid+1,high)
print(search(l,100,0,len(l)-1))

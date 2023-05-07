from functools import reduce
# lambda x,y: x+y #одноразовая функия
def apply(l,f,i=0):
    if i==len(l):
        return
    f(l[i])
    apply(l,f,i+1)

# def sq(x):
#     print (x*x) #тоже самое что напсано ниже в lambda

apply([1,2,3,4,5], lambda x:print(x*x))


s="Abc Aac aaa abc"
print(sorted(s.split(), key =lambda x: x.lower()))#cсортирует исходя из того что все элементы в нижнес регистре
print(sorted(s.split(), key =str.lower))#тоже самое что выше

#map
l=[1,2,3,4,5]
print(list(map(lambda num:chr(num*10),l)))#map нужно 2 аргумента 1 из которой функция(lambda) второй аргумент - l
#применяет к кадому итерируемому обьекту функцию ламба и отображает ее в виде chr

#filter функция должна выдовать true или false
print(list(filter(lambda x: x>2,l)))#к определенной колекции применяет функциюЮ, в которой true уходит в список

#reduce
#необходимо вызвать функцию
print(reduce(lambda x,y: x+y,l))#получаем сумму всего списка из l
print(reduce(lambda x,y:f"{x}-{y}",l))
print(reduce(lambda x,y: x if x>y else y,l))#ищет самый большой элемент в списке
x = range(100)
print(x,type(x))

def bad_generator():
    yield 1 # yield работает как ретурн, но не завершает работу функции.чаще всего указывают циклы
    yield 2
    yield 3.0
    yield "test"


# for i in bad_generator():
#     print(i)

gen1=bad_generator()
gen2=bad_generator()

print(gen1,type(gen1))

try:
    i=iter(gen1)#аналог цикла for 
    #пока выполняется цикломфункия bad_generator она будет выводить показания а потом свалится по ошибке  
    while True:
        print(next(i))
except StopIteration:#останавливаем ручную итерацию благодаря for и except
    print("the end of iteration")


i= iter(gen2)#генераторы не пересекаются между собой и не возможно провести генерацию несколько раз, только 1 раз 
print(next(i))

def fibonacci(n):#бесконечный цикл фибоначи
    a, b=0, 1
    count=0#ограничитель генератра
    while True:
        yield a
        count+=1
        if count==n:#ограничитель генератора
            break
        a,b = b, a+b

# for i in fibonacci(20):
#     print(i)

l=[32,5,6,7,[45432,12,[1,45,3,2,6,78],4,2,65],6,42,4]
def flat_sum(l):
    total=0
    for item in l:
        if isinstance(item,list):
            total+=flat_sum(item)
        else:
            total+=item
    return total
print(flat_sum(l))#суммирует все элементы в древовидном списке

def flatten(l):
    for item in l:
        if isinstance(item,list):
            yield flatten(item)
        else:
            yield item

for i in flatten([1,[2,[3],[4,[5]]]]):
    print(i)


def ever_cubes():
    for i in 10:
        if i%2==0:
            yield i**3

even_cubes=(i**3 for i in range(10)if i%2==0)#i**3-принцип преобразования, for...(10)- цикл,if i%2==0условие
#генератор чисел как list comprehension
for i in even_cubes:
    print(i)
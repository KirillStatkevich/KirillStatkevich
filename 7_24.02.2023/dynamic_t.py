def times(a,b):
    return a*b
print(times(2,3))
print(times([2],3))
print(times("2",3))
def times_for_int(a:int,b:int)->int:#:int указвает на тип поступаемых данных(но не обязательно)
    "the function will multiply only values"
    if isinstance(a, int) and isinstance(b, int):#разрешает ввод данных только в формате int(isinstance-проверка на принадлежность к типу данных)
        return a*b
print(times_for_int("2",3))

def eq(l1,l2): #проверка на совпадение колекций
    for i in l1:
        if i not in l2:
            return False
    for i in l2:
        if i not in l1:
            return False
    return True
print(eq([1,2,3],[3,2,1]))

    


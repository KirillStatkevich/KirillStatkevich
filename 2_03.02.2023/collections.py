d={"one": 1, "two":[2]}
key =1
if key in d:
    print(d[key])
else:
    print(f"cannot find{key}")
res=d.get(key, f"cannot find{key}")#get позволяет брать определенные значения, если не находит то выводит тоБ что после запятой
print(res)
print(d.keys())#выводит набор ключей
print((d.values()))#выводит набор значений
print(d.items())#выводит связь ключа с привязанным значением
if key in d.values():#нашли ключ не в ключах а в значениях(1)
    print("found it!")
print(hash("test"))#хэширует данные(каждый раз будет разное число) зависит от рандома
print(d.pop("two"))#удаление по ключу
print(d.popitem())#удаляет последнее связанное значение ключей из библиотеки
d.clear()#чистит библиотеку
print(d)
t=(1,2,3,4,5)#tuples или кортеж неизменяемый список
print(type(t),t)
t=()
print(type(t), t)
t=(1,)#кортеж из 1 составляющей
print(type(t), t)
l=list(t)#заменяем в turple 1 позицию создав лист
l[0]=1.0#заменяем позицию
t=tuple(l)#совершенно новый объект(на основании t создали список, отредактировали и создали новый кортеж)
print(t)
s=set()#set свалка данных
print(type(s),s)
s={1,2,3,4,5}
s.add(1)#добавление в set
s.add("test")#добавление в set
print(s)
s.update("test")#хэшированное добавление в set свалку
print(s)
s.remove("test")#удаление строки тест из set
print(s)
s.discard("test")#удаляет ключ, если уже удален, то не выдает ошибку
print({1,2,3}.union({3,4,5}))#обьеденение без одинаковых показателей
print({1,2,3}.intersection({3,4,5}))#выводит пересечение двух библиотек
s="test"
s=set(s)#выдает перечень символов без дубликата в рандомных позициях
print(s)
l=list("test")#преобразование спика в set с потерей дубликата символа t и потерей дальнейшего расположения в списке
l=set(l)
l=list(l)
print(l)
a,b ="test", "set"
print(a==b)#сравнивает символы в setЕ(получаем ложь так как сравниваем списки)
print(set(b)==set((a)))# получаем правду, так как это set и символы действительно используются одинаковые




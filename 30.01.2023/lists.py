l= []
print(len(l), type(l), l)
l=[1, 2, 3, 4, 5, "test", [6, 7, 8, 9, 10]]
print(l)
print(l[0], l[-1], l[1:3])
print(list("my test str"))# преобразование текста в списки
l[0]=1.1# заменяем 1 число под индексом 1 на указанное
print(l)
l.append("new elem")#append команда для ввода даных в конец списка
print(l)
l.insert(0,0.0)# втискивает вперед списка необходимые данные двигая все остальные вправо
print(l)
l.extend("test")# разбивает данные на составляюще и добавляет в конец
print(l)
l.remove("test")#удаляет первое схождение из списка (не удалил так как test разбит на части)
print(l)
print(l.pop())#вычеркивает последний элемент и выводит его как результат с конца в начало
print(l.pop())#если указать (0) то пойдет с начала в конец
print(l.pop())
print(l.pop())
print(l)
del l[0:4]# удаляет все шо угодно, в данно случае часть списка от начала до 4 символа
l.clear()# чистит полностью список
print(l)
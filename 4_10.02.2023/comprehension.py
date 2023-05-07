print([x for x in range(10)])#вывосдит List в дипозоне от 0 до 9
l=[str(x) for x in range(10)]#выводит дипозон от 0 до 9 в формате str
print(l)
# l=[]                       тоже самое что и код в строке №2 
# for x in range(10):
#     l.append(str(x))
# print(l)
l=[str(x) for x in range(10) if x%2==0 if x!=0]
print(l)
d={1:"one", 2:"two"}
l=[f"{k}:{v}" for k, v in d.items()]# выводит ключи из словаря в str с указанной функцией, где k-key, v-value d.items(указательБ что необхожимы именно соединения)
print(l)
l={x for x in range(10)} #выводит список чисел в формате set (по порядку по тому что машина воспринимает цифры почти как анаогичные цифры)
print(l)
l={x for x in "test comprehension"} #выводит текст в формате set не в порядке без дубликатов
print (l)
l=tuple(x for x in "test comprehension") #выводит текст в формате turple(кортеж) в последовательном порядке
print (l)
l={x:chr(x*10)for x in range(1,11)}# выводит ключи где x это число, а chr(x*10)- это команда которая интерпритирует цифры в код компуктера
print(l)
l=[[1,2,3],[4,5,6],[7,8,9]]# выводит внутренние списки по отдельности
print([f"{x} - {y}" for x in l for y in x]) #получаем ключи к каждомой цифре в списке
print([f"{y}" for x in l for y in x])# просто перечисляет данные из списка
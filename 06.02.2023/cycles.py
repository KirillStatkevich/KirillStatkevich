x=1
while x<=10:
    print(x)
    x+=1    
l=[1,2,3,4,5]
for elem in l:#перечисляет все значения в указанном диапазоне с указанными услувиями
    print(elem)
print("the end")
#break-прерывает выполнения цикла
#continue-переходит к следующей итерации
#pass- не делает ничего
#else после тела цикла-выполняется только если цикл завершился самостоятельно, те не сраюботало ни одного break
x=0
while True:
    print("infinity,but is it?")
    x+=1
    if x>10:
        break
print("end")
for elem in [1,2,3,4,5]:
    if elem %2==0:#если elem делим на 2 и в остатке 0 то цикл пропускает 1 шаг
        continue#не завершает цикл но продолжает его
    print(elem)
print("end")
for i in range(10):#устанавливает диапазон(это логика при которой к предыдущему значению прибавляется +1)
    print(i)
for i in range(2,11,2):#диапазон от 2 до 11 с шагом 2
    print(i)
for i, e in enumerate("test str"):#помогает разбить на составляющие с выводом позиции(индекса)
    print (i,e)
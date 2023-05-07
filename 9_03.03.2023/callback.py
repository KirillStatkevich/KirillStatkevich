def apply(l,f,i=0):#l-лист f вызов функции как обьекта
    if i==len(l):
        return
    f(l[i])
    apply(l,f,i+1)
apply([1,2,3,4,5],print)#список + функция print

def c1bck():
    print("i,m a callback")

# import threading #штука для многопоточности
# print("before the timer")
# threading.Timer(3,c1bck).start()# 3-3секунды и начинает работать функция c1bck только через 3 секнды после отработки проги
# print("after the timer")
# print("the end")

import time#импортируем время для определения времени обработки данных

chunk=1000 #указываем количество бит(символов) для прочитки(чем больше число то быстрее работает но не больше обьема самого файла)
with open("6_17.02.2023/test.jpg", "rb") as f:#для открытия картинок всегда использовть команды по типу rb
    # print(f.read(15))#пытаемся прочитать первые 15 символов картинки jpg
    with open("6_17.02.2023/test-copy.jpg","wb") as w:#открывается 1 опеном файл а 2ой уже перезаписывает в новый файл
        start=time.time()#начало отсчета времеени
        while True:
            part=f.read(chunk)#БЛАГОДАРЯ ЦИКЛУ ЧИТАЕМ ВЕСЬ ФАЙЛИК но в онце бует выдавать постоянно пустую строку
            if part:#если может прочитать то читает и записывает
                w.write(part)#записывает в новый файлик
            else:#если не возможно прочитать то прекращает работу и записывает 
                break
        end=time.time()#конец подсчета времени
print(end-start)
print("done!")

param=int(input("input max string value start from 35pcls.\n"))
while param <35:
    print("wrong value,try again")
    param=int(input("input max string value start from 35pcls.\n"))
    continue
with open ("13.02.2023/text.txt", 'r') as f:    
    with open("new_text.txt",'w') as new:#записываем сразу в новый файлик под указанным названим с переменной new
        for line in f:
            result=""
            while len(line)>param:
                if line[param]==" ":#если линия заканчивается на конец слова
                    result=line[:param]+"\n"# мы добавляем в конец строки разделение строк
                    line=line[param:].lstrip()# присваиваем строке значение от указанного параметра до разделения строки правого края     
                elif line[param-1]==" ":
                    w=line[:param-1].split()#если последний символ в строке это пробел
                    line=line[param:]
                    w[0]+=" "             
                    result=" ".join(w)+"\n"
                else:
                    w=line[:param].split()[:-1]
                    stub=line[:param].split()[-1]
                    line=line.replace(" ".join(w),"").lstrip()
                    y=0
                    z=0
                    while y<len(stub)+1:
                        if z>=len(w)-1:
                            z=0
                        w[z] += " "
                        y+=1
                        z+=1
                    result=" ".join(w)+"\n"
                if len(line)<=param:
                    result=line
                new.write(result)


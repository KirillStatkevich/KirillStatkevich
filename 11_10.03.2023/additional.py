global_var="test global value"

def print_global_var():
    print(global_var)

print(__name__)
if __name__=="__main__":#не запускает программу пока есть услове и глобальный скоуп(main) пропускает выполнение этой 
    #части. Работает как исполняемый модуль, а как подключаемый не отработает
    for i in range(100):
        print(i)
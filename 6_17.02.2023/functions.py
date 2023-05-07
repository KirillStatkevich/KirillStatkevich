def test_sum(a,b):#вызываем функцию с именем test_sum в которой есть 2 аргументы а и b
    res=a+b#условия функции
    return res#закрываем функцию
print(test_sum(2,4))#выводим результат функии(в скобках указываем аргументов величину)

def test_print(val):
    print(val)
test_print(test_sum(2,4))


def my_func1():
    print("my func 1")
    my_func2()#вызываем 2ю функцию
def my_func2():
    print("my func 2")
my_func1()#вынуждаем прогу сработать по функции

def order (x,y):
    print(f"{x}, {y}")
order("value1", "value2")
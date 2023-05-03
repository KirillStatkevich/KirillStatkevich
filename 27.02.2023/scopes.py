test_val="global value"

def test_scope():
    print(test_val)

def test_scope_2(test_val):
    print("test_val")

test_scope()#благодаря тому что scope находиться в функции она может прочитать все внешние файлы
test_scope_2("test value")
print(test_val)

l=[1,2,3]
def test_list_append():
    l.append(4)
test_list_append()
print(l)

def test_global():
    global test_val#можем поменять глобальную функцию через функцию global, nonlocal
    test_val="new global value"
test_global()
print(test_val)


def test_args_keywords(x,y):
    print(f"x:{x}, y:{y}")
test_args_keywords(y="value1",x="value2")#присвоили аргументам иные места

def test_args_keywords(x,y="test"):#если аргументу сразу указать параметр то можно указать только один параметр
    #но если все таки передать параметр будет использовано то которое было указано в конце
    print(f"x:{x}, y:{y}")
test_args_keywords("value x", "value y")

def sum(l):
    res=0
    for i in l:
        res+=1
    return res
print(sum([1,2,3,4,5]))

def sum(sign,*args):#*args позволяет использовать бесконечное количество аргументов
    res = args[0] if len(args)>0 else 0
    for i in args[1:]:
        if sign=="+":
            res+=i
        elif sign=="*":
            res*=i
    return res
print(sum("*",1,2,3,4,5))

def my_print(*args, sep=" ", end="\n") :
    print(*args, sep=sep,end=end)
my_print(1,2,3,4,5, sep=",", end=".\n")


def my_print(*args, **kwargs) :#kwargs key wards arguments позволяет ввести любое оличество аргументов по имени
    print(*args, sep=kwargs["sep"], end=kwargs["end"])
my_print(1,2,3,4,5, sep=",", end=".\n")
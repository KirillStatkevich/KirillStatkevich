# def say_hello():
# #     print("Hello!")# перенесли ниже

# def do_twice(func):
#     def wrapper():
#         func()
#         func()
#     return wrapper
# # double_say_hello=do_twice(say_hello)
# # double_say_hello()

# def do_hundred(func):
#     def wrapper():
#         for i in range(100):
#             func()
#     return wrapper

# @do_twice#то же самое что и закоменчено ниже
# def say_hello():
#     print("Hello!")

# say_hello=do_twice(say_hello)
# say_hello=do_hundred(say_hello)
# say_hello()

def command(func):
    def wrapper(*args,**kwargs):
        print("process is starting")
        res=func(args[0],args[1])
        print("process is over")
        global args_count#для интеграции в глобальное значение(на пример времени работы проги)
        args_count=len(args)
        return res#, args 2-ой вариант вывода инфы из декоратора
    return wrapper

@command
def sum(x,y):
    return x+y
@command
def cross(x,y):
    return x*y
print(sum(3,4))
print(cross(3,4))
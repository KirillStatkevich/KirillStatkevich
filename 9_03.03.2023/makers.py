#самый простой пример замыкания
def maker (n):
    def action(x):
               return x**n
    return action

cube=maker(3)
print(cube(4))

pw=[]
for i in range(1,101):
    pw.append(maker(i))#в функции maker/action указываем степень от 1 до 101
print([power(2) for power in pw])#указываем число которое будет возводиться в степень
#print([maker(i)(2) for i in range (1,101)])#тоже самое

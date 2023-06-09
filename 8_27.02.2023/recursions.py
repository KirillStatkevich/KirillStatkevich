#рекурсия-функция, которая вызывает сама себя

def level1():
    print("level 1 started")
    level2()
    print("level 1 finished")
def level2():
    print("\tlevel 2 started")
    level3()
    print("\tlevel 2 finished")
def level3():
    print("\t\tlevel 3 started")
    level4()
    print("\t\tlevel 3 finished")
def level4():
    print("\t\t\tlevel 4 started")
    print("\t\t\tlevel 4 finished")
#функция завершается только когда все функции на которые она ссылается будут завершены по цепочке
# level1()
def level(n=1):#пример рекурсии
    print(f"{'    '*(n-1)} level {n} started")
    if n==5:
        return
    level(n+1)
    print(f"{'    '*(n-1)} level {n} finished")
level()
print("the end")

#рекурсия

def print_10_times(text,i=0):
    if i ==10:
        return
    print(text)
    print_10_times(text,i+1)
print_10_times("test")
#!5=5*4*3*2*1-факториал 5
#!4=4*3*2*1
#!3=3*2*1
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

def digits_rem(num):
    if num==0:
        return 0
    return (num%10)+digits_rem(num//10)
print(digits_rem(1234))

def digits_str(num,i=0,res=0):
    str_num=str(num) if isinstance(num,int) else num
    if i==len(str_num):
        return res
    res+=int(str_num[i])
    return digits_str(str_num,i+1,res)
    
print(digits_str(1234))
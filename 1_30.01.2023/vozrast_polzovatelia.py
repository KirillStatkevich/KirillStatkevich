import datetime
min_age=18
user_age=input("enter your age in the format mm.yyyy:\n")
user_age=user_age.replace(" ","").replace(":","").replace(";","")#заменяем пробел пользователя на пустую строку
if len(user_age) !=7 or user_age[2]!=".": #если количество знаков не равно 7 или на 3 месте(индекс 2) не стоит точка то вырубаем
    print("youer input was in incorrect format")
    exit()
m_y=user_age.split(".")#разбиваем введенный возраст по точке
m=m_y[0]#присваиваем индексом 0 первое слово
y=m_y[1]#присваиваем индексом 1 второе слово
if not m.isnumeric() or not y.isnumeric():#проверка месяца и года на то, что пользователь ввел именно цифры digit-принимает все символьную математики(isnumeric/islower/isupper и тд)
    print("youer input was in incorrect format")
    exit()
m,y=int(m), int(y)#ПРИВОДИМ к цифферному варианту
if m>12:
    print("your input was in incorrect format")
    exit()

current_time=datetime.datetime.now()
c_m, c_y=current_time.month, current_time.year
if (c_y+(c_m/12))-(y+(m/12))>min_age:
    print("your get acsess")
else: 
    print("your too young for it")



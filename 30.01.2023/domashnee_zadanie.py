import datetime
key_time={1:"одна",2:"две",3:"три",4:"четыре",5:"пять",6:"шесть",7:"семь",8:"восемь",9:"девять",10:"десять",
11:"одинадцать",12:"двенадцать",13:"тринадцать",14:"четырнадцать",15:"пятнадцать",16:"шестнадцать",17:"семнадцать",
18:"восемнадцать",19:"девятнадцать",20:"двадцать",30:"тридцать",40:"сорок", 0:""}
h_time={1:"первого", 2:"второго",3:"третьего",4:"четвертого",5:"пятого",6:"шестого", 7:"седьмого",8:"восьмого"}
p_v=input("Вы хотите увидеть время текущее или произвести ввод? формат ввода: текущее\произвести ввод\n")
p_v.lower
if p_v=="1":
    p_v=datetime.datetime.now()
    m, h=p_v.minute, p_v.hour
elif p_v=="2":
    p_v=input("введите время в формате hh.mm\n")
    p_v=p_v.replace(" ",".").replace(":",".").replace(";",".").replace(",",".").replace("/",".")
    h_m=p_v.split(".")
    h=h_m[0]
    m=h_m[1]
    h=int(h)
    m=int(m)
    if len(p_v)!=5 or p_v[2]!=".":
        print("Вы ввели не верный формат данных")
        exit()
    h_m=p_v.split(".")
    h=h_m[0]
    m=h_m[1]
    if not h.isnumeric or not m.isnumeric:
        print("Вы ввели данные не верно")
        exit()
    h=int(h)
    m=int(m)
    if h>24 or  h<0:
        print("Вы ввели не существующие часовое время")
        exit()
    if m>60 or m<0:
        print("Вы ввели не существующие минутное время")
        exit()
    if h==0 and m==0:
        print("Полночь")
        exit()
else:
    print("вы ввели не верный формат данных")
    exit()
m_m,h_h=m,h
if m_m==0:
    h=key_time[h]
    m=key_time[m]
    print(f"{h} часов ровно")
elif m_m==30:
    h=key_time[h]
    m=key_time[m]
    if h_h>12:
        if h_h<5 or h_h==7 or h_h==8:
            h1=h_h+1
            h1=h_time[h1]
            print(f"половина {h1=}")
            exit()
        h_h=h_h+1
        print(f"половина {h1}")
    else:
        h_h=h_h+1
        h_h=key_time[h_h]
        print(f"половина {h[:-1]}ого")
elif m_m<30:
    h=key_time[h]
    m=key_time[m]
    if h_h==1 or h_h==2 or h_h==3 or h_h==4 or h_h==7 or h_h==8:
        h1=h_h+1
        h1=h_time[h1]
        print(f"{m} минут {h1}")
    else:
        h_h=h_h+1
        h_h=key_time[h_h]
        print(f"{m} минут {h_h[:-1]}ого")
elif m_m>30 and m_m<45:
    m1, m2=divmod(m,10)
    m1=m1*10
    m1=key_time[m1]
    m2=key_time[m2]
    if h_h==1 or h_h==2 or h_h==3 or h_h==4 or h_h==7 or h_h==8:
        h1=h_h+1
        h1=h_time[h1]
        print(f"{m1}{m2} минут {h1}")
    else:
        h_h=h_h+1
        h_h=key_time[h_h]
        print(f"{m1}{m2} минут {h_h[:-1]}ого")
elif m_m>=45:
    m=60-m
    m=key_time[m]
    h=h_h+1
    h=key_time[h]
    if h_h==1 or h_h==2 or h_h==3 or h_h==4 or h_h==7 or h_h==8:
        h=h_time[h]
        print(f"без {m} минут {h[:-1]}ого")
    else:
        print(f"без {m} минут {h[:-1]}ого")
else:
    print("я устал я ухожу")








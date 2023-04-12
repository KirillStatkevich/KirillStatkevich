import math
a = float(input("enter a\n"))
b = float(input("enter b\n"))
c = float(input("enter c\n"))
dis=b**2-(4*a*c)
if dis>=0:
    if dis==0:
        x=(-b)/(2*a)
        not print("dis=0 and x value is:") and print(x)
        y=(a*x**2)+(b*x)+c
        if y==0:
            print("it's clear")
        else:
            print("your wrong")
    if dis>0:
        x=((-b)+dis**(1/2))/(2*a)
        x1=((-b)-dis**(1/2))/(2*a)
        not print("dis>0 and x value is:") and print(x) 
        not print("x1 value is:") and print(x1)
        y=(a*x**2)+(b*x)+c
        if y==0:
            print("it's clear")
        else:
            print("your wrong")
else:
    print("dis<0 and it's false")

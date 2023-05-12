def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("can't divid by zero")
    except:
        print("something went wrong")
print(div(10,5))
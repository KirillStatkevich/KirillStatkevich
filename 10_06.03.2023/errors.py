x=10
y=0
def div(a,b):
    try:
        return a/b
    except:
        print("holy crap")

try:
    div(x,y)
except:
    print("ooops")
print("the end")
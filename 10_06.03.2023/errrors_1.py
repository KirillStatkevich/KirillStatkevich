l=[1,2,3,4,5]
def get(coll,i):
    return coll[i]

    

try:
    print("before starting")
    get(l,6)
    print("after starting")
except NameError:
    print("some variables does not exist")
except IndexError:
    print("some index does not exist")
print("the end")
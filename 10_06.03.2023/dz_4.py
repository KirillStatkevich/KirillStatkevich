import time
def ebuchaya_functia(func):
    def wrapper(*args):
        start=time.time()
        with open ("10_06.03.2023/test.txt","w") as f:
            f.write (f"Result of your function is:{func(*args)}\n working time your's program is: {time.time()-start}")
    return wrapper

def ebychee_yclovie(x,y):
    return x+y

ebychee_yclovie=ebuchaya_functia(ebychee_yclovie)
ebychee_yclovie(33,12)

# def ymnosh(x,y):
#     return x*y
# ymnosh=ebuchaya_functia(ymnosh)
# ymnosh(122,122)
def sum_dvoek():
    l=[1,2,3,4,5,6,7,8,9,10]
    try:
        print(sum([x for x in l if x%2==0]))
    except TypeError :
        print("you'r input argument is't int or is't list")
sum_dvoek()
num=input("input your values:\n")
def spisok():
    x=[]
    for i in num:
        if i not in x:
            x.append(i)
        continue
    x.sort()
    y=[]
    for i in x:
        if not y:
            y.append([i])
        elif int(i)-prev_x==1:
            y[-1].append(i)
        else:
            y.append([i])
        prev_x=int(i)
        final_ranges = ["-".join([y[0], y[-1]] if len(y) > 1 else y) for y in y]
    print(final_ranges)
spisok()
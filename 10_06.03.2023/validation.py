while True:
    t=input("input your time in format hh:mn\n")
    try:
        h,m=t.split(":")
        h,m=int(h),int(m)
        if h>23:
            raise RuntimeError ("the hours is too big")
        if m>59:
            raise RuntimeError ("the minutes is too big")
        break
    except ValueError:
        print("value error pleas try again!")
        continue
    except RuntimeError as e:
        print(e)
        continue
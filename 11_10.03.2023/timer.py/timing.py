import time

isrun=False

def start():
    global start_time
    global isrun
    isrun=True
    start_time=time.time()

def finish():
    global isrun
    if isrun:
        isrun =False
        return time.time()-start_time
    else:
        return -1
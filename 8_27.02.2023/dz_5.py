def fibonacci(num,num_time=0,value=0,first=1,second=2):
    if num>=num_time:
        value=first+second
        return fibonacci(num,num_time+1,value,first=second,second=value)
    if num<=num_time:
        print(value)
        return
    return fibonacci()
fibonacci(13)
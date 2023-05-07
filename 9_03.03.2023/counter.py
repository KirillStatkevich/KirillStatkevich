#счетчик кликов переходов или тп
def counter_base(n=0):
    def action():
        nonlocal n
        n+=1
        return n
    return action
from10=counter_base(10)
print(from10())
print(from10())
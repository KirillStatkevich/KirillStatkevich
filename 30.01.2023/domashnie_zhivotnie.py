import datetime
c, d, r ="cat", "dog", "rat"
template="a {}, a {} and a {}"
print(template.format(c, d, r))
print(f"a {c}, a {d} and a {r}")

print(str(datetime.datetime.now()))# для пользователя
print(repr(datetime.datetime.now()))# для разарботчика позволяет дальше использовать в работе
x= 25/4.9
print(f"the answer is {25/4.9:.1f}")# :.1f указывает количество занков после запятой

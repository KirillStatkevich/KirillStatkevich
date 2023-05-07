d={}
print(type(d),d)
d={"1":"один", "two":2, "three":3}
print(d)
print(d["1"])
d["new key"]="new value"#добавление нового ключа в существующий перечень
print(d)
d["one"]= 1.0 #заменяет ключ на указанное значение 
del d["new key"]# удаляет указанный ключ
print(d)
try:#создание блоков исключения
    raise IndexError("THe first level of indexerror")#оператор создания исключения
    print("the main logic")
except IndexError:
    raise IndexError("THe second level of indexerror")
else:
    print("everything is fine")
finally:#привязан к try и отрабатывает всегда
    print("finally")
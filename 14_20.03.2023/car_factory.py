#отношение агрегации
class Engine:

    def __init__(self,power,volume):
        self.__power=power
        self.__volume=volume

    def get_volume(self):
        return self.__volume
    
    def get_power(self):
        return (self.__power)
    
    power=property(get_power)
    volume=property(get_volume)

class SerialCar:

    def __init__(self,make,model,engine):
        self.__make=make
        self.__model=model
        self.__engine=engine

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_engine(self): #функция getr позволяет выводить необходимое значение из указанного стандарта
        return self.__engine
    
    def set_engine(self, engine):# благодаря setу мы корректирурем необходимые данные из указанного стандарта
        self.__engine=engine
    
    make=property(get_make)
    model=property(get_model)
    engine=property(get_engine,set_engine)


class SuperCar:
    def __init__(self,make,model,power,volume):
        self.__make=make
        self.__model=model
        self.__engine=Engine(power,volume)

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model
    
    def get_power(self):
        return self.__engine.power

    def get_volume(self):
        return self.__engine.volume
    
    make=property(get_make)
    model=property(get_model)
    volume=property(get_volume)
    power=property(get_power)

v4=Engine(100,2.0)#создаем двигатель под стандартную машину
vw=SerialCar("VW","Golf", v4)#указываем стандартную машину
print(vw.make,vw.model,vw.engine.power, vw.engine.volume)

v8=Engine(200,4.0)#создаем новый двигатель подстандартную машину
vw.engine=v8
print(vw.make,vw.model,vw.engine.power, vw.engine.volume)

s=SuperCar("Ferrari","la Ferrari",300,12)
print(s.make,s.model,s.power,s.volume)

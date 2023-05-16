class Dog:

    def __init__(self,name,breed,color,vaccine_exp):#сюда передаются все объеденяющие с остальными параметры какого-то обьекта
        #и логику создания атрибутов    #если необходимо конкретизация то она в классе не пишется
        self.name=name
        self.breed=breed
        if breed=="wss":
            self.color="white"
        else:
            self.color=color
        self.vaccine_exp=vaccine_exp
        # self.__vaccinated=vaccinated
        # self.__vaccine_exp=vaccine_exp

    def say_hello(self):
        print(f"Hello, my name is {self.name} and i'm {self.color}")
    
    
    def get_vaccine_exp(self):#изменение внутри класса
        if self.__vaccinated:
            return self.__vaccine_exp
        else:
            return
        
    def set_vaccine_exp(self,year):#присваивание внутри класса
        self.__vaccine_exp=year
        self.__vaccinated=True
    
    vaccine_exp=property(get_vaccine_exp,set_vaccine_exp)#связываем несколько функций в рамках одного и того же атрибута
    


psina=Dog("Zephyrka","Wss","white",2024) # создаем новую собаку с определенной моделью поведения
# psina.init("Zephyrka","Wss","white",True,2024) # указываем параметры собаки(name,breed,color)
psina.say_hello()

# внутри инкапсуляции ничего менять нельзя, а для закрепления используется __! но если очень хочется то _Dog__color

dog=Dog("Sharik","n/a","black",2024)
# dog.init("Sharik","n/a","black")
dog.say_hello()

print(dog)
print(dog.vaccine_exp)
dog.vaccine_exp=2025

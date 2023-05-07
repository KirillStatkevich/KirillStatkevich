def prepare():
    print("starting a new pizza")
    print("preparing a base")
    print("adding some sauce")

def add_ingridient(ingr):
    print(f"adding {ingr}")

def grind_cheese():
    print("griding cheese")

def bake(temp,time):
    print(f"baking at {temp} for {time} minutes")

def done():
    print("boxing")
    print("slicing")
    print("done!")

# def make_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake(200,5)
#     done()
# make_pepperoni()

#            замыкание
def pizza_factory(temp,time,*ingrs):
    def factory_method():
        prepare()
        for ingr in ingrs:
            add_ingridient(ingr)
        grind_cheese()
        bake(temp,time)
        done()
    return factory_method
make_pepperoni = pizza_factory(200,5,"pepperoni")
make_double_pepperoni = pizza_factory(200,5,"pepperoni","pepperoni")
make_shimp_pizza=pizza_factory(175,7,"pepperoni","chrimp")
make_double_pepperoni()
make_shimp_pizza()
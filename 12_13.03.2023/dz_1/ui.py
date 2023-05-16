import main

def view_libr():
    output=main.get_all_films()
    print_output(output)

def add_film():
    data_1=input("input your film in format:\n Title,Director,Year,Genre\n")
    data_1=data_1.split(",")
    data_1=tuple(data_1)
    data=[]
    data.append(data_1)
    main.additer(data)
    print("Done! Your's film added at the collection")

def searcher():
    key=input("what are u searching for?\n")
    output=main.search_func(key)
    print_output(output)
   

def print_output(output):
    print(output if output else "no such films")

def main_logic():
    answ=True
    while True:
        print("\nselect an item from the menu:")
        print("1.browse all films\n2.Get film\n3.Add film\n4.Exit")
        answer=input()
        if answer=="1":
            view_libr()
        elif answer=="2":
            searcher()
        elif answer=="3":
            add_film()
        elif answer=="4":
            print("Good Luck!")
            break
        else:
            print("\n Wrong input,try again")





main_logic()

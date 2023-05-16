import oop_logic 
logic=oop_logic.PhooneBookManager()

def get_all_records():
    output=logic.get_all_records()
    print_output(output)
    # print(output if output else "no records")#если в outpute что-то есть то выведетБ если нет то no records


def get_record():
    name=ask_for_name()
    output=logic.get_record_by_name(name)#передаем name в качестве искомового параметра в logic
    print_output(output)

def add_record():
    name=ask_for_name()
    numbers=ask_for_numbers()
    logic.add_record(name, numbers)
    get_all_records()

def ask_for_name():
    return input("input the name:\n")

def ask_for_numbers():
    while True:
        numbers=input("Enter the 7-digit numbers separated by comma\n")
        numbers=numbers.split(",")
        for i in numbers:
            if len(i) !=7 or not i.isdigit():
                continue
        return numbers

def print_output(output):
    print(output if output else "no records")


def main_cycle():
    while True:
        print("\nselect an item from the menu:")
        print("1.browse all records\n2.Get record\n3.Add record")#дает пользователю выбрать необходимый вариант исходя из
        #имеющихся фунцкий в logic
        answer=input()
        if answer=="1":
            get_all_records()
        elif answer == "2":
            get_record()
        elif answer =="3":
            add_record()
        else:
            pass

main_cycle()
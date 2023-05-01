import json # java script object natation(запись бьекта в js(испльзуются только квадратные скобки) самый популярныйформат передачи данных
import pickle #только пайтоновская функция структурирует данные в бинарный формат
#pickle учитывает все обьекты и все типы данных нужно для хранения на своем пк и только на своем пк
import csv#coma separeted values-значения разделенные запятой похоже на таблицы
#начальная версия баз данных открывается в exsel
#urlopen делает запрос на сайт и получить от туда разметку
keys = ["make", "model", "volume", "power", "year", "id"]

data = [    
	("Honda", "Civic", 1.5, 174, 2021, "honda_civic_2021"),
	("Toyota", "Corolla", 2.0, 169, 2022, "toyota_corolla_2022"),
    ("Ford", "Mustang", 5.0, 460, 2021, "ford_mustang_2021"),
    ("Chevrolet", "Camaro", 6.2, 455, 2022, "chevrolet_camaro_2022"),
    ("Dodge", "Charger", 3.6, 292, 2021, "dodge_charger_2021"),
    ("Nissan", "Altima", 2.5, 188, 2022, "nissan_altima_2022"),
    ("Mazda", "CX-5", 2.5, 187, 2021, "mazda_cx5_2021"),
    ("Subaru", "Impreza", 2.0, 152, 2022, "subaru_impreza_2022"),
    ("BMW", "M3", 3.0, 473, 2021, "bmw_m3_2021"),
    ("Mercedes-Benz", "C-Class", 2.0, 255, 2022, "mercedes_cclass_2022")
]
# data=json.dumps(data)#выгружаем данные в консоль в виде строки
#dump, load-dump выгрузка в json,load-выгрузка из jsona
#dumps-выгрузка в строку
# print(data)
# data=json.loads(data)#загружаем обратно в json
# print(data)
res=[]
for car_data in data:
    car_dict={}
    for i in range(len(keys)):
        car_dict[keys[i]]=car_data[i]
    res.append(car_dict)
# print(res)
with open("24.02.2023/carrs.json","w") as f:
    json.dump(res,f)

data=pickle.dumps(data)
print(data)
data=pickle.loads(data)#благодаря pickle сохраняются все типы данных
print(data)

my_print=pickle.dumps(print)#сохраняем функцию print в бинарном состоянии
my_print=pickle.loads(my_print)#
my_print("hello", "from", my_print)#теперь my_print отрабатывает как функция print
with open("24.02.2023/cars.pickle","wb") as f:#создали файлик в бинарном понятии
    pickle.dump(res,f)

with open("24.02.2023/cars.csv","w", newline="") as f:#создаем файлик формата csv newline="" удаляет лишние пустые enterы
    writer=csv.writer(f)#f-указатель на файлик, writer-
    writer.writerow(keys)#writerow-одна строка(row)
    for c_d in data:
        writer.writerow(c_d)#создали новый файлик в котором все структурровано по столбцам и таблицам
# with open("24.02.2023/cars.csv","r", newline="") as f:#открываем созданный файл в режиме чтения
#     reader=csv.reader(f)
#     for row in reader:#читаем и выводим каждую строку
#         print(row)
with open("24.02.2023/cars.csv","r", newline="") as f:#открываем созданный файл в режиме чтения
    reader=csv.DictReader(f)#читает файлик как словари(сопостовляет оглавления колонок с текстом)
    for row in reader:#читаем и выводим каждую строку
        print(row)


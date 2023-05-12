# import additional

# from additional import global_var, print_global_var#вызваные функции находяться в текущем файле но не пересекаются в 
# файле, лучше использвать глобальный импорт. Добавляя в конце as (что-то) используем как конретную переменную. 

from additional import *  #импортирует все денные из пути полность в данный скоп со всеми данными 
# но без связи с основными файлами

# print(additional.global_var)
# additional.global_var="new value" #можно менять значения глобальных переменных, без вмешательства в основной файл
# если список или словарь то можно крутеть вертеть как хочешь
# additional.print_global_var()
global_var="test"#присвоили переменной другое значение
gv="new value"
print(gv)
print_global_var()
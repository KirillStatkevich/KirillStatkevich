def read_text(text,tipe):
    try:  
        with open(text,tipe) as f:
            s=f.read()
            return s
    except FileNotFoundError:
        print("Файл не найдет или его не существует.")

print(read_text("10_06.03.2023/text.txt","r"))
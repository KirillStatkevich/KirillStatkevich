import csv

def additer(data):
    with open("12_13.03.2023/dz_1/result.csv","a", newline="", encoding="utf-8") as f:
        writer=csv.writer(f)
        for c_d in data:
            writer.writerow(c_d)


def get_all_films():
    with open("12_13.03.2023/dz_1/result.csv","r", encoding="utf-8") as f:
        return "".join([row for row in f])



def search_func(key):
    with open("12_13.03.2023/dz_1/result.csv","r", encoding="utf-8") as f:
        while True:
            return "".join([reader for reader in f if key in reader])

import csv

def get_info_from_csv(filename):
    data = list()
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            data.append(row)
    data = tuple(data)
    return data
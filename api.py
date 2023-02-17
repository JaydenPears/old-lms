import os
# Задел под парсинг при исправленных файлах
directory = 'courses-description'
addressess = set()
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        name_of_file = f.split('\\')[-1]
        type_of_activity = name_of_file[name_of_file.index('-') + 1:name_of_file.index('.')]
        data = [elem.strip().split('\t') for elem in open(f, 'r', encoding="utf8").readlines()[1::]]
        for info in data:
            info_for_course = info[1]
            age_limit = info[4]
            cost = info_for_course[info_for_course.rfind('(') + 1: info_for_course.rfind(')')]
            info_for_course = info_for_course[:info_for_course.rfind('(')].strip()
            address = info_for_course[info_for_course.rfind('(') + 1:info_for_course.rfind(')')]
            if ' - ' in address:
                if address.split(' - ')[-1][-1] == ")":
                    address = address.split(' - ')[-1]
                    address = address[:len(address) - 1]
                    addressess.add(address)
                else:
                    addressess.add(address.split(' - ')[-1])
print(addressess)

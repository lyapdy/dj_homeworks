import csv
import os
import pathlib

root = pathlib.PurePath(__file__).parent.parent
file = 'phones.csv'
path = os.path.join(root, file)


class Phones:
    def __init__(self, path=path):
        self.path = path
        pass
    
    def handle(self, *args, **options):
        phones_list = []
        path = self.path
        with open (path, 'r', encoding='utf-8') as data_file:
            reader = csv.reader(data_file, delimiter=';', escapechar = '\\')
            for row in reader:
                dic = {}
                dic['name'] = row[1]
                dic['price'] = row[3]  
                dic['image'] = row[2]
                dic['release_date'] = row[4]
                dic['lte_exists'] = row[5]
                phones_list.append(dic)
        return (phones_list[1:])
        

# sumsumg = Phones()

# print(sumsumg.handle())
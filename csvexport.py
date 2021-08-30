from random import randrange

import csv



class Contacts():
    # def __init__(self, dic_name):
    #     self.dic_name = dic_name
    def __init__(self, dic_name):
        self.dic_name = dic_name
        dictionary = {
                    'header': ['Name', 'Number']
                }
        self.dictionary = dictionary
        print(self.dic_name)

    def local_save(self):
        # header = self.dictionary['header']
        with open('/home/roman/Temp/temp.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.dictionary['header'])
            for each in self.dictionary.keys():
                if each == 'header':
                    continue
                writer.writerow(self.dictionary[each])

    def get(self):
        print(self.dictionary)


    def add(self, *args ):
        
        id = randrange(1000)
        for k in self.dictionary.keys():
            if k != id:
                continue
            else:
                id = randrange(1000)
        
        values = []
        for value in args:
            values.append(value)
        self.dictionary[id] = values

        return id
        


    def update(self, id, *args):
        n = 0
        for arg in args:
            if self.dictionary[id][n]:
                self.dictionary[id][n] = arg
        

        


    def delete(self, id):
        self.dictionary.pop(id, "Not in this dictionary")

user1 = Contacts('user1')
k = user1.add('roman', '65646846846')
user1.get()
user1.update(k, 'admin')
user1.get()
# user1.delete(k)
user1.get()
user1.local_save()

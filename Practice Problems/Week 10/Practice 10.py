import csv

# Get data from csv file
with open('real_estate.csv','r') as f:
    data = csv.reader(f)
    l = []
    for i in data:
        l.append(i)
    l.pop(0)

print(l)

# Create House class


# class House:
#
#     def __init__(self, info):
#         self.info = [name, street, type, size, floors, bedrooms, bathrooms, lot_siz, parking, facing, age, taxes, self.price]
#         self.info[0] = name
#         self.info[1] = street
#         self.info[2] = type
#         self.info[3] = size
#         self.info[4] = floors
#         self.info[5] = self.bedrooms
#         self.info[6] = self.bathrooms
#         self.info[7] = self.lot_size
#         self.info[8] = self.parking
#         self.info[9] = self.facing
#         self.info[10] = self.age
#         self.info[11] = self.taxes
#         self.info[12] = self.price
#
#     def __str__(self):
#         return str(self.info[0]) + str(self.info[1]) + str(self.info[2]) + str(self.info[3]) + str(self.info[4]) + str(self.info[5]) + str(self.info[6]) + str(self.info[7]) + str(self.info[8]) + str(self.info[9]) + str(self.info[10]) + str(self.info[11]) + str(self.info[12])
#
#
# h1 = House(l)
# print(h1)


import csv
streets = []
street = ''
while street != 'exit':
    street = input('Enter a street name (type exit when done): ')
    if street != 'exit':
        streets.append(street)

print(streets)

with open('real_estate.csv', 'r') as f:
    data = csv.reader(f)
    print(data)  # A pointer
    l = []
    it = 0
    for b in data:
        if it != 0
            listing = {}
            listing['number'] = b[0]
            listing['street'] = b[1]
            listing['price'] = b[12]
            l.append(listing)
        else:
            it += 1
print(l)

diction = {}












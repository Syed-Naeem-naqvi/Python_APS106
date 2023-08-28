OrigonalStory = ''

animal = input('Enter an animal: ')
food = input('Enter a food: ')
city = input('Enter a city: ')

OrigonalStory.replace('{animal}', animal)
OrigonalStory.replace('{food}', food)
OrigonalStory.replace('{city}', city)

print(OrigonalStory)
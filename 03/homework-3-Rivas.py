print("Paolo Rivas")
country= ["Brasil", "USA", "Argentina", "Netherlands", "France", "Marrocco", "Spain"]
print(country)
#question 2
for each_country in country:
    print(each_country)
#question 3
sorted_country= sorted(country)
print(sorted_country)
#question 4
print(sorted_country[0])
#question 5
second_to_last= sorted_country[-2]
print(second_to_last)
#question 6
sorted_country.remove("Brasil")
print(sorted_country)
#question 7
for each_country in sorted_country:
    print(each_country)

#DICTIONARIES
#question 1
tree= {'name':'Drago milenario', 'species':'Dracaena draco', 'age': 15, 'location_name':'Icod de los Vinos, Tenerife', 'latitude':28.20, 'longitude':16.42}
#question 2
print("My name is ",tree["name"], "a ",tree["age"], "years old tree that is located in ",tree["location_name"])
#question 3
NYC= {'latitude': 40.7128}
if tree['latitude']< NYC['latitude']:
    print("The ",tree["name"], "in ",tree["location_name"], "is south of NYC")
else:
    ("The ",tree["name"], "in ",tree["location_name"], "is north of NYC")
#question 4
age= input("How old are you?")
if int(age)>= 15:
    print("You are ",((15- int(age))* -1), "years older than ", tree['name'])
else:
    print("You are ",(15- int(age)), "years younger than ", tree['name'])


#List of Dictionaries
#I am assigning postive number to North latitudes and west longitudes.
#South and east would be consider a negative value in this scope.
dictionaries= [{'name':'Moscow', 'latitude': 5545, 'longitude': -3737},
{'name':'Tehran', 'latitude': 3541, 'longitude': -5125},
{'name':'Falkland Island', 'latitude': -5142,  'longitude': 5751},
{'name':'Seoul', 'latitude': 3734,'longitude': -1265},
{'name':'Santiago', 'latitude': -3327, 'longitude': 7040}]

for x in dictionares (y for y in dictionaries['latitude'] if y > 0):
print('-', x['name'])

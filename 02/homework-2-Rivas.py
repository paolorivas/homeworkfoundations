print("Paolo Rivas")
print("2016-05-25")
print("homework 2")

#lISTS

numbers= [22, 90, 0, -10, 3, 22, 48]
print(numbers)
#Display the 4th element of this list.
print(numbers[3])
#Display the sum of the 2nd and 4th element of the list.
print(numbers[1]+numbers[3])
#second largest number
largest = numbers[0]
second_largest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > second_largest:
        second_largest = numbers[i]
    if numbers[i] > largest:
        tmp = second_largest
        second_largest = largest
        largest = tmp
print(second_largest)
#Display the last element of the original unsorted list
print(numbers[-1])
#excersise 6
for anyelement in numbers:
    if anyelement< 10:
        print(anyelement*30)
    elif anyelement% 2 == 0:
        print(anyelement+ 6)
    elif anyelement> 50:
        print(anyelement- 10)
    elif anyelement != -10:
        print(anyelement- 1)
#Sum the result of each of the numbers divided by two.
myInt= 2
numbers[:] = [x / myInt for x in numbers]
print(numbers[:])

#DICTIONARIES
#Define a new dictionary
movie= {'name':'titanic', 'year':'1997', 'director':'James Cameron', 'budget': 2000000000}

print ("My favorite movie is", movie['name'], "which was released in", movie['year'], "and was directed by", movie['director'])
#excersise 9
movie['revenue']= 2185372302
utilities= movie['revenue']-movie['budget']
print("Titanic total utilities were", utilities)
#excersise 10
if movie['revenue']< movie['budget']:
    print("This movie was a flop")
elif movie['revenue']>= (movie['budget']*5):
    print("This movie was a good investment")
else:
    print("This was not a bad nor good investment")
#excersise 11
NYCpeople= {'Manhattan':1600000 , 'Brooklyn':2600000, 'Bronx':1400000, 'Queens':2300000, 'Staten Island':470000}
#excersise 12
print(NYCpeople['Brooklyn'])
#excersise 13
total=(int(NYCpeople['Manhattan'])+int(NYCpeople['Brooklyn'])+int(NYCpeople['Bronx'])+int(NYCpeople['Queens'])+int(NYCpeople['Staten Island']))
print(total)
#excersise 14
porcentaje=(NYCpeople['Manhattan']/total)*100
print("Manhattan represents a", porcentaje, "%")

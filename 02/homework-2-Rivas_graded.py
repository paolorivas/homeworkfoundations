# Grade: 12.5 / 15

print("Paolo Rivas")
print("2016-05-25")
print("homework 2")

#lISTS

numbers= [22, 90, 0, -10, 3, 22, 48]
print(numbers)

# TA-COMMENT: (-1) You missed a question! You were supposed to display the number of elements in your list.

#Display the 4th element of this list.
print(numbers[3])
#Display the sum of the 2nd and 4th element of the list.
print(numbers[1]+numbers[3])
#second largest number

# TA-COMMENT: This is really complicated! And to be honest, the code below is a bit hard to follow. There's a much easier solution -- you could have just sorted the list and then printed the second element.
largest = numbers[0]
second_largest = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > second_largest:
        second_largest = numbers[i]
    if numbers[i] > largest:
        tmp = second_largest
        second_largest = largest
        largest = tmp

# TA-COMMENT:

print(second_largest)
#Display the last element of the original unsorted list
print(numbers[-1])
#excersise 6

# TA-COMMENT: (-1) You shouldn't use elif's all the way down for this logical structure -- for example, you want certain calculations to occur only if TWO conditions are true. For example, a number can be less than 10 AND even (but in the code below, only one of the conditions will run).
for anyelement in numbers:
    if anyelement< 10:
        print(anyelement*30)
    elif anyelement% 2 == 0:
        print(anyelement+ 6)
    elif anyelement> 50:
        print(anyelement- 10)
    elif anyelement != -10:
        print(anyelement- 1)

# TA-COMMENT: This is a potential solution to Question 6:

for number in numbers:
	original = number

	if original < 10:
		number = number * 30

		if (original%2) == 0:
			number = number + 6

	elif original > 50:
		number = number - 10

	if original != -10:
		number = number - 1

	print(number)


#Sum the result of each of the numbers divided by two.

myInt= 2
numbers[:] = [x / myInt for x in numbers] # TA-COMMENT: This is a list comprehension! Note that you don't have to use the '[:]' notation on numbers. Also, you didn't need to store 2 inside a variable, you could've used it directly in your list comprehension.

print(numbers[:]) # TA-COMMENT: (-0.5) You didn't sum the numbers!

#DICTIONARIES
#Define a new dictionary
movie= {'name':'titanic', 'year':'1997', 'director':'James Cameron', 'budget': 2000000000}

print ("My favorite movie is", movie['name'], "which was released in", movie['year'], "and was directed by", movie['director'])
#excersise 9
movie['revenue']= 2185372302
utilities= movie['revenue']-movie['budget']
print("Titanic total utilities were", utilities)
#excersise 10

# TA-COMMENT: Good job!
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

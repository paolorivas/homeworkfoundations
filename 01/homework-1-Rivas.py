print("Paolo Rivas Legua")
print("05"+"/16"+"/2016")
print("homework "+str(1))
name= input("what is your name mate?")
print("hello, " + name)
year_of_birth= input("what year were you born?")
age=2016-int(year_of_birth)
print("you are "+str(age)+" years old")

#According to cardio-research.com, the average heart of a human being beats 72bpm.
#A blue whale’s heart beats six times a minute and a rabbit has 205bpm.
#A single calendary year is most likely to have 525,600 minute. All calculations are
#based on a regular mean. Standard deviation are not being weight.

heartbeat=int(age)*32843200
heartbeat2=int(heartbeat)/1000000
print("Your hearth has most likely bitten arround "+str(heartbeat2)+" millions times since you were born")
whalebeat=int(age)*3153600
whalebeat2=int(whalebeat/1000000)
print("Which is the equivalent of "+str(whalebeat2)+" millions on beats on average of a blue whale")
rabbitbeat=int(age)*10774800
rabbitbeat2=int(rabbitbeat)/1000000000
print("and aproximately "+str(rabbitbeat2)+" billions heartbeats of a rabbit, if they would have your age.")
print("keep it pumping!")

#according to universetoday.com, the planet venus takes 0.61 earth years to go arround the sun
# and neptuno takes 164.79 years compared to a calendar round of the planet earth.

venusage=int(age)*0.61
neptunoage=int(age)*167.4
print("If you were living in the planet venus your age would have blown "+str(venusage)+" candles")
print("On the other hand, in Neptuno you would be an experienced "+str(neptunoage)+" years old human. Impresive.")
age3=int(age)-27
age2=(int(age)-27)*-1
if age==27:
    print(" Be careful if you are a rockstar. like me, you might die and be part of the 27 club!")
if age<27:
    print("You are younger than me")
else:
    print("according to our year of birth, we are "+str(age3)+" years apart")
if age>27:
    print("You are older than me")
else:
    print("According to our year of birth, we are "+str(age2)+" years apart")
test = int(age)%2
if test==0:
	print ("your age is an even number.")
if test ==1:
	print ("your age is an odd number.")
age4=2016-int(age)
if age4>=2009:
    print("You´ve only been alive for 1 superbowl tittle of the Pittsburgh Steelers")
if 2009>age4>=2006:
    print("You´ve only been alive for 2 superbowl tittle of the Pittsburgh Steelers")
if 2006>age4>=1980:
    print("You´ve only been alive for 3 superbowl tittle of the Pittsburgh Steelers")
if 1980>age4>=1979:
    print("You´ve only been alive for 4 superbowl tittle of the Pittsburgh Steelers")
if 1979>age4>=1976:
    print("You´ve only been alive for 5 superbowl tittle of the Pittsburgh Steelers")
if 1976>age4>=1975:
    print("You´ve only been alive for 6 superbowl tittle of the Pittsburgh Steelers")
if 1933<=age4<1945:
    print("Franklin D. Roosevelt was president the moment you were born")
if 1945<=age4<1961:
    print("Dwigth D. Eisenowards was president the moment you were born")
if 1961<age4<1963:
    print("John F. Kennedy was president the moment you were born")
if 1963<=age4<1969:
    print("Lyndon B. Johnson was president the moment you were born")
if 1969<=age4<1974:
    print("Richard Nixon was president the moment you were born")
if 1974<=age4<1977:
    print("Gerald Ford was president the moment you were born")
if 1977<=age4<1981:
    print("James Carter was president the moment you were born")
if 1981<=age4<1989:
    print("Ronald Reagan was president the moment you were born")
if 1989<=age4<1993:
    print("Goerge H. Bush was president the moment you were born")
if 1993<=age4<2001:
    print("Bill Clinton was president the moment you were born")
if 2001<=age4<2008:
    print("Goerge W. Bush was president the moment you were born")
if 2009<=age4<2016:
    print("Barack Obama was president the moment you were born")

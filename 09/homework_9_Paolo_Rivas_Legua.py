
# coding: utf-8

# In[328]:

#test diccionary
earthquake = {
      'rms': '1.85',
      'updated': '2014-06-11T05:22:21.596Z',
      'type': 'earthquake',
      'magType': 'mwp',
      'longitude': '-136.6561',
      'gap': '48',
      'depth': '10',
      'dmin': '0.811',
      'mag': '5.7',
      'time': '2014-06-04T11:58:58.200Z',
      'latitude': '59.0001',
      'place': '73km WSW of Haines, Alaska',
      'net': 'us',
      'nst': '',
      'id': 'usc000rauc'}


# In[329]:

#    print(eq_to_sentence(earthquake))


# In[330]:

#A DEPTH POWER, MAGNITUDE earthquake was reported DAY TIME_OF_DAY on DATE LOCATION.


# ### Question 1

# In[331]:

def depth_to_words(x):
    if 0 < int(x['depth']) < 70:
        return "A shallow"
    elif 70 < int(x['depth']) < 300:
        return "An intermediate"
    elif 300 < int(x['depth']) < 700:
        return "A deep"
    else:
        return "didn't work"

#test 
#x = earthquake 
print(depth_to_words(x))


# In[332]:

def magnitude_to_words(x):
    if 0 < float(x['mag']) < 6:
        return "shallow to moderate"
    elif 6 < float(x['mag']) < 8:
        return "strong to mayor"
    elif 8 < float(x['mag']):
        return "a great"
    
#Test 
print(magnitude_to_words(x))


# In[333]:

get_ipython().system('pip install dateutils')


# In[334]:

import dateutil.parser
timestring = x['time']
yourdate = dateutil.parser.parse(timestring)

def day_in_words(x):
    return yourdate.strftime("%A")

#Test
day_in_words(x)


# In[335]:

def time_in_words(x):
    if 5 < yourdate.hour <=12:
        return str(yourdate.hour)+" "+"in the morning"
    elif 1 <= yourdate.hour < 5:
        return str(yourdate.hour)+" "+"in the afternoon"
    elif 5 <= yourdate.hour < 9:
        return str(yourdate.hour)+" "+"in the evenning"
    elif 9 <= yourdate.hour < 12:
        return str(yourdate.hour)+" "+"in the night"
    
#test   
time_in_words(x)


# In[336]:

def date_in_words(x):
    return yourdate.strftime("%b %d")

#test
date_in_words(x)


# ### Question 2

# In[337]:

#"A DEPTH DESCRIPTION, MAGNITUDE earthquake was reported DAY TIME_OF_DAY on DATE LOCATION."

def equeation_bah(x):
    return str(depth_to_words(x))+" "+str(x['depth'])+" "+"km"+" "+"depth"+" "+"and"+" "+str(x['mag'])+" "+"degree"+" "+str(magnitude_to_words(x))+" "+"earthquake"+" "+"was reported"+" "+time_in_words(x)+" "+"of"+date_in_words(x)+" "+"at"+" "+x['place']     


# In[338]:

print(equeation_bah(earthquake))


# ### Question 3

# In[339]:

#set up
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[340]:

earthquakes_df = pd.read_csv("1.0_month.csv")
earthquakes = earthquakes_df.to_dict('records')


# In[341]:

earthquakes_df


# In[342]:

earthquakes


# In[343]:

for y in earthquakes:
    if y['mag'] >= 4:
        print(equeation_bah(y))


# In[344]:

#if the earthquake is anything other than an earthquake (e.g. explosion or quarry blast), print
# There was also a magnitude MAGNITUDE TYPE_OF_EVENT on DATE LOCATION.
# For example,
# There was also a magnitude 1.29 quarry blast on June 19 12km SE of Tehachapi, California.
# with TYPE_OF_EVENT being explosion, quarry blast, etc and LOCATION being 'place' - e.g. '0km N of The Geysers, California'.


# In[345]:

def magnitude_type_of_event(x):
    return x['type']
#Test
magnitude_type_of_event(x)


# In[349]:

def equeation_bah2(x):
    mag = x['mag']
    place = x['place']
    return "There was also a"+" "+str(mag)+" "+magnitude_type_of_event(x)+" "+"on"+" "+time_in_words(x)+" "+"of"+" "+date_in_words(x)+" "+"at"+" "+place   


# In[350]:

#test
equeation_bah2(x)


# In[363]:

print(type(earthquakes))
for item in earthquakes:
    if item['mag'] >= 4:
        print(equeation_bah(item))
    if item['type'] != "earthquake":
        print(equeation_bah2(item))
        


# In[ ]:




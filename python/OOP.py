### OBJECT ORIENTED PROGRRAMMING ###

## "Class" is a set or category of things having some property or attribute
## in common and differentiated from others by kind, type, or quality.
## In technical terms we can say that class is a blue print for
## individual objects with exact behaviour.

## "Object" is one of instances of the class which can perform
## the functionalities which are defined in the class.

## "self" represents the instance of the class.
## By using the "self" keyword we can access the attributes & methods
## of the class in python.

## "__init__" is a reseved method in python classes.
## It is known as a constructor in object oriented concepts.
## This method called when an object is created from the class and
## it allows the class to initialize the attributes of a class.

## How can we use  "__init__ " ?
## Example: you're creating a NFS game for that we should have a car.
## Car can have attributes like "color", "company", "speed_limit" etc.
## and methods like "change_gear", "start", "accelarate", "move" etc.

class Kilim:
   def __init__(self, genislik, yukseklik, birim_maliyet=1):
       self.genislik = genislik
       self.yukseklik = yukseklik
       self.birim_maliyet = birim_maliyet
   
   def cevre_hesapla(self):
       return 2 * (self.genislik + self.yukseklik)
   
   def alan_hesapla(self):
       return self.genislik * self.yukseklik
   
   def maliyet(self):
       alan = self.alan_hesapla()
       return alan * self.birim_maliyet

kucuk_kilim = Kilim(1,2)
kucuk_kilim.genislik        #returns 1
kucuk_kilim.yukseklik       #returns 2
kucuk_kilim.birim_maliyet   #returns 1 (by default)
kucuk_kilim.cevre_hesapla()         #returns 6 
kucuk_kilim.alan_hesapla()          #returns 2
kucuk_kilim.maliyet()               #returns 2

iran_kilim = Kilim(3,5,4)
iran_kilim.genislik        #returns 3
iran_kilim.yukseklik       #returns 5

iran_kilim.birim_maliyet   #returns 4
iran_kilim.cevre_hesapla()         #returns 16 
iran_kilim.alan_hesapla()          #returns 15
iran_kilim.maliyet()               #returns 60


#####################################
## The most basic Python class
class User:   #this class does nothing!
  pass        #a class must have at least 1 line!

'''STYLE GUIDE FOR PYTHON (PEP8)
fieldnames should be lowercase with words separated by underscores!
'''
user1 = User() #the user1 is an "INSTANCE" of User "CLASS"
user1.first_name = "Frank"      #FIELD
user1.second_name = "Sinatra" #FIELD
print(user1.first_name) #will return Ali!

user2 = User() #the user1 is an "INSTANCE" of User "CLASS"
user2.age = "20"      #FIELD
user2.sex = "Male" #FIELD

#####################################
## INIT METHOD ('Initialization' a.k.a 'Constructor')
class User:
  '''This is a "DOCSTRING"!
  It includes fundamental information
  about this class!
  If you run 'help(User)'
  You'll get this DOCSTRING!

  Methods defined here:
  __init__(self,full_name,birthday)

  ---------------------------------

  Data descriptors defined here:

  __dict__
    dictionary for instance variables (if defined)

  __weakref__
    list of weak references to the object (if defined)
  '''

  def __init__(self, full_name, birthday):
    #Stores Value - Provided Value
    self.name     = full_name
    self.birthday = birthday #yyyymmdd

    #Extract the first and last names
    name_parts = full_name.split(" ")
    self.first_name = name_parts[0]
    self.last_name = name_parts[1]

  def age(self):
    '''Return the age of the user in years'''
    today = datetime.date(2020,12,12)
    yyyy = int(self.birthday[0:4])
    mm = int(self.birthday[4:6])
    dd = int(self.birthday[6:8])
    dob = datetime.date(yyyy,mm,dd) #Date of Birth
    age_in_days = (today-dob).days
    age_in_years = age_in_days/365
    return int(age_in_years)


user = User("Frank Sinatra", "19151212")
print(user.name)        #Frank Sinatra
print(user.first_name)  #Frank
print(user.last_name)   #Sinatra
print(user.birthday)    #19151212
print(user.age())       #105






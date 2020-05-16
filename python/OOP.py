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
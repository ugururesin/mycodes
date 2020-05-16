#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:39:55 2019

@author: UGUR
"""
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
#
weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
#
weekly_sales = str(weekly_sales)  #convert the type back!!
print("This week's total sales: " + weekly_sales)
#

## STRING 'METHODS'
# Methods are like some of the functions!
print("ugur uresin".title())    #title() method: Makes the initials capital
#
print("ugur uresin".islower())  #is.lower() method: Checks whether all are lower-case
#
print("EU published EU laws".count('EU')) #count('X') method: Counts number of X
#
#format() method
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
#
new_str = "The cow jumped over the moon."
new_str.split() #['The', 'cow', 'jumped', 'over', 'the', 'moon.']
#
msg="ABCDE"
msg.index('C')  #A=0, B=1, C=2...
#
msg2="AB CD EF"
msg2.index('C') #A=0, B=1, space=2, C=3...
#
msg3="the end of the story" 
msg3.index('the')   #gives index of first 'the'
msg3.rindex('the')  #gives index of last 'the'


verse = "You are the first and you are the last\n Do not matters whether you are alive"
message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."
length = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')
print(message.format(length, first_idx, last_idx, count))

## SLICE and DICE with LISTS
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
print(days[0])  #gives the first element in days list
print(days[-1]) #gives the last element in days list
#
print(days[0:5])    #ATTENTION the last index(5) is not printed!
print(days[:5])     #ATTENTION the last index(5) is not printed!
print(days[5:7])    #ATTENTION there is no index(7) but used to print index(6)!
print(days[-2:])    #Last two elements in the days!
print(max(days))    #MAX gives the biggest element alphabetically
print(min(days))    #MIN gives the smallest element alphabetically
print(sorted(days)) #Returns a copy of a list in order from smallest to largest, leaving the list unchanged.

## JOIN Method
#Join is a string method that takes a list of strings as an argument, and
#returns a string consisting of the list elements joined by a separator string.
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
#
print("-".join(["Garcia", "O'Kelly"])) #GIVES Garcia-O'Kelly
#


## APPEND Method
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)  #GIVES ['a', 'b', 'c', 'd', 'z']
#


## TUPLES
dimensions = (52, 40, 100)
dimensions = 52, 40, 100    #WO () also it's a tuple!
print(type(dimensions))
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))


## SETS
#A set is MUTABLE, UNORDERED collections of UNIQUE elements! (No duplicate!)
students = ['Ali','Kim','Sue','Tim','Kim','Joe','Tim','Tom']
print(students)
print(set(students))
studentset = {'Alex', 'Alex', 'John', 'Frank'}
print(studentset) #Duplicates are gone!
studentset.add('Joe')
print(studentset) #'Joe' is added


## DICTIONARY
#MUTABLE & UNORDERED data structure that contains mappings of keys to values. 
#KEYS are UNIQUE
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium" which is 2!
#
print("carbon" in elements)         #True
print(elements.get("dilithium"))    #None
#
n = elements.get("dilithium")
print(n is None)        #True
print(n is not None)    #False
#
#
# NESTED DICTIONARY
elements = {'hydrogen':{'number':1,
                        'weight':1.00794,
                        'symbol':'H'},
            'helium':{'number':2,
                        'weight':4.002602,
                        'symbol':'He'}}
print(elements['hydrogen'])
print(elements['hydrogen']['weight'])
print(elements.get('hydrogen','There\'s no such element!'))
print(elements.get('protein','There\'s no such element!'))


##
a = [1, 2, 3]
b = a
c = [1, 2, 3]
#List a and list b are equal and identical
#But a and c point to two different objects, they aren't identical objects!
print(a == b)
print(a is b)
print(a == c)
print(a is c)


### ADDITIONAL APPLICATIONS ###
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, "\n")

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to set to get unique words
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique)

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 


# TRIALS
boqp = {'VIN10001':{'carline':'B460', 'x1':0.2, 'x2':0.4, 'x3':-0.6, 'x4':1},
        'VIN10002':{'carline':'B460', 'x1':0.2, 'x2':0.4, 'x3':-0.6, 'x4':1},
        'VIN10003':{'carline':'B460', 'x1':0.2, 'x2':0.4, 'x3':-0.6, 'x4':1},
        'VIN10004':{'carline':'B460', 'x1':0.2, 'x2':0.4, 'x3':-0.6, 'x4':1},
        'VIN10005':{'carline':'B460', 'x1':0.2, 'x2':0.4, 'x3':-0.6, 'x4':1},
        'VIN10006':{'carline':'B460', 'x1':0.2, 'x2':0.4, 'x3':-0.6, 'x4':1},
        'VIN10007':{'carline':'B460', 'x1':0.2, 'x2':0.4, 'x3':-0.6, 'x4':1},
        'VIN10008':{'carline':'B460', 'x1':0.2, 'x2':0.4, 'x3':-0.6, 'x4':1},
        'VIN10009':{'carline':'B460', 'x1':0.2, 'x2':0.4, 'x3':-0.6, 'x4':1},
        'VIN10010':{'carline':'B460', 'x1':0.2, 'x2':0.4, 'x3':-0.6, 'x4':1}}
qls = {'VIN10001':{'carline':'B460', 'error':4,},
       'VIN10002':{'carline':'B460', 'error':4,},
       'VIN10003':{'carline':'B460', 'error':4,},
       'VIN10004':{'carline':'B460', 'error':4,},
       'VIN10005':{'carline':'B460', 'error':4,},
       'VIN10006':{'carline':'B460', 'error':4,},
       'VIN10007':{'carline':'B460', 'error':4,},
       'VIN10008':{'carline':'B460', 'error':4,},
       'VIN10009':{'carline':'B460', 'error':4,},
       'VIN10010':{'carline':'B460', 'error':4,}}
mymodel = (boqp['VIN10001']['x1'],boqp['VIN10001']['x2'],boqp['VIN10001']['x3'],
           boqp['VIN10001']['x4'],qls['VIN10001']['error'])

55 >= 55 and 55 < 60
state = "CA"
state =="CA"

# FOR LOOP (ITERABLES)
cities =['new york', 'amsterdam', 'istanbul', 'los angeles']
#cities is the iterable
#city is loop iteration variable
for city in cities:
    print(city.title())
#
# Using RANGE
for x in range(10,15,1):
    print(x)
#
cities =['new york', 'amsterdam', 'istanbul', 'los angeles']
for index in range(len(cities)):
    cities[index] = cities[index].title()
    print(cities)
#

## REPLACE METHOD
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    name = name.lower().replace(" ", "_")
    usernames.append(name)
    
print(usernames)


# XML TAG COUNTER
tokens = ['<greeting>', 'Hello World!', '</greeting>']
#
count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
print(count)


## WORD COUNTER
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock',
               'holmes','the','great','gasby','hamlet','adventures','of',
               'huckleberry','fin']
word_counter = {}
word_counter2 = {}
#
## OPTION-1
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)
#
## OPTION-2
for word in book_title:
    word_counter2[word] = word_counter2.get(word, 0) + 1
print(word_counter2)


# ITERATING through DICTIONARIES
team = {"Ali":34,"Tim":41,"Sue":29,"Tom":31,"Kim":33,"Can":30}
team.items()
#
for key in team:
    print(key)
#
for value in team: #ATTENTION: The loop still prints KEYS!!!
    print(value)
#
for key, value in team.items():
    print("Member: {}, Age: {}".format(key, value))
#

## EXAMPLE-1 
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for object, count in basket_items.items():
   if object in fruits:
       result += count
print("There are {} fruits in the basket.".format(result))
#

## EXAMPLE-2
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
#Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
       fruit_count += count
    else:
        not_fruit_count += count
print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))
#




## WHILE LOOP (SUM & POP)
#
# EXAMPLE-1
card_deck = [4,11,8,5,13,2,8,10]
hand = []
#
while sum(hand) <=17:
    hand.append(card_deck.pop())
#pop removes the last element from a list and returns it!
#    
print(hand)
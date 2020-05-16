# =============================================================================
# MAIN PYTHON CODES (CREATED BY UGUR URESIN)
# =============================================================================

# =============================================================================
# SHORTCUTS
# =============================================================================
# CMD+4 Gives a comment frame as given above
# kntrl+C Stops the execution in the console
# The dot (.) after a package name lists the sub-functions in the package
#

# =============================================================================
# IMPORTING THE LIBRARIES
# =============================================================================
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


# =============================================================================
# WORKING DIRECTORY
# =============================================================================
import os
os.getcwd()     #TO GET CURRENT WD
#
path_windows ="C:\\Users\\admin\\Desktop\\mycodes\\data"
path_mac="/Users/UGUR/Desktop/mycodes/data"
os.chdir(path_windows)  #TO SET THE PATH AS WD


# =============================================================================
# DATA TYPES: int, float, bool, string
# =============================================================================
# INTEGERS and FLOATS
x = int(4.7)    #x is now an integer 4
y = float(4)    #y is now a float of 4.0
print(type(x))  #int
print(type(y))  #float
#
# STRINGS
this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)  #Simon's skateboard is in the garage.
#
# LIST-TUPLES-DICTIONARY
mylist = ["red", "blue"]
mytuples = ("green", 256)
mydictionary = {'color':"RGB", 'red':200}
#
mylist[1]
mytuples[1]
print(mydictionary['color'])
#


# =============================================================================
# MATH FUNCTIONS
# =============================================================================
import math
math.sin(math.pi/2)
#
round(1.2) #rounds to 1
round(1.5) #rounds to 2
#
5%2 #gives the modulo(5,2)
#


# =============================================================================
# ## CREATE STRINGS
# =============================================================================
name = "Ugur"
print(type(name))
message1 = "This message is given by quote marks" 
print(message1)
message2 = 'This message is given by "apostrophe" sign' 
print(message2)
message3 = """This message is given by "triple quote" marks""" 
print(message3)
#
## RECORDING STRINGS
name = input("What is your name?: ")
print(name)
age = input("How old are you?: ")
print(age)
city = input("Where do you live?: ")
print(city)
message = "{} is {} years old and lives in {}"
output = message.format(name,age,city)
print(output)


# =============================================================================
# VARIABLE SCOPES: LOCAL VS. GLOBAL
# =============================================================================
# In Python functions create local scopes
# whereas loops and if statements do NOT!
#
# Example
# GLOBAL SCOPE (Both f1 and f2 works)
a = 100
def f1():
    print(a)
def f2():
    print(a)     
f1()
f2()
#
# LOCAL SCOPE (f2 do NOT work!)
def f1():
    b = 100
    print(b)
def f2():
    print(b)     
f1()
f2()
#


# =============================================================================
# STRING METHODS (A METHOD IS A FUNCTION SPECIFIC TO STRINGS)
# =============================================================================
# Note: strings are immutable  
# Format: string.method()
text = "Happy Birthday" 
text.count("p") #counts the given character in the "text"
text.lower()    #turns the "text" into lowercases
text.upper()    #turns the "text" into uppercases
text.capitalize()   #turns the first case of the "text" into uppercase
text.title()        #turns the all first cases of the "text" into uppercases
text.islower()      #checks whether the "text" is lower
text.isalpha()      #checks whether there is a blank in the "text" (NO BLANK=T)
text.isdigit()      #checks whether "text" is composed of digits only
text.index("Birthday")      #gives the index (starts from 0 and gives an index for the blanks also)
text.index("QWERTYUIO")     #gives the index (returns an error if the given character is not available)
text.find("QWERTYUIOP")     #gives the index (returns -1 if the given character is not available)
#
# The Strip Method (To remove characters)
text2 = "000Happy Birthday000"
text2.strip("0")            #removes the zeros from the "text2"
text2.lstrip("0")           #removes the zeros from the LHS "text2"
text2.rstrip("0")           #removes the zeros from the RHS "text2"
#
name = input("What is your name?: ")            #put your name with a blank!
len(name)                                       #gives the length of the "name" (gives +1 for the blank!)
name2 = input("What is your name?: ").strip()   #strip will remove the blanks!
len(name2)
#
# Note: HELP > Python Docs > The Python Standard Library > String Methods !!!
#
# The Slicer Method (To slice strings)
# Format: string[start:end:step]
word = "supercalifragilisticexpialidocious"
word[0:5:1] #gives the indices 0,1,2,3,4 (5 is not included)
word[5::1]  #gives the all indices start with 5
word[:5]    #gives the first 5 indices 0,1,2,3,4
word[:-3]   #gives the all indices except from last 3
word[::-1]  #gives the all indices by reversing them all
word[-3]    #counts indices from the end (gives the last 3rd index)
#
# The Index Method
word.index("cali")
word[word.index("cali") :] #gives the sub-string after the "cali" ("cali" included)
word[: word.index("cali")] #gives the sub-string before the "cali"
word[word.index("cali") : word.index("exp")] #gives the sub-string between cali and exp (exp is not included)
#
# E-mail slicer project
email = input("What is your email address?: ").strip()
# slice out user name
user = email[:email.index("@")]
print(user)
#
# slice domain name
domain = email[email.index("@") + 1: email.index(".com")]
print(domain)
#
# format message
output = "Your username is {} and your domain name is {}".format(user,domain)
print(output)
#


# =============================================================================
# LOGIC (BOOLEAN OPERATORS)
# =============================================================================
#
# Numerical Comparison
2 > 10 #Basic comparison (returns False)
2 == 2 #Basic comparison (returns True)
2 != 2 #Basic comparison (returns False)
2 >= 2 #Basic comparison (returns True)
2 <= 3 #Basic comparison (returns True)
#
# Conditions
not True    #gives False
not False   #gives True
not 3==4    #gives True
#
2==2 or 3==4 #gives True
2==2 and 3==3 #gives True
2==2 and 3==4 #gives False
#
mydata = [1,2,3,4,5]
10 in mydata    #gives false!
del mydata[0]   #deletes the 0th element!
mydata
#
# Note: the "and" & "not" can be used together for NAND
#


# =============================================================================
# CONDITIONAL FLOWS
# =============================================================================
#
# if-else Format 
x1=1000
if x1>2000:
    print("x1 is bigger than 2000")
elif x1>1600:
    print("x1 is bigger than 1600")
elif x1>1200:
    print("x1 is bigger than 1200")
else:
    print("x1 is less than 1200")
#
# Example
num1 = 50
num2 = 100
if num1>num2:
    print("num1 is bigger than num2")
elif num2>num1:
    print("num2 is bigger than num1")
else:    
    print("num1 and num2 are equal")
#
#
# WHILE Format
#
# Example
number = 1
while number <= 3:
    print(number)
    number=number+1
#
#
# forFormat
for number in range(0,101,5): #start from 0 goes to 101 by a step=5
    print(number)
#
for letter in "abcde":
    print(letter)
#
#Note: pass can be used for "do nothing"    
#


# =============================================================================
# BREAK
# =============================================================================
for letters in 'ABCÇD':
    if letters == 'Ç':
        break #STOPS THE LOOP!
    print("Güncel harf: ",letters)
#
temperature=30
while temperature<35:
    print("Ambient temperature:",temperature," in operational limits")
    temperature = temperature+1
    if temperature == 35:
        break
print("Ambient temperature is",temperature,". The operation stops!")
#


# =============================================================================
# CONTINUE
# =============================================================================
for letter in 'Python':
        if letter=='h':
            continue
        print("Current letter: ",letter)


# =============================================================================
# LIST COMPREHENSIONS
# =============================================================================
#
# Example
even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers) 
#
odd_numbers = [x for x in range(1,101) if x % 2 == 1]
print(odd_numbers) 
#
my_words=["the","quick","brown","fox","jumps","over","the","lazy","dog"]
answer = [[w.upper(), w.lower(), len(w)] for w in my_words ] 
print(answer)    
#


# =============================================================================
# PYTHON DATASTRUCTURES
# =============================================================================
#
# "LISTS"
our_list = [2,-3,4,"a","b",True,False] #list can includes different types of data
print (our_list)
our_list[3] #gives the 3rd index (here "a")
our_list[0:3] #gives the following indices: 0,1,2
#
our_list2 = [2,-3,4,["a","b"],True,False]
our_list2[3]    #gives the 3rd index (here "[a,b]")
our_list2[3][1] #gives here "b"
#
# List Operations
A = [1,2,3,4]
#
A + 5       #gives an error!
A + [5]     #TRUE
#
A + "XYZ"          #gives an error!
A + ["XYZ"]        #TRUE (Adds "XYZ" as a single char!)
A + list("XYZ")    #TRUE (Adds each chars seperately!)
A + list(str("1")) #TRUE (Adds "1" as a char!)
#
# Append
A = [1,2,3,4]
A.append(10)    #Adds "10" in the last
print(A)
#
# Insert
A.insert(2,200) #Adds "200" in 2nd index
print(A)
#
#
# "TUPLES" (Similar to lists but immutable!)
#
our_tuple = 1,2,3,"A","B","C"
type(our_tuple)
our_tuple = (1,2,3,"A","B","C")
type(our_tuple)
#
# Multiple assignment can be done by TUPLES
#
(BOB,DOD,TIM) = [22,24,26]
BOB     #gives 22
DOD     #gives 24
TIM     #gives 26
#
# 
# "DICTIONARY" (Includes a key and its value!)
ages = {"AMY":19,"EVA":21,"KIM":23}
ages["EVA"]                            #gives 21
ages["SKY"]=25                         #adds the SKY with the value of 25
ages
del ages["AMY"]                        #removes the AMY with the its value
ages
ages.keys()                            #gives the keys
ages.values()                          #gives the values
ages.items()                           #gives the all keys and the values
#
ages.keys()[0]                         #WRONG! Dictionaries do not have indices!!!
ages_list = list(ages.keys())
ages_list[0]                           #VALID! Lists have indices!!!
#
students = {
        "AMY":["ID001",19,"A"],
        "EVA":["ID001",21,"B"],
        "KIM":["ID001",23,"C"],
        "SKY":["ID001",25,"D"]
        }
students
students["EVA"]         #gives the all values of EVA
students["EVA"][0:2]    #gives the EVA's ID and EVA's age
#
students2 = {
        "AMY":{"ID":"ID001","Age":19,"Grade":"A"},
        "EVA":{"ID":"ID001","Age":21,"Grade":"B"},
        "KIM":{"ID":"ID001","Age":23,"Grade":"C"},
        "SKY":{"ID":"ID001","Age":25,"Grade":"D"}
        }
students2
students2["EVA"]           #gives the dictionary of EVA
students2["EVA"]["ID"]     #gives the EVA's ID
#
students2["EVA"]["ID"],students2["EVA"]["Age"]      #gives the EVA's ID and Age!
#
#


# =============================================================================
# FUNCTIONS
# =============================================================================
# Example
def add(x,y):
    return x+y      #Warning: return makes the output is assign"able"!
                    #So, do not use print instead of return!
result = add(2,3)
result
#    
# Example2
def rev(text):
    return text[::-1]
result2 = rev("hello")
result2
#


# =============================================================================
# KEYWORD ARGUMENTS & DEFAULT PARAMETERS
# =============================================================================
# Parameters: What we use in function definition! (Here: name, age, likes)
# Arguments: What we give to the function (Here: Tim, 23, Apple) 
#
def about(name, age, likes):
    sentence= "{} is {} years old and likes {}".format(name, age, likes)
    return sentence
about("Tim","23","Apple")
#
about("Tim","23","Apple") #positional arguments
about(age="23",name="Tim",likes="Apple") #keyword arguments
#
def about(name, age, likes="Soccer"):
    sentence= "{} is {} years old and likes {}".format(name, age, likes)
    return sentence
about("Tim","23")           #gives the likes=Soccer by default
about("Tim","23","Tennis")  #gives the likes=Tennis as given
#
# WARNING: Parameters with Defaults must be in the last order!!!
#


# =============================================================================
# PACKING AND UNPACKING
# =============================================================================
# Unpacking Example
numbers=[1,2,3,4,5]
print(1,2,3,4,5)    #gives 1 2 3 4 5
print(numbers)      #gives [1,2,3,4,5]
print(*numbers)     #gives 1 2 3 4 5 (* unpacks the list!)
#
print("abc")        #gives abc
print("a","b","c")  #gives a b c
print(*"abc")       #gives a b c
#
# Packing Example
def add(x,y):
    return x+y #is limited with 2 parameters
#
def add(*numbers):
    total = 0
    for number in numbers:
            total = total + number
    return(total)           #we can add numbers as much as we want!
add(1,2,3,4,5,6,7,8,9)      #gives 45!
#
# Packdown Keyword Arguments
def about(name, age, likes):
	sentence = "Meet {}! He is {} years old and he likes {}".format(name,age,likes)
	return sentence
#
dictionary = {"name":"Jack", "age":28, "likes":"Python"}
about(**dictionary)
about(name="Jack", age=28, likes="Python")
#
def foo(**kwargs): #keyword arguments can be anything!
	for key, value in kwargs.items():
		print("{}:{}".format(key, value))

#
foo(Jack="male", Jane="female")
#


# =============================================================================
# STRING OPERATORS
# =============================================================================
# Seperators
print("Boston","Chigago", sep="-")      #Boston-Chigago
print("Boston","Chigago", sep=" x ")    #Boston x Chigago
# New Line
print("Boston\nChigago")                #New line for Chigago
# To prevent \n 
print("C:\new folder")                  #Creates a new line
print("C:\\new folder")                 #No new line (1st Method)
print(r"C:\new folder")                 #No new line (2nd Method)
# Tab Space
print("Boston\tChigago")                #A tab between Boston and Chigago
# Beep Sound
print("\a")                             #Beep sound!
# Char Check
print("a" in "Hello")                   #Gives False
print("l" in "Hello")                   #Gives True
# is and is not operator
a = 10
b = 20
print(a is b)       #Gives False
print(a is not b)   #Gives True
#
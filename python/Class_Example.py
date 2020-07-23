import datetime

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

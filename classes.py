#THIS IS AN EXERCISE IN CREATING CLASSES


#I STARTED OFF BY INITIATING THE CLASS AND ADDING SOME BASIC PROPERTIES
from http.client import PRECONDITION_REQUIRED
from unicodedata import name

class Marine_mammal:
    def __init__(self, name, gestation):
        self.name = name
        self.gestation = gestation 

#a1 = Marine_mammal("Orcas", "15-18 months")
#a2 = Marine_mammal("Humpback whales", "11 months")
#a3 = Marine_mammal("Bottlenose dolphins", "12 months")


#print(a1.name)
#print(a1.gestation)

#this update added functions to the marine mammal class

    def myfunc(self): 
        print("Learn more about " + self.name)

a1 = Marine_mammal("Orcas", "15-18 months")
a1.myfunc()

a2 = Marine_mammal("Humpback whales", "11 months")
a2.myfunc()

a3 = Marine_mammal("Bottlenose dolphins", "12 months")
a3.myfunc()



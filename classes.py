#THIS IS AN EXERCISE IN CREATING CLASSES

from http.client import PRECONDITION_REQUIRED
from unicodedata import name

class Marine_mammal:
    def __init__(self, name, gestation):
        self.name = name
        self.gestation = gestation 

a1 = Marine_mammal("Orcas", "15-18 months")

print(a1.name)
print(a1.gestation)
  

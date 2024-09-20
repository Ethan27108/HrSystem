from Name import *
from Address import *
from BirthInfo import *
class PersonalInfo:
    def __init__(self, first, middle,last, housenumber, street,city,province,country,age, day,month,year):
        self.name = Name(first, middle,last)
        self.address = Address(housenumber, street,city,province,country)
        self.birthInfo=BirthInfo(age, day,month,year)
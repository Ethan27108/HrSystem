from PersonalInfo import *
from ContactInfo import *
from JobInfo import *
class Employee:
    def __init__(self, first, middle,last, housenumber, street,city,province,country, age, day,month,year,cell, workNum, home,work, hourlyRate, hours,bonus,yearsWorked,empNum):
        self.personalInfo = PersonalInfo(first, middle,last, housenumber, street,city,province,country, age, day,month,year)
        self.contactInfo = ContactInfo(cell, workNum, home,work)
        self.jobInfo=JobInfo(hourlyRate, hours,bonus,yearsWorked)
        self.empNum=empNum
    
from Email import *
from PhoneNumber import *
class ContactInfo:
    def __init__(self, cell, workNum, home,work):
        self.phoneNumber = PhoneNumber(cell, workNum)
        self.email = Email(home,work)
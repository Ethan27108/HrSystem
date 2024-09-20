from Billing import *
from YearsWorked import *
class JobInfo:
    def __init__(self, hourlyRate, hours,bonus,yearsWorked):
        self.billing = Billing(hourlyRate, hours,bonus)
        self.yearsWorked=YearsWorked(yearsWorked)
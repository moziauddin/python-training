import pandas as pd
from pandas.tseries.holiday import holiday_calendars
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay


usb = CustomBusinessDay(calendar=USFederalHolidayCalendar())
print('USB: \n', usb)
range = pd.date_range(start='12/24/2018', end='1/4/2019', freq=usb)[::-1]
print(range)

df = pd.read_csv('files/holiday-missing-dates.csv')
print(df)

df.set_index(range, inplace=True)
print(df)

'''
USFederalHolidayCalendar() is a Class designed as an example. 
To build our own country class get the github code for USFederalHolidayCalendar
Build a new class with this skeliton

class USFederalHolidayCalendar(AbstractHolidayCalendar):
    """
    US Federal Government Holiday Calendar based on rules specified by:
    https://www.opm.gov/policy-data-oversight/
       snow-dismissal-procedures/federal-holidays/
    """
    rules = [
        Holiday('New Years Day', month=1, day=1, observance=nearest_workday),
    ]
'''
from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday
class myBirthdayCal(AbstractHolidayCalendar):
    rules = [
        Holiday('My Birthday', month=1, day=11)
    ]

mycal = CustomBusinessDay(calendar=myBirthdayCal())
print('MY CAL', mycal)
date_range = pd.date_range(start='1/1/2019', end='1/15/2019', freq=mycal)
print(date_range)  # 11th should be missing

# Modifying weekday schedules
# Egypt Fri, Sat holiday
weekmask_egy = 'Sun Mon Tue Wed Thu'  # No commas in the day string
egy_week = CustomBusinessDay(weekmask=weekmask_egy)
egy_dates = pd.date_range(start='2/1/2019', periods=15, freq=egy_week)
print(egy_dates)
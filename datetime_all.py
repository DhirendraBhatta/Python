#This will import datetime and timedelta function from datetime library
#This will print today's date
from datetime import datetime,timedelta
today=datetime.now()
print('Today is : '+str(today))
#This will print yesterday's date
one_day=timedelta(days=1)
yesterday=today-one_day
print('Yesterday was: '+str(yesterday))
#This will print tomorrow's date
tomorrow=today+one_day
print('Tomorrow will be : '+str(tomorrow))
print()
#This will print one week before date
one_week=timedelta(weeks=1)
week=today-one_week
print('One week before was: '+str(week))
#This will print one hour before time 
print()
one_hour=timedelta(hours=1)
hour=datetime.now()-one_hour
print('One hour before was : '+str(hour))
#This will print one minute earlier time
one_minute=timedelta(minutes=1)
minute=datetime.now()-one_minute
print('One minute before was: '+str(minute))
#This will print one second earlier time
one_seconds=timedelta(seconds=1)
second=today-one_seconds
print('One Second before was: '+str(second))
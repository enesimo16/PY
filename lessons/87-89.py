import locale
from datetime import datetime,timedelta,time,date

locale.setlocale(locale.LC_TIME,"tr-TR.UTF-8")

result=datetime.now()
print(result)

my_date=datetime.today()

print(my_date.hour)
print(datetime.weekday(my_date)) # günler 0 dan başlar 0=pazartesi
print(datetime.ctime(my_date))
print(my_date.strftime("%d")) # harfler kısaltmayı verir direkt. d gün b ay falan...
result=datetime.timestamp(my_date)
print(result)
print(datetime.fromtimestamp(result))

date1=datetime(2025,1,15)
date2=datetime(2025,1,8)

difference=date1-date2
print(difference)
print(difference.days)

today=datetime.now()
future_date=today+timedelta(days=7)
print(future_date)

past_date=today-timedelta(hours=4,minutes=10)
print(past_date)

print(datetime.isocalendar(today))

myTime=time(14,20,34)
myDate=date(2025,1,19)
combined=datetime.combine(myDate,myTime)
print(combined)

today2=datetime.now()
updated=today.replace(hour=7,minute=19)
print(updated)
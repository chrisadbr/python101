import time
import calendar
from datetime import datetime
from datetime import date

#Displaying the current time and date
localtime = time.asctime(time.localtime(time.time()))
print("Current time: ",  localtime)

#Displaying month calender

#calendar starts with sunday as the first day of the week
cal_month = calendar.TextCalendar(calendar.SUNDAY)
display_cal = cal_month.formatmonth(2019, 12)
print("\n" + display_cal)

#Displaying the current time and date formatted
now = datetime.now()
cur_date = now.strftime("%d-%m-%y  %H:%M:%S")
print("Date and time: ", cur_date)

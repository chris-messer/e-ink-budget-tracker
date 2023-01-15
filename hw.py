import calendar
import datetime

today = datetime.date.today()
last_day_of_month = today.replace(day=calendar.monthrange(today.year, today.month)[1])
monday = today - datetime.timedelta(days=today.weekday())
days_left = last_day_of_month - monday
return int(days_left.days) + 1

print("o")
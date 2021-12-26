import calendar

month, date, year = list(map(int, input().split()))
wd = calendar.weekday(year, month, date)
week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(week[wd])

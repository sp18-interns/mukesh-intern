# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
weekdays = ['MONDAY','TUESDAY','WEDNESDAY','THRUSDAY','FRIDAY','SATURDAY','SUNDAY']
m,d,y=map(int,input().split())
a=calendar.weekday(y,m,d)
print(weekdays[a])

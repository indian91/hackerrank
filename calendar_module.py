#sample input: 08 05 2015
#sample output: WEDNESDAY

import calendar 
x=list(map(int,input().split()))
print(calendar.day_name[calendar.weekday(x[2],x[0],x[1])].upper())

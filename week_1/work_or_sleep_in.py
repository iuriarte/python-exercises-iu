#!/usr/bin/env python3

import calendar

day = -1
print ("day {}".format(day))
valid_days = list(range(0, 7))
print(valid_days)
while day not in valid_days:
    day = int(input('Please enter day (0 - 6) : '))

week = list(calendar.day_name)
week.pop(6)
week.insert(0, 'Sunday')

if (day) in range(1, 5):
    print("Go to work")
    
else:
    print("Sleep in")

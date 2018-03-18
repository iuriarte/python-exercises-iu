#!/usr/bin/env python3
import calendar

day = int(input('Day (0-6)? '))
week = list(calendar.day_name)
week.pop(6)
week.insert(0, 'Sunday')
print(week[day])
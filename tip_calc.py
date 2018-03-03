#!/usr/bin/env python3

total = float(input("Total bill amount? "))
service = input("Level of service? ")
service = service.lower()
if service == 'good':
    tip_percent =.2
    
elif service == 'fair':
    tip_percent = .15
    
elif service == 'bad':
    tip_percent = .1
else:
    exit = 1
    print("Sorry try again!")
    
if exit != 1:    
    tip = float(total*tip_percent)
    print("Tip amount {}".format(tip))

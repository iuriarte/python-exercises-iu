#!/usr/bin/env python3

bill = float(input("Total bill amount? "))
service = input("Level of service? ")
split = float(input("Split how many ways? "))

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
    tip = float(bill*tip_percent)
    total = float(bill+tip)
    perperson = float(total/split)
    print("Tip amount: {}".format(tip))
    print("Total amount: {}".format(total))
    print("Amount per person: {}".format(perperson))
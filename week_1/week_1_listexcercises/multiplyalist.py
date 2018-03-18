#!/usr/bin/env python3

listofnumbers = [1,2,3,5,7,10,11,13,17,19]
factor = 2
endofrange = len(listofnumbers)
multipliedlist = []

for number in range(0, endofrange):
    multiply = factor * listofnumbers[number]
    multipliedlist.append(multiply)

print("List of Numbers: ", listofnumbers)
print("Factor: ", factor)
print ("Multiplied List = ", multipliedlist)
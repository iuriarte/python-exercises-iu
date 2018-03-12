#!/usr/bin/env python3

listofnumbers = [1,3,5,7,11,13,17,19]
endofrange = len(listofnumbers)
sumofnumbers = 0

for number in range(0, endofrange):
  numberinturn = listofnumbers[number]
  sumofnumbers += listofnumbers[number]
  
print("List of Numbers = ", listofnumbers)  
print ("Sum of Numbers = ", sumofnumbers)
  
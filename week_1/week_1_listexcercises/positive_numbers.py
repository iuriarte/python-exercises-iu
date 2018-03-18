#!/usr/bin/env python3

listofnumbers = [3,1,51,7,-18,19,11,13,17,-1,-2]
endofrange = len(listofnumbers)
listofnumbers.sort()
positivenumbers = []
largets_number = listofnumbers[(endofrange-1)]

for number in range(0, endofrange):
    numberinturn = listofnumbers[number]
    if listofnumbers[number] > 0:
        positivenumbers.append(numberinturn)
        
print("Array of positivenumbers : ", positivenumbers)
  
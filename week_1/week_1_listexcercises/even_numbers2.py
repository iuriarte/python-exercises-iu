print ('what the heck!!!!!')
listofnumbers = [1,2,3,5,7,10,11,13,17,19]
even_numbers = []
endofrange = len(listofnumbers)

for number in range(0, endofrange):
  print(number)
  numberinturn = listofnumbers[number]
  print (numberinturn)
  sumofnumbers =+ listofnumbers[number]
  if listofnumbers[number]%2 == 0:
    even_numbers.append(numberinturn)
  
print(even_numbers)
  
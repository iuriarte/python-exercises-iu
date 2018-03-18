#!/usr/bin/env python3

intab = "AEGIOST"
outab = "4361057"
astring = "this is a really silly excersice"
cap_string = astring.upper()
transtab = cap_string.maketrans(intab, outab)

print(astring)
print (cap_string.translate(transtab))

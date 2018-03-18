#!/usr/bin/env python3

intab = "AEGIOST"
outab = "4361057"
astring = "defend the east wall of the castle"
cap_string = astring.upper()
transtab = cap_string.maketrans('rot_13')
encrypted_char = []
cypher_key = 2

print(astring)
print (cap_string.translate(transtab))



for char in astring:
    print("char type: ", type(char))
    print("char: ", char)
    char_index = (ord(char))
    print("char_index: ", type(char_index))
    print("char_index: ", char_index)
    #encrypted_char = (chr((char_index+cypher_key)%26))
    #encrypted_char.decode('rot_13')
    print("encrypted_char", encrypted_char)
    print("encrypted_char type: ", type(encrypted_char))
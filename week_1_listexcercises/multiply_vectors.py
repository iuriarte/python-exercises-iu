#!/usr/bin/env python3

vector1 = [2,4,5]
vector2 = [2,3,6]

endofrange = len(vector1)
multiplied_vector = []

for number in range(0, endofrange):
    multiply = vector1[number] * vector2[number]
    multiplied_vector.append(multiply)

print("Vector 1: ", vector1)
print("Vector 2: ", vector2)
print ("Multiplied vectors = ", multiplied_vector)
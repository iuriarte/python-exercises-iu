#!/usr/bin/env python3

matrix1 = [ [1,3], [2,4]]
matrix2 = [ [5,2], [1,0]]
added_matrix =[]

print("Matrix1 : ", matrix1)
print("Matrix2 : ", matrix2)

for i in range (0,2):
    #print("i= ", i)
    for j in range (0,2):
        addition = matrix1[i][j]+matrix2[i][j]
        added_matrix.append(addition)
        
print("Added_matrix = ", added_matrix)
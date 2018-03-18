#!/usr/bin/env python3


matrix1 = [ [1,3,0,5], [2,4,1,3]]
matrix2 = [ [5,2,1,5], [1,0,1,-3]]

added_matrix =[]
addition = []

m1_lenght=len(matrix1)
m2_lenght=len(matrix2)
m1_sub_length = len(matrix1[0])
m2_sub_lenght = len(matrix2[0])

print("Matrix1 : ", matrix1)
print("Matrix2 : ", matrix2)
print("Matrix1 len = ", m1_lenght)
print("Matrix2 len = ", m2_lenght)
print("Matrix1 sub-len = ", m1_sub_length)
print("Matrix2 sub-len = ", m2_sub_lenght)

if (m1_lenght == m2_lenght and m1_sub_length == m2_sub_lenght):
    for i in range (0,m1_lenght):
        #print("i= ", i)
        row = []
        for j in range (0,m1_sub_length):
            addition = matrix1[i][j]+matrix2[i][j]
            row.append(addition)
            print("row = ", row)
        added_matrix.append(row)
    
    print("Added_matrix = ", added_matrix)
else:
    print("Matrices are not of the same lenght")
#!/usr/bin/env python3


list1 = [1,3,0,5,9,0,5,3,0,0,'lost', 9, 'lost raider', 1, 'lost']

seen = set()

unique =[]
for i in list1:
    if i not in seen:
        #print("i = ", i)
        unique.append(i)
        #print("unique(i) = ", unique)
        seen.add(i)
        #print("seen (i) = ", seen)

print("List1 = ", list1)
print("seen = ", seen)
print("unique = ", unique)

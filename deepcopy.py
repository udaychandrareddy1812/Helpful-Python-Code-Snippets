'''
In Python, if there are two lists, say lis1 and lis2, and we assign lis2 = lis1, 
both variables will reference the same list in memory. 
As a result, any changes made to lis2 will also affect lis1. 
To avoid this, we can use a deep copy to create an independent copy of the original list.

'''

lis1 = [1,2,3,4,5,6,7,8]
print(lis1)
lis2=lis1
print(lis2)
lis2.append(2)
print(lis1)
print(lis2)

import copy

lis1 = [1,2,3,4,5,6,7,8]
print(lis1)
lis2 = copy.deepcopy(lis1)
print(lis2)
lis2.append(2)
print(lis1)
print(lis2)

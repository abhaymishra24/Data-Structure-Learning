
# Problem number 1 - Array method 
# Data Structure problem in Array 

from array import * 

a1=array ('i', [23,24,12])

# for loop 

for i in a1:
    print(i)

for i in range (3):
    print(a1[i], end=" ")

# while loop

i=0

while i<len(a1):
    print(a1[i])
    i+=1
    
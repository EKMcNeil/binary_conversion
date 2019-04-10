#!/usr/bin/python3

import sys

#print ("Number of arguments:", len(sys.argv), "arguments.")
#print ("Argument List:", str(sys.argv))

if len(sys.argv) != 2:
    print("Incorrect Number of Arguments")
    sys.exit(1) 

binary = sys.argv[1]
#print("Binary", list(binary))

#system check for binary digits only
for digit in list(binary):
    if digit != "0" and digit != "1":
        print("Invalid Binary Number")
        sys.exit(1)

x=0
nybbles=[]
first=0
result = 0

for digit in list(binary):
    if x % 4 == 0:
        if x != 0:
            nybbles.append(binary[first:x])  
        first = x
    x += 1         

#division into nybbles
if x <= len(binary):
    nybbles.append(binary[first:])

print(nybbles)

x=0
result=0

#binary to decimal conversion
for digit in reversed(list(binary)):
    if digit == "1":
      result += int(digit)*2**x
    x +=1

print(result)

a = 9
x = 0
m = 16
list = ("a", "b", "c", "d", "e", "f", "g", "h")

#simply getting the program written
for x in list(result):
    b = result % 16**x
    if b == a:
        print(next(list))
    x += 1
    a += 1
    else:
        print(b)
    break

sys.exit[1] 

#tuple for values to use 'next' to iterate over. May not be correct
hextuple = ("a", "b", "c", "d", "e", "f", "g", "h")
 
#attempt to convert hex to decimal - syntax issues
for x in list(result):
    b = result % 16**int(x)
    if b >= a:
        print(hextuple[1]) 
    a += 1
    x += 1
    next(hextuple)#attempt to use the next letter in the tuple
    else:
        b < a:
        print(b)
    break
 
print(b)

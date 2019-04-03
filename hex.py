#!/usr/bin/python3

import sys

#print ("Number of arguments:", len(sys.argv), "arguments.")
#print ("Argument List:", str(sys.argv))

if len(sys.argv) != 2:
    print("Incorrect Number of Arguments")
    sys.exit(1) 

binary = sys.argv[1]
#print("Binary", list(binary))

for digit in list(binary):
    if digit != "0" and digit != "1":
        print("Invalid Binary Number")
        sys.exit(1)

x=0
result=0

for digit in list(binary):
    if digit == "1": 
        result +=int(digit)*2**x
        x+=1
    
print(result)





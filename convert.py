#!/usr/bin/python3

import sys

#converts binary to decimal
def binary_to_decimal(binary): 
    x = 0
    result = 0
    for digit in list(binary):
        if digit == "1": 
            result += int(digit) * 2**x 
            #print(x, result)
            x += 1
        if digit == "0":
            x +=1
            #print(x, result)
        return result

#print ("Number of arguments:", len(sys.argv), "arguments.")
#print ("Argument List:", str(sys.argv))

if len(sys.argv) != 2:
    print("Incorrect Number of Arguments")
    sys.exit(1) 

binary = sys.argv[1]
#print("Binary", list(binary))

#system checks for correct values input
for digit in list(binary):
    if digit != "0" and digit != "1":
        print("Invalid Binary Number")
        sys.exit(1)

result = binary_to_decimal
         
print(result)

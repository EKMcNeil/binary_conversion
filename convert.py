#!/usr/bin/env python3

import sys

#converts binary to decimal
class BinaryToDecimal:
    def binary_to_decimal(self, binary):
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
        #print(self)    
        return result

def main():
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

    btod = BinaryToDecimal()
    #print(btod)
    result = btod.binary_to_decimal(binary)

    print(result)

#print ("Number of arguments:", len(sys.argv), "arguments.")
#print ("Argument List:", str(sys.argv))

if __name__ == '__main__':
    main()

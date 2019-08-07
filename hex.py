#!/usr/bin/env python3

#converts binary to hexadecimal 
#maybelittleendianstyle

import sys

#print("Binary", list(binary))

class InvalidBinary(Exception):
    pass

class BinaryToHex:
    def binary_to_hex(self, binary):
        #system check for binary digits only
        for digit in list(binary):
            if digit != "0" and digit != "1":
                raise InvalidBinary(binary)
                
        #print(list(binary))
        x = 0
        nybbles = []
        first = 0
        result = 0

        for digit in (list(binary)):
            x += 1         
            if x % 4 == 0:              
                if x != 1:
                    nybbles.append(binary[first:x])  
                first = x
                #print(nybbles)

        #division into nybbles
        if x <= len(binary):
            t = binary[first:]
            r = len(binary) % 4
            if r > 0:
                for i in range(4-r):
                    t += "0"        
                nybbles.append(t)
         
        #print(nybbles)

        hexnum = ""

        for nybble in nybbles:
            if nybble == "0000":
                hexnum += "0"
            elif nybble == "0001":
                hexnum += "8"
            elif nybble == "0010":
                hexnum += "4"
            elif nybble == "0011":
                hexnum += "c"
            elif nybble == "0100":
                hexnum += "2"
            elif nybble == "0101":
                hexnum += "a"
            elif nybble == "0110":
                hexnum += "6"
            elif nybble == "0111":
                hexnum += "e"
            elif nybble == "1000":
                hexnum += "1"
            elif nybble == "1001":
                hexnum += "9"
            elif nybble == "1010":
                hexnum += "5"
            elif nybble == "1011":
                hexnum += "d"
            elif nybble == "1100":
                hexnum += "3"
            elif nybble == "1101":
                hexnum += "b"
            elif nybble == "1110":
                hexnum += "7"
            elif nybble == "1111":
                hexnum += "f"

        return hexnum

def main():

        #print ("Number of arguments:", len(sys.argv), "arguments.")
        #print ("Argument List:", str(sys.argv))

        if len(sys.argv) != 2:
            print("Incorrect Number of Arguments")
            sys.exit(1) 

        binary = sys.argv[1]

        bintohex = BinaryToHex() 
        try:
            result = bintohex.binary_to_hex(binary)
            print(result)
        except InvalidBinary as e:
            print("Invalid binary number " + str(e))
 
if __name__ == '__main__':
    main()

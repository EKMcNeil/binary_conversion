#!/usr/bin/env python3

import sys

class InvalidError(Exception):
    pass 
                                               
#convert decimal to binary
#max defines the maximum number of bits
class DecimalToBinary:
    def decimal_to_binary(self, decimal, max = 16):
        for digit in list(decimal):
            #print("Got digit:" + digit)
            if not digit in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                raise ValueError(decimal + " is not a valid decimal")

        if int(decimal) > (2**max) - 1:
            print(decimal + " is bigger than the maximum size " + str(2**max-1))
            sys.exit(1)
     
        r = int(decimal)
        if r == 0:
            return "0"

        m = 0
        for n in range(0, max + 1):
            if 2**n > int(decimal):
                m = n
                break
     
        #print("m = " + str(m))

        binary = ""

        for i in reversed(range(0, m)):
            #print("i = " + str(i))
            t = r - 2**i
            #print("t = " + str(t))
        #setting temporary variable   
            if t >= 0:
                r = t 
                binary += "1"
            else:
                binary += "0"
                
        result = binary[::-1]      
        
        return result

def main():
        #print ("Number of Arguments:", len(sys.argv), "arguments.")
        #print ("Argument List:", str(sys.argv))

        if len(sys.argv) != 2:
            print("Incorrect Number of Arguments")
            sys.exit(1)

        decimal = sys.argv[1]
        #print("Decimal", list(decimal))

        try:
            result = decimal_to_binary(decimal)
        except ValueError as e:
            print(e)
            sys.exit(1)

        print(result)

if __name__ == '__main__':
    main()

#!/bin/env python3

import sys
                                                
#MAXimum number of bits converted 
MAX = 16 

def decimal_to_binary(decimal):
    for digit in list(decimal):
        #print("Got digit:" + digit)
        if not digit in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            #print(decimal + " is not a valid decimal")
            sys.exit(1)

    if int(decimal) > 2**MAX-1:
        print(decimal + " is bigger than the maximum size " + str(2**MAX-1))
        sys.exit(1)

    m = 0
    for n in range(0, MAX):
        if 2**n > int(decimal):
            m = n-1
            break
 
    #print("m = " + str(m))

    r = int(decimal)
    binary = ""

    for i in reversed(range(0, m+1)):
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

#print ("Number of Arguments:", len(sys.argv), "arguments.")
#print ("Argument List:", str(sys.argv))

if len(sys.argv) != 2:
    print("Incorrect Number of Arguments")
    sys.exit(1)

decimal = sys.argv[1]
#print("Decimal", list(decimal))

result = decimal_to_binary(decimal)

print(result)


#!/usr/bin/python3

import sys
#print ("Number of Arguments:", len(sys.argv), "arguments.")
#print ("Argument List:", str(sys.argv))

if len(sys.argv) != 2:
    print("Incorrect Number of Arguments")
    sys.exit(1)

import logging
logging.basicConfig(filename="decimal.py", level=logging.debug)
logging.debug("This should go into logs") #print("Debugging logs")

decimal = sys.argv[1]
#print("Decimal", list(decimal))

def test_range(decimal):
    if decimal in range(0, 10,000):
       print(" %s is a valid decimal")
    else:
       print("%s is not a valid decimal")

max = 16

for n in range(0, max-1):
    if 2**n>decimal:
       m = n-1 
       break

if 2**n>decimal:
    print("1")
    else:
       print("0")

for n in range(0, max-1):
    if 2**n>m:
       o = n-1
       break

  

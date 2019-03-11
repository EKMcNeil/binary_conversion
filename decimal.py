#!/usr/bin/python3

import sys
#print ("Number of Arguments:", len(sys.argv), "arguments.")
#print ("Argument List:", str(sys.argv))

if len(sys.argv) != 2:
    print("Incorrect Number of Arguments")
    sys.exit(1)

decimal = sys.argv[1]
#print("Decimal", list(decimal))

def test_range(decimal):
    if decimal in range(0, 10,000):
       print(" %s is a valid decimal")
    else:
       print("%s is not a valid decimal")

max = 16

for n in range(0, max-1):
    if 2 ** n > decimal:
       m = n-1 
       break

if 2 ** n > decimal:
    print("1")
else:
    print("0")

#alternately use divmod(decimal variable1/2 **n variable 2) to return the answer of division and the remainder... doesn't make it as easy toput the remainder in though
if 2 ** m > decimal%2 ** n:
    o = m-1
    if true:
      print("1")       
    else:
      print("0")
    break
  

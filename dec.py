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
    if not int(decimal):
       print("%s is not a valid decimal")

max = 16

for n in range(0, max-1):
    if int(pow(2, n)) > int(decimal):
       print("1")
       m = n-1
    if not int(pow(2, n)) < int(decimal):
       print("0") 
       break

second_digit = (int(decimal)%int(pow(2, n))
#second digit from the left
   
if  int(pow(2, m)) > int(second_digit):
    print("1")
else:
    print("0")
    




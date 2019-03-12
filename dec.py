#!/usr/bin/python3

import sys
#print ("Number of Arguments:", len(sys.argv), "arguments.")
#print ("Argument List:", str(sys.argv))

if len(sys.argv) != 2:
    print("Incorrect Number of Arguments")
    sys.exit(1)

decimal = sys.argv[1]
#print("Decimal", list(decimal))

for digit in list(decimal):
    print("Got digit:" + decimal)
    if digit in range(0, 9):
        print(" %s is a valid decimal")
        sys.exit(1)

sys.exit(0)

max = 16

for n in range(0, max-1):
    if int(pow(2, n)) > int(decimal):
       print("1")
       m = n-1
    elif int(pow(2, n)) < int(decimal):
       print("0") 
       break
       exit

second_digit = int(decimal)%int(pow(2, n))
#second digit from the left
   
for h in range(0, max-1):
    if int(pow(2, m)) > int(second_digit):
       print("1")
    elif int(pow(2, m)) < int(second_digit):
       print("0")
    break









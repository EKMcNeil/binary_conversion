#!/usr/bin/python3

import sys

#maximum number of bits converted 
max = 16 

#print ("Number of Arguments:", len(sys.argv), "arguments.")
#print ("Argument List:", str(sys.argv))

if len(sys.argv) != 2:
    print("Incorrect Number of Arguments")
    sys.exit(1)

decimal = sys.argv[1]
#print("Decimal", list(decimal))

for digit in list(decimal):
    print("Got digit:" + digit)
    if not digit in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print(decimal + " is not a valid decimal")
        sys.exit(1)

#sys.exit(0)

if int(decimal) > 2**max-1:
    print(decimal + " is bigger than the maximum size " + str(2**max-1))
   #sys.exit(1)

max = 16
remainder = 0 

for n in range(0, max-1):
    if int(pow(2, n)) > int(decimal):
       print("1")
       m = n-1
       #what function does this m actually have???
    elif int(pow(2, n)) < int(decimal):
       print("0")
    remainder = (int(decimal)%int(pow(2 ,n)))
    #Sets remainder variable for next loop 
    break
    exit

print(remainder)
sys.exit(1)

#hashed out until I remember why I set this variable! second_digit = int(decimal)%int(pow(2, n))
#second digit from the left
   
for n in range(0, max-1):
    if int(pow(2, n)) > int(remainder):
       print("1")
    elif int(pow(2, n)) < int(remainder):
       print("0")
    remainder = (int(remainder)%int(pow(2, n)))
    break










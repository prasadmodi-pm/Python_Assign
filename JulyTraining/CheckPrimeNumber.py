__author__ = 'prasadmodi'
import math
num = int(input("Please enter a number to check prime or not: "))

i = 2

while(num > i):
    if(num % i == 0 and i is not num):
        print("It is Not a Prime")
        break
    i = i + 1
else:
    print("It is Prime Number")

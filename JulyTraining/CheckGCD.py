__author__ = 'prasadmodi'
def GCD(a,b):
    if(a > b):   # check which element is smaller
        min = b

    else:
        min = a
    for i in range(1,min+1):
        if((a % i == 0) and (b % i==0)):
            gcd = i

    return gcd
num = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))

print("GCD of two numbers: ",GCD(num,num2))


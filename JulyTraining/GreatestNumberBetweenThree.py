__author__ = 'prasadmodi'
num = str(input("Please enter number 1: "))
num2 = str(input("Please enter number 2: "))
num3 = str(input("Please enter number 3: "))

if(num > num2 and num > num3):
    print("This is Greatest Number",num)

elif(num2 > num and num2 > num3):
    print("This is Greatest Number",num2)
else:
    print("This is Greatest Number",num3)
__author__ = 'prasadmodi'
list = []

num = int(input("Number of elements in list: "))   # Total Number of elements list accepts

for i in range(num):
    nums = input("enter elements to be added to list: ")  # Elements taken from user
    list.append(nums)
    print(list)

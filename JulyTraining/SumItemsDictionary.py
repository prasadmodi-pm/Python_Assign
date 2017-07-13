__author__ = 'prasadmodi'
dict = {'a': [1,2,3], 'b': [2,3,4]}

dict2 = {}

for k,v in dict.items():
    dict2[k] = sum(v)

print(dict2)







import re
import sys

array = ['9D6PF7', 'HS7XHY', 'W5Q8R', 'Y7VSJ', 'N9MPM','6CPZB']

def make_pw_token(arr):
    
    rev = ''
    for token in arr:
        rev = rev+token[::-1]+'-'
    return rev[:-1]


param_1 = input("Code>>>")

rev = param_1+'-'+make_pw_token(array)
rev2 = make_pw_token(rev)

#print(param_1)
print(rev)
print(rev2==param_1)



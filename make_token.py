import re
import sys

array = ['3A','02401F','9D6PF7', 'HS7XHY', 'W5Q8R', 'Y7VSJ', 'N9MPM','6CPZB']
array2 = ['3A','15022D','LYBM58','HWRAX5','MYC78','NYQBH','NFX43','5HQA8']

def make_pw_token(arr):
    
    rev = ''
    for token in arr:
        rev = rev+token[::-1]+'-'
    return rev[:-1]




rev =  make_pw_token(array)
rev2 = make_pw_token(array2)

#print(param_1)
print(rev)
print(rev2)



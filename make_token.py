import re
import sys


def make_pw_token(str):
    result = re.split('#', str)
    rev = ''
    for token in result:
        rev = rev+token[::-1]+'-'
    return rev[:-1]


# main
#param_1= sys.argv[1]

param_1 = input("Code>>>")

param_1= param_1+'#9D6PF7#HS7XHY#W5Q8R#Y7VSJ#N9MPM#6CPZB'

rev = make_pw_token(param_1)
rev2 = make_pw_token(rev)


print(param_1)
print(rev)
print(rev2==param_1)



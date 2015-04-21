
import string

s1 = "waterbottle"
s2 = "erbottlewat"
s3 = "fa"
s4 = "af"
s5 = "nugget"
s6 = "getgun"

def isSubstring(one, two):
    return string.find(one, two)

def checkrotate(input1, input2):
    if isSubstring(input1+input1, input2) == -1:
        return False
    else:
        return True

print checkrotate(s1,s2)
print checkrotate(s3,s4)
print checkrotate(s5,s6)
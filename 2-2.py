from LinkedList import *

def init():
    input = NodeList()
    for i in "FOLLOW UP":
        input.add(Node(i))
    return input

input1 = init()
input2 = init()
input3 = init()
input4 = init()

def element(lst,n):
    return lst.sublist(n)

print element(input1,1)
print element(input1,2)
print element(input1,3)
print element(input2,4)
print element(input2,5)
print element(input2,6)
print element(input2,7)
print element(input2,8)
print element(input3,9)
print element(input3,10)
print element(input3,11)
print element(input3,12)

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

def remove(input,node):
    input.remove(node)

remove(input1,input1.sublist(2))

print input1
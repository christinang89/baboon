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


def partition(input, val):
    small = NodeList()
    big = NodeList()
    eq = NodeList()
    temp = input.start
    while temp!= None:
        storednext = temp.next
        if temp.value < val:
            small.add(temp)
        elif temp.value == val:
            eq.add(temp)
        else:
            big.add(temp)
        temp = storednext
    small.combine(eq)
    small.combine(big)
    return small

print partition(input1, "O")
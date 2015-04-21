from LinkedList import *

def init():
    input = NodeList()
    for i in "FOLLOLOWWF LULLUUPMP":
        input.add(Node(i))
    return input

input = init()
input2 = init()
input3 = init()
input4 = init()

def cheat(input):
    temp = input.start
    arr = [temp.value]
    while temp.next is not None:
        if temp.next.value not in arr:
            arr.append(temp.next.value)
            temp = temp.next
        else:
            temp.next = temp.next.next
    return input

print cheat(input)

def second(input):
    temp = input.start
    while temp.next is not None:
        temp2 = temp
        while temp2.next is not None:
            if temp2.next.value == temp.value:
                temp2.next = temp2.next.next
            else:
                temp2 = temp2.next        
        temp = temp.next
    return input

print second(input2)

def third(input):
    temp = input.start
    while temp.next is not None:
        input.removefromnode(temp.next, temp.value)
        #print input
        temp = temp.next

    return input

print third(input3)
from LinkedList import *
import string

def init():
    input = NodeList()
    for i in [7,1,6,1]:
        input.add(Node(i))
    return input

def init2():
    input = NodeList()
    for i in [5,9,2]:
        input.add(Node(i))
    return input

def init3():
    input = NodeList()
    for i in [6,1,7,1]:
        input.add(Node(i))
    return input

def init4():
    input = NodeList()
    for i in [9,5,1,9]:
        input.add(Node(i))
    return input

input1 = init()
input2 = init2()
input3 = init()
input4 = init2()
input5 = init3()
input6 = init4()

def convertInt(lst):
    temp = lst.start
    sum = 0
    multiple = 1
    while temp is not None:
        sum += temp.value * multiple
        multiple *= 10
        temp = temp.next
    return sum

def add(one,two):
    total = convertInt(one) + convertInt(two)
    result = NodeList()
    for i in str(total)[::-1]:
        result.add(Node(int(i)))
    return result

print add(input1, input2)

result = NodeList()

def add1(one,two,carry):
    temp1 = one
    temp2 = two
    if temp1 is None and temp2 is None and carry == 0:
        return result
    elif temp1 is None and temp2 is None:
        result.add(Node(carry))
    else:
        sum = 0
        if temp1 is None:
            sum = temp2.value + carry
        elif temp2 is None:
            sum = temp1.value + carry
        else:
            sum = temp1.value + temp2.value + carry

        if sum < 10:
            result.add(Node(sum))
            carry = 0
        else:
            result.add(Node(sum%10))
            carry = int(sum/10)

        if temp1 is None:
            add1(None, temp2.next,carry)
        elif temp2 is None:
            add1(temp1.next, None, carry)
        else:
            add1(temp1.next, temp2.next, carry)

add1(input3.start, input4.start,0)
print result

final = NodeList()
print input5
print input6
def tempadd(one,two,extra):
    sum = one.value + two.value + extra
    if sum < 10:
        final.insert(Node(sum))
        extra = 0
    else:
        final.insert(Node(sum%10))
        extra = int(sum/10)
    return extra

def forward(one,two):
    temp1 = one
    temp2 = two
    if temp1.next is None and temp2.next is None:
        return tempadd(temp1, temp2, 0)
    else:
        return tempadd(temp1, temp2, forward(temp1.next, temp2.next))

def super(one, two):
    if one.length() > two.length():
        for i in xrange(one.length() - two.length()):
            two.insert(Node(0))
    elif two.length() > one.length():
        for i in xrange(two.length() - one.length()):
            one.insert(Node(0))

    n = forward(one.start,two.start)
    if n > 0:
        final.insert(Node(n))

super(input5, input6)
print final


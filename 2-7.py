#check if linkedlist is palindrome

from LinkedList import *

def init():
    input = DoubleNodeList()
    for i in "HELLEH":
        input.add(Node2(i))
    return input

def init2():
    input = NodeList()
    for i in "1234321":
        input.add(Node(i))
    return input

input1 = init()
input2 = init2()

def palindrome(input):
    head = input.head()
    tail = input.tail()
    for i in xrange(int(input.length()/ 2)):
        while head != tail:
            if head.value != tail.value:
                return False
            else:
                head = head.next
                tail = tail.prev
    return True

print palindrome(input1)

def printreverse(input):
    if input.next is None:
        print input.value
    else:
        printreverse(input.next)
        print input.value

#print printreverse(input2.start)

def comparehelper(first,second):
    if second.value == first.value:
        return True
    else:
        return False

def compare(first,second):
    if second is None:
        return first
    n = compare(first,second.next)
    if n == None:
        return None
    if comparehelper(second,n):
        print n.value + " matches with " + second.value
        return n.next
    else:
        print n.value + " does not match with " + second.value
        return None

def palindromeSingle(input):
    first = input.start
    second = input.start
    while second is not None and second.next is not None :
        first = first.next
        second = second.next.next
    second = first
    first = input.start

    if compare(first, second):
        print "YES"
    else:
        print "NO"

print palindromeSingle(input2)

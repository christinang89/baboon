class Node:
    #linkedlist
    def __init__(self,val):
        self.next = None
        self.value = val
    def __repr__(self):
        return self.value

class NodeList:
    def __init__(self):
        self.start = None
    def head(self):
        return self.start
    def tail(self):
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        return temp
    def add(self, node):
        node.next = None
        if self.start is None:
            self.start = node
        else:
            temp = self.start
            while (temp.next is not None):
                temp = temp.next
            temp.next = node

    def insert(self,node):
        node.next = None
        if self.start is None:
            self.start = node
        else:
            node.next = self.start
            self.start = node

    def combine(self,lst):
        self.tail().next = lst.head()

    def __repr__(self):
        temp = self.start
        accumulator = ""
        while (temp is not None):
            accumulator += str(temp.__repr__())
            temp = temp.next
        return accumulator
    def remove(self, node):
        temp = self.start
        if temp is None:
            return temp
        elif temp == node:
            self.start = self.start.next
            return self
        else:
            while (temp.next != None):
                if temp.next == node:
                    temp.next = temp.next.next
                    return self
                temp = temp.next
            return self

    def length(self):
        temp = self.start
        if temp is None:
            return 0
        elif temp.next is None:
            return 1
        else:
            count = 1
            while temp.next is not None:
                count += 1
                temp = temp.next
            return count

    def removefromnode(self,node,val):
        temp = self.start
        if temp != node:
            while temp.next != None and temp.next != node:
                temp = temp.next
        
        while temp.next is not None:
            if temp.next.value == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

    def sublist(self,n):
        if n > self.length():
            return "Error, index out of bounds"
        n = self.length() - n + 1
        temp = self.start
        if n == 1:
            return temp
        else:
            count = 1
            while count < n:
                temp = temp.next
                count += 1
            return temp

class Node2:
    #Doubly linkedlist
    def __init__(self,val):
        self.next = None
        self.value = val
        self.prev = None
    def __repr__(self):
        return self.value

class DoubleNodeList:
    def __init__(self):
        self.start = None
    def head(self):
        return self.start
    def tail(self):
        temp = self.start
        if temp is None:
            return None
        while temp.next is not None:
            temp = temp.next
        return temp
    def add(self, node):
        node.next = None
        node.prev = self.tail()
        if self.start is None:
            self.start = node
        else:
            self.tail().next = node
    def length(self):
        temp = self.start
        if temp is None:
            return 0
        elif temp.next is None:
            return 1
        else:
            count = 1
            while temp.next is not None:
                count += 1
                temp = temp.next
            return count
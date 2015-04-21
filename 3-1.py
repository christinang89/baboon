

class Stack():
    def __init__(self):
        self.size = 18
        self.first = 0
        self.second = self.size / 3
        self.third = 2 * self.size / 3
        self.store = []
        for i in xrange(self.size):
            self.store.append(None)
    def push(self,val,stacknum):
        if stacknum == 1:
            if self.first == (self.size / 3):
                print "cant push"
            else:
                self.store[self.first] = val
                self.first += 1
        elif stacknum == 2:
            if self.second == (2 * self.size / 3):
                print "cant push"
            else:
                self.store[self.second] = val
                self.second += 1
        elif stacknum == 3:
            if self.third == self.size:
                print "cant push"
            else:
                self.store[self.third] = val
                self.third += 1
    def pop(self, stacknum):
        if stacknum == 1:
            if self.first is None or self.first == 0:
                print "cant pop"
            else:
                self.first -= 1
                temp = self.store[self.first]
                self.store[self.first] = None
                return temp
        elif stacknum == 2:
            if self.second is None or self.second == (self.size / 3):
                print "cant pop"
            else:
                self.second -= 1
                temp = self.store[self.second]
                self.store[self.second] = None
                return temp
        elif stacknum == 3:
            if self.third is None or self.third == (2 * self.size / 3):
                print "cant pop"
            else:
                self.third -= 1
                temp = self.store[self.third]
                self.store[self.third] = None
                return temp
    def __repr__(self):
        return self.store

s = Stack()
s.push(2,1)
s.push(3,1)
s.push(4,1)
s.push(5,1)
s.push(6,1)
s.push(7,1)
s.push(8,1)
print s.__repr__()

s.push(2,2)
s.push(5,2)
s.push(6,2)
s.push(8,2)
s.push(2,2)
s.push(4,2)
s.push(6,2)
s.push(4,2)
s.push(7,2)
print s.__repr__()
s.push(2,3)
print s.__repr__()

print s.pop(1)
print s.pop(1)
print s.pop(1)
print s.pop(1)
print s.pop(1)
print s.pop(1)
print s.pop(1)
print s.pop(1)
print s.pop(1)
print s.pop(1)
print s.__repr__()
print "#####"
print s.pop(2)
print s.pop(2)
print s.pop(2)
print s.pop(2)
print s.pop(2)
print s.pop(2)
print s.pop(2)
print s.pop(2)
print s.pop(2)
print s.__repr__()
print s.pop(3)
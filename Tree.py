class Node():
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
    def __repr__(self):
        return self.value
    def depth(self):
        leftdepth = 0
        if self.left:
            leftdepth = self.left.depth()
        rightdepth = 0
        if self.right:
            rightdepth = self.right.depth()
        return max(leftdepth,rightdepth) + 1
    def depthNew(self):
        leftdepth = 0
        if self.left:
            leftdepth = self.left.depthNew()
        rightdepth = 0
        if self.right:
            rightdepth = self.right.depthNew()

        if abs(leftdepth-rightdepth) > 1:
            return -1

        if leftdepth == -1 or rightdepth == -1:
            return -1
        
        return max(leftdepth,rightdepth) + 1

    def depthNoHack(self):
        leftdepth = 0
        if self.left:
            (leftbalanced,leftdepth) = self.left.depthNoHack()
        rightdepth = 0
        if self.right:
            (rightbalanced,rightdepth) = self.right.depthNoHack()

        maxdepth = max(leftdepth,rightdepth) + 1
        isBalanced = leftbalanced and rightbalanced and abs(leftdept - rightdepth) <= 1

        return (isBalanced, maxdepth)

class BinaryTree():
    def __init__(self):
        self.start = None
    def __repr__(self):
        def helper(top):
            if top is None:
                return ""
            else:
                return helper(top.left) + str(top.__repr__()) + helper(top.right)

        return helper(self.start)
        
    def add(self, node):
        def addhelper(top, node):
            if node.value < top.value:
                if top.left is None:
                    top.left = node
                else:
                    addhelper(top.left, node) 
            else:
                if top.right is None:
                    top.right = node
                else:
                    addhelper(top.right, node)
            
        if self.start is None:
            self.start = node
        else:
            addhelper(self.start, node)        

    def insert(self,node):
        def addhelper(top, node):
            if top is None:
                return node
            if node.value < top.value:
                top.left = addhelper(top.left, node)
            else:
                top.right = addhelper(top.right, node)
            return top
            
        self.start = addhelper(self.start, node)

    def depth(self):
        return self.start.depth()


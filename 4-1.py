from Tree import *

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(4)

tree = BinaryTree()
tree.add(a)
tree.add(b)
tree.add(c)
tree.add(d)
print tree

def check(node):
    if node is None:
        return True

    leftdepth = 0
    rightdepth = 0
    if node.left:
        leftdepth = node.left.depth()
    if node.right:
        rightdepth = node.right.depth()

    if abs(leftdepth - rightdepth) > 1:
        return False
    else:
        return check(node.left) and check(node.right)

print "depth: ", check(tree.start)

def checkNew(node):
    if node.depthNew() == -1:
        return False
    else:
        return True

print "depth: ", checkNew(tree.start)
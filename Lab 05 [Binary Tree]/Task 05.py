# -*- coding: utf-8 -*-
"""

Task 5
"""

def summation(root):
    if root == None:
        return 0
    return root.elem + summation(root.left) + summation(root.right)


def subtract_summation(root):
    if root == None:
        return 0
    left = summation(root.left)
    right = summation(root.right)
    return left - right


#Driver Code
root=BTNode(71)
#Write other nodes by yourself from the given tree of Doc File
node1 = BTNode(27)
node2 = BTNode(62)

root.left = node1
root.right = node2

node3 = BTNode(80)
node4 = BTNode(75)

node1.left = node3
node1.right = node4

node5 = BTNode(87)
node6 = BTNode(56)

node3.left = node5
node3.right = node6

node7 = BTNode(41)
node8= BTNode(3)

node2.left = node7
node2.right = node8

node9 = BTNode(19)
node10 = BTNode(89)

node8.left = node9
node8.right = node10

print(subtract_summation(root)) #This should print 111
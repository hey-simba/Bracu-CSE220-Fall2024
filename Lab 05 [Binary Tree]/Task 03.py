# -*- coding: utf-8 -*-
"""

Task 3
"""

def helper (root, sum=0, i=0):
  if root is None:
    return sum
  else:
    if i==0:
      sum+= root.elem
    else:
      sum+= root.elem%i
    sum= helper(root.left, sum, i+1)
    sum= helper(root.right,sum, i+1)
  return sum

def sumTree(root):
  return helper(root)

#Driver Code
#Input 1
root1 = BTNode(9)
node2 = BTNode(4)
node3 = BTNode(5)
node4 = BTNode(18)
node5 = BTNode(14)
node6 = BTNode(3)
node7 = BTNode(54)
node8 = BTNode(12)
node9 = BTNode(8)
node10 = BTNode(91)
node11 = BTNode(56)

root1.left = node2
root1.right = node3

node2.left = node4

node3.left = node5
node3.right = node6

node4.left = node7
node4.right = node8

node5.left = node9

node8.left = node10
node8.right = node11

print(sumTree(root1)) #This should print 15
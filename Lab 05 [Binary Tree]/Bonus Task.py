# -*- coding: utf-8 -*-
"""

Bonus Task
"""

def helper(root, level=0,sum=0):
  if root is None:
    return sum
  else:
    if level%2!=0:
      sum+=root.elem
    else:
      sum-=root.elem
    sum= helper(root.left,level+1,sum)
    sum=helper(root.right,level+1,sum)
  return sum

def level_sum(root):
  return helper(root)

#DRIVER CODE
root = BTNode(1)
n2 = BTNode(2)
n3 = BTNode(3)
n4 = BTNode(4)
n5 = BTNode(5)
n6 = BTNode(6)
n7 = BTNode(7)
n8 = BTNode(8)
root.left = n2
root.right = n3

n2.left = n4
n3.left = n5
n3.right = n6

n5.left = n7
n5.right = n8


print(level_sum(root)) #This should print 4
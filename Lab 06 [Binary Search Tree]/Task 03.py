# -*- coding: utf-8 -*-
"""

Task 3
"""

def sum_of_leaves(root, sum):
  if root is None:
    return sum

  if root.left is None and root.right is None:
      sum+=root.elem

  sum= sum_of_leaves(root.left,sum)
  sum= sum_of_leaves(root.right,sum)
  return sum


#DRIVER CODE
#Write by yourself from the given tree
#DRIVER CODE
root = BTNode(30)
root.left = BTNode(10)
root.left.left = BTNode(3)
root.left.right=BTNode(15)
root.left.left=BTNode(2)
root.right=BTNode(40)
root.right.right=BTNode(55)
root.right.left=BTNode(35)
root.right.left.right=BTNode(36)

print(sum_of_leaves(root, 0))
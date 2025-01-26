# -*- coding: utf-8 -*-
"""
Task 1
"""

def LCA(root, x, y):
  if root == None:
      return root
  if x < root.elem:
    if y < root.elem:
      return LCA(root.left, x, y)
  if x > root.elem :
    if  y > root.elem:
      return LCA(root.right, x, y)
  return root.elem


#DRIVER CODE
root = BTNode(15)
root.left = BTNode(10)
root.left.left = BTNode(8)
root.left.right= BTNode(12)
root.left.left.left= BTNode(6)
root.left.left.right= BTNode(9)
root.right= BTNode(25)
root.right.left= BTNode(20)
root.right.right= BTNode(30)
root.right.left.left= BTNode(18)
root.right.left.right= BTNode(22)
print(LCA(root,6,12))
print(LCA(root,20,6))
print(LCA(root,18,22))
print(LCA(root,20,25))
print(LCA(root,10,12))
#Write by yourself from the given tree (Create parent node and its corresponding left and right children nodes)
#check all the sample inputs given
#You can take help by seeing the driver code of Lab-6
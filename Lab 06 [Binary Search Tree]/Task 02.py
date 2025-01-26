# -*- coding: utf-8 -*-
"""
Task 2
"""

def find_path(root, key):
  li= []
  while root is not None:
    if key<root.elem:
      li.append(root.elem)
      root= root.left


    elif key>root.elem:
      li.append(root.elem)
      root= root.right

    else:
      li.append(root.elem)
      return li
  if root is None:
    return "No Path found"




#DRIVER CODE
#Write by yourself from the given tree
root= BTNode(30)
root.left= BTNode(10)
root.right= BTNode(40)
root.left.left= BTNode(3)
root.left.right= BTNode(15)
root.right.left= BTNode(35)
root.right.right= BTNode(55)

print(find_path(root,15))
#This should print [30,10,15]

print(find_path(root,50))
#This should print No Path Found
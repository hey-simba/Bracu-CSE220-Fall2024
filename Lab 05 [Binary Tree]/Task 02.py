# -*- coding: utf-8 -*-
"""
Task 2
"""

def smallest_level(root, level={}, i=0):
    if root is None:
        return level

    if i not in level:
        level[i] = root.elem

    else:
        if root.elem < level[i]:
            level[i] = root.elem

    smallest_level(root.left, level, i + 1)
    smallest_level(root.right, level, i + 1)

    return level

#DRIVER CODE
root = tree_construction([None, 4,9,2,3,-5,None,7])
print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  3 9 5 4 2 7
print()
print('Level Wise Smallest Value: ', end = ' ')
print(smallest_level(root)) #Level Wise Smallest Value:  {0: 4, 1: 2, 2: -5}

#practice ## must note this in mind

def helper(root,level={}, i=0):
  if root is None:
    return level

  else:
    if i not in level:
      level[i]= root.elem
    else:
      if root.elem<level[i]:
        level[i]= root.elem

  helper(root.left,level, i+1)
  helper(root.right,level, i+1)
  return level


def smallest_level(root):
  return helper(root)


#DRIVER CODE
root = tree_construction([None, 4,9,2,3,-5,None,7])
print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  3 9 5 4 2 7
print()
print('Level Wise Smallest Value: ', end = ' ')
print(smallest_level(root)) #Level Wise Smallest Value:  {0: 4, 1: 2, 2: -5}
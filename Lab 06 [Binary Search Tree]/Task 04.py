# -*- coding: utf-8 -*-
"""

Task 4
"""

def inorder_predecessor(root, x):
  predecessor = None
  current = root
  while current:
    if x.elem < current.elem:
       current = current.left
    elif x.elem > current.elem:
        predecessor = current
        current = current.right
    else:

      if current.left:

        temp = current.left
        while temp.right:
          temp = temp.right
          predecessor = temp
      break

  return predecessor
#DRIVER CODE
root = BTNode(20)
n1 = BTNode(8)
n2 = BTNode(22)
n3 = BTNode(4)
n4 = BTNode(12)
n5 = BTNode(10)
n6 = BTNode(14)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n4.left = n5
n4.right = n6

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  4 8 10 12 14 20 22
print()

x = root
print(f'Inorder predecessor of node {x.elem}: {inorder_predecessor(root, x).elem}') #Inorder predecessor of node 20: 14
x = root.left.right.right
print(f'Inorder predecessor of node {x.elem}: {inorder_predecessor(root, x).elem}') #Inorder predecessor of node 14: 12
x = root.left.right.left
print(f'Inorder predecessor of node {x.elem}: {inorder_predecessor(root, x).elem}') #Inorder predecessor of node 10: 8
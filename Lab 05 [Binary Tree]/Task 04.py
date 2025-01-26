# -*- coding: utf-8 -*-
"""

Task 4
"""

def swap_child(root, level, M):
  if root is None:
    return root
  else:
    if level< M:
      root.left, root.right= root.right, root.left
      swap_child(root.left, level+1, M)
      swap_child(root.right, level+1, M)
      return root




#Driver Code
nodeA = BTNode('B')
nodeB = BTNode('C')
root.left = nodeA
root.right = nodeB

nodeC = BTNode('D')
nodeD = BTNode('E')
nodeA.left = nodeC
nodeA.right = nodeD

nodeE = BTNode('G')
nodeF = BTNode('H')
nodeC.left = nodeE
nodeC.right = nodeF

nodeG = BTNode('I')
nodeD.left = nodeG

nodeH = BTNode('F')
nodeB.right = nodeH

nodeI = BTNode('J')
nodeH.left = nodeI


print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root)   #Given Tree Inorder Traversal: G D H B I E A C J F
print()

root2 = swap_child(root, 0, 2)
print('Swapped Tree Inorder Traversal: ', end = ' ')
inorder(root2)  #Swapped Tree Inorder Traversal: J F C A I E B G D H
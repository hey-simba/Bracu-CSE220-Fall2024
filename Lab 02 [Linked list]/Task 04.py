# -*- coding: utf-8 -*-
"""
Task 4: Word Decoder
"""

def retrieve_elem(head, idx):
    temp = head
    count = 0
    while (temp!=None):
        if count == idx:
            return temp.elem
            break
        temp = temp.next
        count += 1
    return None

def word_Decoder(head):
  count  = 0
  temp = head
  while temp != None:
    count += 1
    temp = temp.next

  x = 13 % count
  new_head= None

  temp_2= head
  idx=0
  while(temp_2!=None):
    if idx>0 and idx<count:
      if idx%x==0:
        node= retrieve_node(head, idx)
        node_elem= node.elem

        n= Node(node_elem, new_head)
        new_head = n

    idx+=1
    temp_2=temp_2.next

  none_node= Node(None, None)
  none_node.next= new_head
  new_head= none_node

  return new_head


#Driver Code
print('==============Test Case 1=============')
head = createList(np.array(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C']))
print("Encoded Word:")
printLinkedList(head) #This should print B→M→D→T→N→O→A→P→S→C

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→C→A→T

print('==============Test Case 2=============')

head = createList(np.array(['Z', 'O', 'T', 'N', 'X']))
print("Encoded Word:")
printLinkedList(head) #This should print Z→O→T→N→X

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→N
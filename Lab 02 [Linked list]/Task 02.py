# -*- coding: utf-8 -*-
"""
Task 2: Remove Compartment
"""

def Count(head):
  temp=head
  total_node=0
  while(temp!=None):
    total_node+=1
    temp=temp.next
  return total_node

def retrieve_node(head,idx):
  temp=head
  count=0
  while temp != None:
    if count == idx:
      return temp
    temp = temp.next
    count += 1
  return None


def remove_compartment(head,n):
  total_node= Count(head)
  temp=head
  n=(total_node-n)

  if (n==0):
      temp=head.next
      head.next=None
      head=temp
  elif n>0 and n<total_node:
      prev_node= retrieve_node(head,n-1)
      current_node=prev_node.next
      prev_node.next=current_node.next
      current_node.next=None
  else:
      return head
  return head


print('==============Test Case 1=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,2)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->72
print()
print('==============Test Case 2=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,7)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->56-->72
print()
print('==============Test Case 3=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,6)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 15-->34-->41-->56-->72
print()
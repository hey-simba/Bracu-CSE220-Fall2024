
"""
Bonus Task: ID Generator
"""

def retrieve_node(head,idx):
  temp=head
  count=0
  while temp != None:
    if count == idx:
      return temp

    temp = temp.next
    count += 1


def idGenerator(head1, head2, head3):

  new_head= Node(head1.elem, None)
  temp1 = head1.next
  while temp1 != None:
    n = Node(temp1.elem, new_head)
    new_head = n
    temp1 = temp1.next

  temp2= head2
  temp3=head3

  count=0

  while(temp2!=None and temp3!=None):

    retrieve_1= retrieve_node(head2,count)
    retrieve_2= retrieve_node(head3,count)
    if retrieve_1 != None and retrieve_2 != None:
     val1 = retrieve_1.elem
     val2= retrieve_2.elem
    sum= val1+ val2

    node= Node(sum, None)
    sum=0
    total_node= Count(new_head)
    last_node= retrieve_node(new_head, total_node-1)
    last_node.next= node

    count+=1
    temp2= temp2.next
    temp3= temp3.next

  return new_head
print('==============Test Case 1=============')
head1 = createList(np.array([0,3,2,2]))
head2 = createList(np.array([5,2,2,1]))
head3 = createList(np.array([4,3,2,1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print  2 → 2 → 3 → 0 → 9 → 5 → 4 → 2


print('==============Test Case 2=============')
head1 = createList(np.array([0,3,9,1]))
head2 = createList(np.array([3,6,5,7]))
head3 = createList(np.array([2,4,3,8]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print 1 → 9 → 3 → 0 → 5 → 10 → 8 → 15
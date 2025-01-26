# -*- coding: utf-8 -*-
"""

Task 5: Alternate Merge
"""

def alternate_merge(head1, head2):
    new_head = None
    current = None
    temp_1 = head1
    temp_2 = head2

    count = 1


    while temp_1!= None or temp_2 != None:
        if count % 2 != 0:
                new_node = Node(temp_1.elem, None)
                if new_head ==None:
                    new_head = new_node
                    current = new_head
                else:
                    current.next = new_node
                    current = current.next
                temp_1 = temp_1.next
        else:
                new_node = Node(temp_2.elem, None)
                current.next = new_node
                current = current.next
                temp_2 = temp_2.next

        count += 1

    return new_head
print('==============Test Case 1=============')
head1 = createList(np.array([1,2,6,8,11]))
head2 = createList(np.array([5,7,3,9,4]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print    1 --> 5 --> 2 --> 7 --> 6 --> 3 --> 8 --> 9 --> 11 --> 4


print('==============Test Case 2=============')
head1 = createList(np.array([5, 3, 2, -4]))
head2 = createList(np.array([-4, -6, 1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print    5 → -4 -> 3 → -6 -> 2 -> 1 -> -4


print('==============Test Case 3=============')
head1 = createList(np.array([4, 2, -2, -4]))
head2 = createList(np.array([8, 6, 5, -3]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print   4-> 8 → 2-> 6 → -2 → 5 → -4 -> -3
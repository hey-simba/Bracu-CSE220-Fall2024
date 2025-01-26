# -*- coding: utf-8 -*-
"""
Task 3: Assemble Conga Line
"""

def Count(head):
  temp=head
  total_node=0
  while(temp!=None):
    total_node+=1
    temp=temp.next
  return total_node

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


def assemble_conga_line(conga_line):
  conga=True

  temp=conga_line
  res=conga_line.elem
  count=1
  total_node=Count(head)

  while(temp!=None):
    if(count>0 and count<total_node):
      after_node=retrieve_node(conga_line,count+1)
      after_elem = after_node.elem
      if (after_elem>=res):
        res= after_elem
      else:
        conga= False
        break
    temp=temp.next
    count+=1
  return conga


print('==============Test Case 1=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print True
unittest.output_test(returned_value, True)
print()
print('==============Test Case 2=============')
conga_line = createList(np.array([10,15,44,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print False
unittest.output_test(returned_value, False)
print()
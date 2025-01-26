# -*- coding: utf-8 -*-
"""
Task 1: Building Blocks
"""

def count (head):
  count= 0
  temp=head
  while(temp!=None):
    count+=1
    temp=temp.next
  return count

def check_similar(building_1, building_2):
  similar= True
  total_nodes_1= count(building_1)
  total_nodes_2=count(building_2)

  if total_nodes_1!=total_nodes_2:
    similar= False

  temp_1=building_1
  temp_2=building_2

  while(temp_1!=None and temp_2!=None):
    if (temp_1.elem != temp_2.elem):
      similar=False
      break

    temp_1=temp_1.next
    temp_2=temp_2.next
  if similar:
    return "Similar"
  else:
    return "Not Similar"


print('==============Test Case 1=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Similar'
unittest.output_test(returned_value, 'Similar')
print()

print('==============Test Case 2=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Yellow', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()

print('==============Test Case 3=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()

print('==============Test Case 4=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()
# -*- coding: utf-8 -*-
"""
Task 1: Diamond Count
"""

def diamond_count(stack,string):

  for char in string:
      stack.push(char)

  temp1= Stack()
  temp2= Stack()

  while stack.isEmpty()!=True:
    a= stack.pop()
    if a== "<":
      temp1.push(a)
    elif a== ">":
      temp2.push(a)

  count1=0
  while(temp1.isEmpty()!=True):
    temp1.pop()
    count1+=1

  count2=0
  while(temp2.isEmpty()!=True):
    temp2.pop()
    count2+=1
  if count1>count2 or count1==count2:
    return count2
  else:
    return count1

print('Test 01')
stack = Stack()
string = '<..><.<..>> '
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')


print('Test 02')
stack = Stack()
string = '<<<..<......<<<<....>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 1
unittest.output_test(returned_value, 1)
print('-----------------------------------------')


print('Test 03')
stack = Stack()
string = '>>><...<<..>>...>...>>>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')
# -*- coding: utf-8 -*-
"""
Task 3: Stack Reverse
"""

def conditional_reverse(stack):
  temp= Stack()
  temp.push(stack.pop())

  while stack.isEmpty()!=True:
    a= temp.peek()
    b= stack.peek()
    if a!=b:
      temp.push(stack.pop())
    else:
      stack.pop()
  return temp

print('Test 01')
st=Stack()
st.push(10)
st.push(10)
st.push(20)
st.push(20)
st.push(30)
st.push(10)
st.push(50)
print('Stack:')
print_stack(st)
print('------')
reversed_stack=conditional_reverse(st)
print('Conditional Reversed Stack:')
print_stack(reversed_stack) # This stack contains 50, 10, 30, 20, 10 in this order whereas top element should be 10
print('------')
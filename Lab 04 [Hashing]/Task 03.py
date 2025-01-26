# -*- coding: utf-8 -*-
"""

Task 3

Implement the __hash_function() and insert() methods
"""

class Node:
  def __init__(self, value=None, next = None):
    self.value = value
    self.next = next

class HashTable:
  def __init__(self, length):
    n = Node()
    self.ht = [n] * length
    self.length = length

  def show(self):
    count = 0
    for i in self.ht:
      temp = i
      print(count, end=" ")
      while temp!=None:
        print (temp.value, end="-->")
        temp = temp.next
      count += 1
      print()


  #Do it by yourself
  def __hash_function(self, key):
    sum=0
    if len(key)%2==0:
        for j in range(0,len(key),2):
          sum+= ord(key[j])
    else:
        for j in range(1,len(key),2):
          sum+=ord(key[j])
    idx= sum % len(self.ht)
    return idx

  #Do it by yourself
  def insert(self, key, value):
    node= Node((key,value),None)
    idx= self.__hash_function(key)

    if self.ht[idx].value is None:
      self.ht[idx] = node
    else:
      count=0
      prev= None
      current= self.ht[idx]
      while current is not None:
        if current.value[1]< node.value[1]:
          if prev is None:
            node.next= current
            self.ht[idx] = node

          else:
            prev.next= node
            node.next=current
          return


        prev=current
        current=current.next
      prev.next = node

#Driver Code
ht = HashTable(3)

print("------Test#1------")
ht.insert("apple", 20)
ht.insert("coconut", 90)
ht.insert("cherry", 50)
ht.show()
print("------Test#2------")
ht.insert("banana", 30)
ht.insert("pineapple", 50)
ht.show()
print("------Test#3------")
ht.insert("apple", 100)
ht.insert("Guava", 10)
ht.show()

# Driver Code Output:
# 0 ('coconut', 90)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)-->('pineapple', 50)-->('banana', 30)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)--> ('pineapple', 50)--> ('banana', 30)-->
# 1 ('apple', 100)--> ('apple', 20)--> ('Guava', 10)-->
# 2 ('cherry', 50)-->
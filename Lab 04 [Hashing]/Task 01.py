# -*- coding: utf-8 -*-
"""
Task 1

You will have to complete the vehicleNodes constructor and then

implemenet the __hash_function() and insert_vehicle() methods.
"""

#Complete this constructor
class vehicleNodes:
  def __init__(self, brand, vehicle_type, rent, passenger, next = None):
    self.brand = brand
    self.vehicle_type = vehicle_type
    self.rent = rent
    self.passenger = passenger
    self.next = next

class VehicleHashTable:
  def __init__(self, size):
    self.vehicleTable = [None]*size
    self.empty_slot = {}
    for i in range(size):
      self.empty_slot[i] = False

  def create_from_vehicle_info_array(self, arr):
    for i in arr:
      self.insert_vehicle(i)

  def print_vehicle_hashtable(self):
    idx = 0
    for i in self.vehicleTable:
      print(idx, ':', end = ' ')
      head = i
      while head != None:
        print(f'(Brand: {head.brand}, Type: {head.vehicle_type}, Rent: {head.rent}, No. of Passengers: {head.passenger})', end = '---->')
        head = head.next
      print('None')
      print()
      idx += 1

  def find_empty_slot(self):
    for k,v in self.empty_slot.items():
      idx = k
      del self.empty_slot[k]
      return idx


  #Do it by yourself
  def __hash_function(self, brand):
      index= 0
      sum=0
      for char in brand:
        sum+= ord(char)
      index= sum% len(self.vehicleTable)

      # Do not discard the next 3 lines
      if index in self.empty_slot:
        del self.empty_slot[index]
      return index


  #Do it by yourself
  def insert_vehicle(self, vehicle):
    idx= self.__hash_function(vehicle[0])
    node = vehicleNodes(vehicle[0], vehicle[1], vehicle[2], vehicle[3])
    if self.vehicleTable[idx] is None:
      self.vehicleTable[idx] = node
    else:
      current = self.vehicleTable[idx]
      if current.brand==vehicle[0]:
        while current.next is not None:
          current= current.next
        current.next=node
      else:
        new_idx= self.find_empty_slot()
        self.vehicleTable[new_idx] = node

    return self.vehicleTable

#DRIVER CODE
vehicle_info = [('Toyota', 'Private Car', 500, 4), ('Jeep', 'SUV', 950, 6), ('Lamborghini', 'SUV', 6900, 6), ('Hyundai', 'Bike', 100, 1), ('BMW', 'Private Car', 1000, 8), ('Honda', 'Bike', 150, 1), ('Ferrari', 'Private Car', 2500, 4), ('BMW', 'Minivan', 5800, 7)]

vt = VehicleHashTable(len(vehicle_info))

vt.create_from_vehicle_info_array(vehicle_info)
print("============== Printing The HashTable ==============")
vt.print_vehicle_hashtable()

# should print
# 0 : (Brand: Toyota, Type: Private Car, Rent: 500, No. of Passengers: 4)---->None

# 1 : (Brand: Lamborghini, Type: SUV, Rent: 6900, No. of Passengers: 6)---->None

# 2 : (Brand: Hyundai, Type: Bike, Rent: 100, No. of Passengers: 1)---->None

# 3 : (Brand: Honda, Type: Bike, Rent: 150, No. of Passengers: 1)---->None

# 4 : (Brand: Jeep, Type: SUV, Rent: 950, No. of Passengers: 6)---->None

# 5 : (Brand: Ferrari, Type: Private Car, Rent: 2500, No. of Passengers: 4)---->None

# 6 : (Brand: BMW, Type: Minivan, Rent: 5800, No. of Passengers: 7)---->(Brand: BMW, Type: Private Car, Rent: 1000, No. of Passengers: 8)---->None

# 7 : None
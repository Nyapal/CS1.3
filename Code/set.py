# Choose a DS to implement your set with 
#from binary import Binary
from hashtable import HashTable 

class Set():
  '''initialize a new empty set structure, and add each element if a sequence is given'''
  def __init__(self, elements=None):
    self.hashtable_set = HashTable()
    if elements is not None:
      for ele in elements:
        self.add(ele)

  '''size - property that tracks the number of elements in constant time'''
  def size(self):
    return self.hashtable_set.size
  
  '''contains(element) - return a boolean indicating whether element is in this set'''
  def contains(self, element):
    return self.hashtable_set.contains(element)

  '''add(element) - add element to this set, if not present already'''
  def add(self, element):
    if not self.hashtable_set.contains(element):
      self.hashtable_set.set(element, None)


  '''remove(element) - remove element from this set, if present, or else raise KeyError'''
  def remove(self, element):
    if self.hashtable_set.contains(element):
      self.hashtable_set.delete(element)
    else:
      raise ValueError('Item not found')

  '''union(other_set) - return a new set that is the union of this set and other_set'''
  def union(self, other_set):
    new_set = Set()
    for element in other_set.keys():
      new_set.add(element)
    for element in self.hashtable_set.keys():
      new_set.add(element)
    return new_set

  '''intersection(other_set) - return a new set that is the intersection of this set and other_set'''
  def intersection(self, other_set):
    new_set = Set()
    for element in other_set:
      if self.contains(element):
        new_set.add(element)
    return new_set

  '''difference(other_set) - return a new set that is the difference of this set and other_set'''
  def difference(self, other_set):
    new_set = Set()
    for element in self:
      if not other_set.contains(element):
        new_set.add(element)
    return new_set

  '''is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set'''
  def is_subset(self, other_set):
    pass
    # for element in self:
    #   if not other_set.contains(element):
    #     return False 
    # return True

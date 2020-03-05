from sets import Set
import unittest

class SetTest(unittest.TestCase):

  def test_init_empty(self):
    s = Set()
    assert s.size() == 0

  def test_init(self):
    s = Set([1, 3, 5])
    assert s.size() == 3
  
  def test_contains(self):
    s = Set([1, 2, 3])
    assert s.contains(1) == True
    assert s.contains(3) == True
    assert s.contains(5) == False
    assert s.size() == 3

  def test_add(self):
    s = Set()
    s.add(1) == True 
    s.add(2) == True 
    s.add(3) == True 
    s.add(4) == True 
    s.add(5) == True 
    assert s.size() == 5

  def test_remove(self):
    s = Set(['a', 3, 6, 9, 12, None, 'i'])
    assert s.size() == 7
    s.remove(12)
    assert s.size() == 6
    assert s.contains('a') == True
    s.remove('a')
    assert s.contains('a') == False

  def test_union(self):
    a = Set([1, 2, 3, 4, 5])
    b = Set([4, 5, 6, 7, 8])
    a_union_b = a.union(b)
    assert a_union_b.contains(8) == True
    assert a_union_b.contains(2) == True
    assert a_union_b.contains(4) == True
    assert a_union_b.contains(0) == False
    assert a_union_b.contains(9) == False
    assert a_union_b.size() == 8

  def test_intersection(self):
    a = Set([1, 2, 3, 4, 5])
    b = Set([4, 5, 6, 7, 8])
    a_intersection_b = a.intersection(b)
    assert a_intersection_b.contains(1) == False
    assert a_intersection_b.contains(8) == False
    assert a_intersection_b.contains(4) == True
    assert a_intersection_b.contains(5) == True
    a.add('a')
    b.add('a')
    a.add(2.5)
    a_intersection_b = a.intersection(b)
    assert a_intersection_b.contains('a') == True
    assert a_intersection_b.contains(2.5) == False
  
  def test_difference(self):
    a = Set([1, 2, 3, 4, 5])
    b = Set([4, 5, 6, 7, 8])
    a_difference_b = a.difference(b)
    assert a_difference_b.contains(4) == False
    assert a_difference_b.contains(5) == False
    assert a_difference_b.contains(1) == True
    assert a_difference_b.contains(2) == True
    b.remove(4)
    a_difference_b = a.difference(b)
    assert a_difference_b.contains(4) == True

  def test_is_subset(self):
    a = Set([1, 2, 3])
    b = Set([1, 2, 4, 5])
    assert a.is_subset(b) == False
    a.add(3)
    a.add(4)
    a.add(5)
    assert a.is_subset(b) == True
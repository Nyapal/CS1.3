from set import Set
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
    pass

  def test_intersection(self):
    pass
  

  def test_difference(self):
    pass

  def test_is_subset(self):
    pass

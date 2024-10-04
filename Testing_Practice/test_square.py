import unittest

def calculate_square(number):
  return number * number 


class Square(unittest.TestCase):
  
  def test_square_positive(self):
    self.assertEqual(calculate_square(2), 4)
    
  def test_square_negative(self):
    self.assertEqual(calculate_square(-3), 9)
    
    

if __name__ == "__main__":
  unittest.main()
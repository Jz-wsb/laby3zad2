import unittest
from app import add, substract, multiply

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    
    def test_substract(self): 
        self.assertEqual(substract(2, 3), -1)

    def test_multiply(self): 
        self.assertEqual(multiply(2, 3), 6)

if __name__ == '__main__':
    unittest.main()

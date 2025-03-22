import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), "The sum is 5")

if __name__ == "__main__":
    unittest.main()
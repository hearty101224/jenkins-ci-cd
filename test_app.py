import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(2, 3), "The sum is 5")

if __name__ == "__main__":
    unittest.main()
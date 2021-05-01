import unittest
import calculator

class testCaseAdd(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(calculator.calc(5,10), (15,-5,50,0.5))

if __name__ == "__main__":
    unittest.main()

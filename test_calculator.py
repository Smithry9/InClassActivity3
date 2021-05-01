import unittest
import calculator

class testCaseAdd(unittest.TestCase):
    #Tests that should pass
    def test_calc1(self):
        self.assertEqual(calculator.calc(5,10), (15,-5,50,0.5))
    def test_calc2(self):
        self.assertEqual(calculator.calc(4,2), (6,2,8,2.0))
    def test_calc3(self):
        self.assertEqual(calculator.calc(1,4), (5,-3,4,0.25))

    #Test that should fail
    def test_calc4(self):
        self.assertEqual(calculator.calc(4,8), (1,-1,1,1))

if __name__ == "__main__":
    unittest.main()

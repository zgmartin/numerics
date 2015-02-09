import unittest
from roots import bisection
from numpy.polynomial import Polynomial

class RootTest(unittest.TestCase):

    def setUP(self):
        self.poly = Polynomial([1,3,2], [-3,2])
        self.inter = [-2,.0]
        self.tol = 0.2


    def bisect_test(self):
        result = bisection(self.poly,self.inter,self.tol)
        answer = 1.0
        
        self.assertEquals(result,answer)

if __name__ == '__main__':
    unittest.main()
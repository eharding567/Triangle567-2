import unittest
import math
from triangle_1 import classify_triangle

class test_cases(unittest.TestCase):
    def testMySet1(self):
        self.assertEqual(classify_triangle(1,2,3),"Scalene")
        self.assertEqual(classify_triangle(4,2,3),"Scalene")
        self.assertEqual(classify_triangle(3,2,3),"Isoceles")
        self.assertEqual(classify_triangle(60,60,55),"Isoceles")
        self.assertEqual(classify_triangle(1,1,1),"Equilateral")
        self.assertEqual(classify_triangle(75,75,75),"Equilateral")
        self.assertEqual(classify_triangle(3,4,5),"Right Scalene")
        self.assertEqual(classify_triangle(5,12,13),"Right Scalene")
        self.assertEqual(classify_triangle(math.sqrt(2),1,1),"Right Isosceles")
        self.assertEqual(classify_triangle(344,4,5),"InvalidInput")
        self.assertEqual(classify_triangle(5,3903,1300),"InvalidInput")
        self.assertEqual(classify_triangle('z',1,2),"InvalidInput")
        self.assertEqual(classify_triangle(0,1,2), "InvalidInput")
        self.assertEqual(classify_triangle(1,-2,2), "InvalidInput")
        self.assertEqual(classify_triangle(1,2,0), "InvalidInput")
        self.assertEqual(classify_triangle(1,22,2), "NotATriangle")
        self.assertEqual(classify_triangle(65,1,1), "NotATriangle")
        self.assertEqual(classify_triangle(1,1,65), "NotATriangle")


if __name__ == '__main__':
    unittest.main(exit=False)

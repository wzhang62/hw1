import unittest
from hw1 import classify_triangle

class test_triangles(unittest.TestCase):

    def testRightTriangleA(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Triangle', '3,4,5 is a right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Right Triangle', '5,3,4 is a right triangle')

    def testEquilateralTriangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral Triangle', '3,3,3 should be equilateral')

    def testIsoscelesTriangle(self):
        self.assertEqual(classify_triangle(7, 6, 6), 'Isosceles Triangle', '7,6,6 is a isosceles triangle')

    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(5, 7, 9), 'Scalene Triangle', '3,4,5 is a scalene triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
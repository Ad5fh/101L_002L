## Aissatou Diallo
## ad5fh@umsystem.edu 
## CS 101 Lab
##PROBLEM: Testing
##Algorithm: The program below is used to test if the functions in the Grades.py file is working properly. 
#################################################################################################################################

import unittest
import Grades
import math

class Grade_test(unittest.TestCase):

    def test_total_returns_total_of_list(self):
        result= Grades.Total([1,10,22])
        self.assertEqual(result,33, 'The total function should return 33')

    def test_total_returns_0(self):
        result= Grades.Total([])
        self.assertEqual(result,0, 'The total function should return 0')

    def test_average_one(self):
        result= Grades.Average([2,5,9])
        self.assertAlmostEqual(result,5.33333333333333)
       
    def test_average_two(self):
        result= Grades.Average([2,15,22,9])
        self.assertAlmostEqual(result,12)
    
    def test_average_nan(self):
        result= Grades.Average([])
        self.assertIs(result,math.nan)
    
    def test_median_one(self):
        result= Grades.Median([2,5,1])
        self.assertEqual(result,2)

    def test_median_two(self):
        result= Grades.Median([5,2,1,3])
        self.assertEqual(result,2.5)

    def test_median_returns_ValueError(self):
        with self.assertRaises(ValueError):
            result= Grades.Median([])
            self.assertIs(result)


unittest.main()
    